#!/usr/bin/env python3
# -*- coding: utf-8 -*-

DEBUG = False
MOCKDATA = False

JOLLA = False
try:
  import pyotherside
  JOLLA = True
except:
  pass

import os.path
import re
import http.cookiejar
import urllib.request, urllib.error, urllib.parse
import math
import time
import json
import threading
from datetime import date, datetime, timedelta

import Encryption

if MOCKDATA:
  import MockData

class SimpelScraper:

  update_timeout = 3600 # 1 Hours timeout
  data_file = '.SimpelScraper.data.bin' # Hidden data file
  history_file = '.SimpelScraper.history.bin' # Hidden data file

  def __init__(self, username = None ,password = None):
    try:
      self.encryption = Encryption.Encryption()
    except Encryption.EncryptionException as error:
      self.__notify_message('notification','Encryption error ' + str(error))

    self.encryption = Encryption.Encryption()
    self.__notify_message('notification','Encryption is ' + ('enabled' if self.encryption.isEnabled() else 'disabled'))
    self.login_ok = False
    self.reset_settings(False)

    # .Net postback form fields
    self.form_elements_regex = re.compile('<input .*name="(?P<name>[^"]+)"(.*value="(?P<value>[^"]*)")?[^>]+>', re.MULTILINE)

    # Generic email regex
    self.valid_email_regex  = re.compile("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$")

    # Use 1000 bytes factor for data useage
    self.internetdata_unit_factor = 1000
    self.internetdata_unit_name = 'MB'

    # Online pages with the data for scraping
    self.login_cookie = None
    self.portal_url   = 'https://www.mijnsimpel.nl'
    self.online_pages = {}

    # Login data
    self.online_pages['login'] = {'urlpath' : 'login.aspx' ,
                                  'regexes' : { 'login_detect' : re.compile('<h1>Inloggen op Mijn Simpel</h1>'),
                                                'login_check' : re.compile('<p>Welkom\s*<strong>\s*(?P<loginname>[^<]+)\s*</strong>,</p>', re.MULTILINE)
                                              }
                                  }

    # Account data
    self.online_pages['account'] = {'urlpath' : 'account.aspx' ,
                                    'regexes' : { 'data' : re.compile('<tr>\s*<td[^>]+>([^<]+)</td>\s*<td[^>]+>([^<]+)</td>')
                                                }
                                    }

    # Usage data
    self.online_pages['usage'] = {'urlpath' : 'credit.aspx' ,
                                  'regexes' : { 'call_usage' : re.compile('(\d+) minuten'),
                                                'sms_usage' : re.compile('(\d+) SMS'),
                                                'data_usage' : re.compile('(\d+) ' + self.internetdata_unit_name)
                                                }
                                    }

    # Account data
    self.online_pages['contract'] = {'urlpath' : 'simproperties.aspx' ,
                                    'regexes' : { 'data' : re.compile('<tr>\s*<td[^>]+>([^<]+)</td>\s*<td[^>]+>([^<]+)</td>'),
                                                  'mobilenumber': re.compile('Mijn Simpel voor (?P<mobile>\d{10})')
                                                }
                                    }

    # Plafond data
    self.online_pages['plafond'] = {'urlpath' : 'belplafond.aspx' ,
                                    'regexes' : { 'data' : re.compile('<tr>\s*<td[^>]*>\s*Plafond\s*</td>\s*<td[^>]*>\s*<span[^>]*>\s*(?P<plafond>€ \d+,\d{0,2})\s*<span>\s*</td>'),
                                                  'excluded': re.compile('<tr>\s*<td[^>]*>Telefoonnummer\s*(?P<counter>\d)\s*</td>\s*<td[^>]*>.*<input.*type="text".*(value="(?P<mobilenumber>))?".*/>\s*</span>\s*</td>')
                                                }
                                    }

    self.__load_application_data()

    self.__history_fields = {'data_update_timeout', 'sms_usage','call_usage','data_usage','days_usage'}
    self.__load_application_history()

    if username is not None:
      self.set_username(username)

    if password is not None:
      self.set_password(password)

    if self.login():
      self.__get_online_data()

    self.updater = threading.Thread(target=self.__auto_update)
    self.updater.daemon = True
    self.updater.start()

  def __notify_message(self,type,message):
    if JOLLA:
      pyotherside.send(type,str(message))

  def __print_debug(self,message):
    if DEBUG:
      try:
        print('[' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '] Python DEBUG: ' + str(message))
      except Exception as e:
        print('DEBUG countained non displayable chars....')

  def __load_application_data(self):
    if not os.path.isfile(SimpelScraper.data_file):
      return

    try:
      with open(SimpelScraper.data_file, mode='rb') as data_file:
        old_application_data = json.loads(self.encryption.decrypt(data_file.read()))
        self.application_data = dict(list(self.application_data.items()) + list(old_application_data.items()))
    except Exception as e:
      self.__notify_message('notification','Error loading data exception: ' + str(e))

  def __save_application_data(self):
    try:
      with open(SimpelScraper.data_file, mode='wb') as data_file:
        data_file.write(self.encryption.encrypt(json.dumps(self.application_data)))
    except Exception as e:
      self.__notify_message('notification','Error saving data exception: ' + str(e))

  def __load_application_history(self):
    if not os.path.isfile(SimpelScraper.history_file):
      return

    try:
      with open(SimpelScraper.history_file, mode='rb') as data_file:
        old_history_data = json.loads(self.encryption.decrypt(data_file.read()))
        self.history_data = dict(list(self.history_data.items()) + list(old_history_data.items()))
    except Exception as e:
      self.__notify_message('notification','Error loading history exception: ' + str(e))

  def __save_application_history(self):
    try:
      with open(SimpelScraper.history_file, mode='wb') as data_file:
        data_file.write(self.encryption.encrypt(json.dumps(self.history_data)))
    except Exception as e:
      self.__notify_message('notification','Error saving history exception: ' + str(e))

  def __add_history(self):
      history = {}
      for data_field in self.__history_fields:
          history[data_field] = self.application_data[data_field]

      self.history_data[str(self.application_data['last_update'])] = history
      self.__print_debug('Added data to history')
      self.__print_debug(self.history_data)
      self.__save_application_history()

  def __init_online_session(self):
    self.login_cookie = http.cookiejar.CookieJar()

    self.opener = urllib.request.build_opener(
        urllib.request.HTTPRedirectHandler(),
        urllib.request.HTTPSHandler(debuglevel=1),
        urllib.request.HTTPCookieProcessor(self.login_cookie))

    urllib.request.install_opener(self.opener)

  def __get_online_data(self,page = None,data = None,force_update = False):
    # Get online data when:
    #    1. Forced
    #    2. Postdata
    #    3. Outdated
    last_update = int(time.time()) - int(self.application_data['last_update'])
    self.__print_debug('Get online data for page: ' + str(page) + ' -> Forced: ' + str(force_update) + ', Data: ' + str(data is not None) + ', Outdated: ' + str(last_update > self.application_data['data_update_timeout']) + ', ' + str( int(self.application_data['data_update_timeout']) - (int(time.time()) - self.application_data['last_update'])) + ' seconds left')
    if force_update or (data is not None) or ( last_update > int(self.application_data['data_update_timeout'])):
      pages = self.online_pages
      if data is not None:
          pages = [page]

      for page in pages:
        if page == 'login':
          continue

        html = self.__process_online_data(page,data)
        self.__print_debug('Downloaded online data for page ' + page)
        #self.__print_debug(html)

        self.__parse_data(page,html)

      self.application_data['last_update'] = int(time.time())
      self.__add_history();
      self.__save_application_data()

  def __process_dotNet_form_fields(self,html):
    elements = {}
    # Get the form fields with keys
    elements_data = self.form_elements_regex.findall(html)
    if elements_data:
      for element in elements_data:
        elements[element[0]] = element[2]

    # Get the Javascript postback values
    elements_regex = re.compile('javascript:__doPostBack\(\'(?P<target>[^\']+)\',\'(?P<argument>[^\']*)\'\)', re.MULTILINE)
    elements_data = elements_regex.findall(html)
    if elements_data:
      for element in elements_data:
        elements['__EVENTTARGET'] = element[0]
        elements['__EVENTARGUMENT'] = element[1]

    return elements

  def __process_online_data(self,page,data = None):
    html = ''
    if page in self.online_pages:
      # .Net postBack form fixer
      # First load the form to get all the fields.
      if data is not None:
        self.__print_debug('Parsing dotNet form fields ' + page)
        formhtml = self.__process_online_data(page)
        fields = self.__process_dotNet_form_fields(formhtml)
        neededfields = {}
        self.__print_debug('Got .Net form data:')
        self.__print_debug(fields)

        for fielddata in data:
          for field in fields:
            if field.startswith('__'):
               neededfields[field] = fields[field]
            if fielddata in field:
              neededfields[field] = data[fielddata]

        data = neededfields.copy()

      if MOCKDATA:
        self.__print_debug('Using MOCK Data for page ' + page)
        html = MockData.getpage(page)
      else:
        post_data = None
        if data is not None:
          self.__print_debug('Posting data:')
          self.__print_debug(data)
          post_data = urllib.parse.urlencode(data).encode('utf-8')

        response = self.opener.open(self.portal_url + '/' + self.online_pages[page]['urlpath'],post_data)
        html = response.read().decode('utf-8')

        # Moet nog worden uitgezocht.... hangt van de cookies en sessies af
        #if page != 'login' and self.login_detect_regex.search(html):
        #  self.__notify_message('notification','Cookie expired, relogin for page' + page)
        #  if self.login():
        #    self.__print_debug('Recursive restart processing online data')
        #    html = self.__process_online_data(page,data)

    return html

  def __auto_update(self):
    while True:
      self.__print_debug('Auto update loop')
      if self.isLoggedIn():
        last_update = self.application_data['last_update']
        self.__get_online_data()

        if self.application_data['last_update'] != last_update:
          self.__notify_message('update-data','Updated data!')
      else:
          self.__print_debug('Not logged in (yet)')

      self.__print_debug('Do a new update in ' + str(SimpelScraper.update_timeout) + ' seconds')
      time.sleep(SimpelScraper.update_timeout)

  def __parse_data(self,type,html):
    if html == '':
      return

    self.__print_debug('Parse data for: ' + type)
    if type in self.online_pages:
      if 'account' == type:
        self.__parse_account_data(html)
      if 'usage' == type:
        self.__parse_usage_data(html)
      if 'contract' == type:
        self.__parse_contract_data(html)
      if 'plafond' == type:
        self.__parse_plafond_data(html)

      #if 'voicemail' == type:
      #  self.__parse_voicemail_data(html)
      #if 'callforward' == type:
      #  self.__parse_callforward_data(html)

  # Credits: http://stackoverflow.com/questions/42950/get-last-day-of-the-month-in-python#13565185
  def __days_in_month(self,any_day):
    next_month = any_day.replace(day=28) + timedelta(days=4)  # this will never fail
    return int((next_month - timedelta(days=next_month.day)).day)

  def __parse_account_data(self,html):
    self.__print_debug('Parse account data')
    self.application_data['account'] = {}
    for regex_name in self.online_pages['account']['regexes']:
      for data in self.online_pages['account']['regexes'][regex_name].findall(html):
        self.application_data['account'][data[0].strip()] = data[1].strip()

    self.__print_debug(self.application_data['account'])

  def __parse_usage_data(self,html):
    self.__print_debug('Parse usage data')
    self.application_data['sms_usage'] = {}
    self.application_data['call_usage'] = {}
    self.application_data['data_usage'] = {}

    for regex_name in self.online_pages['usage']['regexes']:
      #self.__print_debug(self.online_pages['usage']['regexes'][regex_name])
      for data in self.online_pages['usage']['regexes'][regex_name].findall(html):
        #self.__print_debug(data)
        # This regex will produce two matches. First match is current used, second match is max in account
        if 'used' not in self.application_data[regex_name]:
          self.application_data[regex_name]['used'] = int(data)
          if regex_name == 'data_usage':
            self.application_data[regex_name]['used'] = int(self.application_data[regex_name]['used'] * self.__data_unit_factor(self.internetdata_unit_name))
        else:
          self.application_data[regex_name]['total'] = int(data)
          if regex_name == 'data_usage':
            self.application_data[regex_name]['total'] = int(self.application_data[regex_name]['total'] * self.__data_unit_factor(self.internetdata_unit_name))

          self.application_data[regex_name]['free'] = self.application_data[regex_name]['total'] - self.application_data[regex_name]['used']

      self.__print_debug(self.application_data[regex_name])

    now = date.today()
    self.application_data['days_usage']['total'] = self.__days_in_month(now)
    self.application_data['days_usage']['used']  = int(now.day)
    self.application_data['days_usage']['free']  = self.application_data['days_usage']['total'] - self.application_data['days_usage']['used']

    self.__print_debug(self.application_data['days_usage'])

  def __parse_contract_data(self,html):
    self.__print_debug('Parse contract data')
    contract_fields = ['Abonnement','3G internet & sms bundels','Contractsduur','Ingangsdatum eerste contract','PUKcode']
    self.application_data['contract'] = {}
    self.application_data['options'] = {}

    #self.__print_debug(self.online_pages['contract']['regexes'])
    for regex_name in self.online_pages['contract']['regexes']:
      #self.__print_debug(self.online_pages['contract']['regexes'][regex_name])
      for data in self.online_pages['contract']['regexes'][regex_name].findall(html):
        fieldname = data[0].replace('*','').strip()
        if fieldname in contract_fields:
          self.application_data['contract'][fieldname] = data[1].replace('*','').strip()
        elif regex_name == 'mobilenumber':
          self.application_data['contract']['mobilenumber'] = data.strip()
        else:
          self.application_data['options'][fieldname] = data[1].replace('*','').strip()

    self.__print_debug(self.application_data['contract'])
    self.__print_debug(self.application_data['options'])

  def __parse_plafond_data(self,html):
    self.__print_debug('Parse plafond data')
    self.application_data['plafond'] = {}

    #self.__print_debug(self.online_pages['plafond']['regexes'])
    for regex_name in self.online_pages['plafond']['regexes']:
      #self.__print_debug(self.online_pages['plafond']['regexes'][regex_name])
      for data in self.online_pages['plafond']['regexes'][regex_name].findall(html):
        if regex_name == 'data':
          self.application_data['plafond']['limit'] = data.strip()
        elif regex_name == 'excluded':
          self.application_data['plafond']['exclude_nr_' + data[0].strip()] = data[1].strip()

    self.__print_debug(self.application_data['plafond'])

    '''
  def __parse_voicemail_data(self,html):
    match = self.regex_voicemail_active.search(html)
    if match:
      self.application_data['voicemail_active'] = match.group('active') is None or (match.group('active').strip()).lower() != 'niet'

    match = self.regex_voicemail_pin.search(html)
    self.application_data['voicemail_pin'] = ''
    if match and match.group('pincode') is not None:
      self.application_data['voicemail_pin'] = match.group('pincode')

    match = self.regex_voicemail_email.search(html)
    self.application_data['voicemail_email'] = ''
    if match and match.group('voicemailemail') is not None:
      self.application_data['voicemail_email'] = match.group('voicemailemail')

  def __parse_callforward_data(self,html):
    match = self.regex_callforward_direct.search(html)
    self.application_data['callforward_direct'] = ''
    if match:
      self.application_data['callforward_direct'] = match.group('direct')

    match = self.regex_callforward_busy.search(html)
    self.application_data['callforward_busy'] = ''
    if match:
      self.application_data['callforward_busy'] = match.group('busy')

    self.application_data['callforward_active'] = ( self.application_data['callforward_direct'] != '' or \
                                                    self.application_data['callforward_busy'] != '')


  def __set_voicemail_active(self,active):
    self.application_data['voicemail_active'] = active in [True,1,'True','true','on','On']

  def __set_voicemail_pin(self,pin):
    if re.match('^[0-9]{4}$',str(pin)):
      self.application_data['voicemail_pin'] = pin

  def __set_voicemail_email(self,email):
    if self.valid_email_regex.match(email):
      self.application_data['voicemail_email'] = email

  def __set_callforward_direct(self,direct):
    if direct is not None:
      self.application_data['callforward_direct'] = direct

  def __set_callforward_busy(self,busy):
    if busy is not None:
      self.application_data['callforward_busy'] = busy
'''

  def __data_unit_factor(self,unit):
    if 'MB' == unit:
      return math.pow(self.internetdata_unit_factor,2)
    elif 'GB' == unit:
      return math.pow(self.internetdata_unit_factor,3)

    return float(self.internetdata_unit_factor)


  # Public functions starts here
  def set_username(self,username):
    if username is not None and username != '':
      self.application_data['username'] = username
      self.__save_application_data()

  def set_password(self,password):
    if password is not None and password != '':
      self.application_data['password'] = password
      self.__save_application_data()

  def set_data_update_timeout(self,timeout):
    if timeout is not None and timeout != '' and int(timeout) >= 2 and int(timeout) <= 24:
      self.application_data['data_update_timeout'] = int(timeout) * 3600
      self.__save_application_data()
      return True
    else:
      return False

  def set_credentials(self,username,password):
    self.set_username(username)
    self.set_password(password)
    return self.login()

  def get_username(self):
    return self.application_data['username']

  def get_password(self):
    return self.application_data['password']

  def login(self):
    self.__print_debug('Start login')
    self.login_ok = False

    if self.application_data['username'] is None or self.application_data['password'] is None:
      self.__print_debug('Login methode missing credentials')
      return False

    self.__init_online_session()

    login_data = {'action': 'login',
                  'txtLoginName': self.application_data['username'],
                  'hdnLoginWW': self.application_data['password'] }

    html = self.__process_online_data('login',login_data)
    if MOCKDATA:
      html = MockData.getpage('logincheck')

    #self.__print_debug('HTML Code after login:')
    #self.__print_debug(html)

    self.login_ok = self.online_pages['login']['regexes']['login_check'].search(html)
    if self.login_ok:
      self.application_data['loggedinname'] = self.login_ok.group('loginname')
      self.__print_debug('Login successfull!! Username: ' + self.application_data['loggedinname'])
      self.login_ok = True

    return self.isLoggedIn()

  def isLoggedIn(self):
    return True == self.login_ok

  def get_account_data(self,force_update = False):
    self.__get_online_data(force_update = force_update)

    return_data = {}
    for item in self.application_data.keys():
      if 'voicemail_' not in item and 'callforward_' not in item:
        return_data[item] = self.application_data[item]

    return return_data


  '''def get_voicemail_data(self,force_update = False):
    self.__get_online_data(force_update = force_update)

    return_data = {}
    for item in self.application_data.keys():
      if 'voicemail_' in item:
        return_data[item] = self.application_data[item]

    return_data['last_update'] = self.application_data['last_update']
    return return_data

  def get_callforward_data(self,force_update = False):
    self.__get_online_data(force_update = force_update)

    return_data = {}
    for item in self.application_data.keys():
      if 'callforward_' in item:
        return_data[item] = self.application_data[item]

    return_data['last_update'] = self.application_data['last_update']
    return return_data'''

  def get_all_data(self,force_update = False):
    self.__get_online_data(force_update = force_update)
    return self.application_data


  '''def set_voicemail_settings(self, active = None, pin = None, email = None):
    self.__set_voicemail_active(active)
    self.__set_voicemail_pin(pin)
    self.__set_voicemail_email(email)

    post_data = {'action': 'vmsettings',
                 'vmpin': self.application_data['voicemail_pin'],
                 'vmemail': self.application_data['voicemail_email'] }

    if self.application_data['voicemail_active'] is True:
      post_data['vmactive'] = 'on'

    self.__get_online_data('voicemail',post_data)
    return True

  def set_callforward_settings(self, direct = None, busy = None):
    self.__set_callforward_direct(direct)
    self.__set_callforward_busy(busy)

    post_data = {'action': 'cfsettings',
                 'cfim': self.application_data['callforward_direct'],
                 'cfbs': self.application_data['callforward_busy'] }

    self.__get_online_data('callforward',post_data)
    return True'''

  def get_history(self,month = None,year = None):
    self.__print_debug('Get history data')

    # Create tempory history data array based on days
    history_data = {}

    for history_update_date in self.history_data:
      # Copy of the data
      data = self.history_data[history_update_date]
      data['last_update'] = int(history_update_date)

      # Create date index in format 20151121
      history_update_date = datetime.fromtimestamp(int(history_update_date)).strftime('%Y%m%d')

      if history_update_date not in history_data or history_data[history_update_date]['last_update'] < data['last_update']:
        history_data[history_update_date] = data

    self.__print_debug(history_data)
    return history_data

  def reset_settings(self, save = True):
    self.application_data = {
        'last_update': 0,
        'data_update_timeout': int(4 * 3600),
        'username': None,
        'password': None,

        'account' : {},
        'contract' : {},
        'options' : {},
        'plafond' : {},

        'sms_usage':  {'total': None, 'used': None, 'free': None},
        'call_usage': {'total': None, 'used': None, 'free': None},
        'data_usage': {'total': None, 'used': None, 'free': None},
        'days_usage': {'total': None, 'used': None, 'free': None},
    }
    self.history_data = {}

    if save:
      self.__save_application_data()
      self.__save_application_history()

    return True

scraper = SimpelScraper()
