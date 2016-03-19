#!/usr/bin/env python3
# -*- coding: utf-8 -*-

VERSION = '0.2'
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
import platform
from datetime import date, datetime, timedelta
from collections import OrderedDict

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
    #self.form_elements_regex = re.compile('<input .*name="(?P<name>[^"]+)"(.*value="(?P<value>[^"]*)")?[^>]+>')
    self.form_elements_regex = re.compile('<input[^>]+name="(?P<name>[^"]+)([^>]+)>')

    # Generic email regex
    self.valid_email_regex  = re.compile("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$")

    # Use 1000 bytes factor for data useage
    self.internetdata_unit_factor = 1000
    self.internetdata_unit_name = 'MB'

    # Online pages with the data for scraping
    self.login_cookie = None
    self.portal_url   = 'https://www.mijnsimpel.nl'

    # Maintain order for first run...
    self.online_pages = OrderedDict()

    # Login data
    self.online_pages['login'] = {'urlpath' : 'login.aspx' ,
                                  'regexes' : { 'login_detect' : re.compile('<h1>Inloggen op Mijn Simpel</h1>'),
                                                'login_check'  : re.compile('<p>Welkom\s*<strong>\s*(?P<loginname>[^<]+)\s*</strong>,</p>')
                                              }
                                  }
    # Usage data
    self.online_pages['usage'] = {'urlpath' : 'credit.aspx' ,
                                  'regexes' : { 'call_usage' : re.compile('(\d+) minuten'),
                                                'sms_usage'  : re.compile('(\d+) SMS'),
                                                'data_usage' : re.compile('(\d+) ' + self.internetdata_unit_name)
                                                }
                                    }
    # Plafond data
    self.online_pages['plafond'] = {'urlpath' : 'belplafond.aspx' ,
                                    'regexes' : { 'data' : re.compile('<tr><td[^>]*>Plafond<\/td><td[^>]*><span[^>]*>(?P<plafond>. \d+,\d{0,2})'),
                                                  'excluded': re.compile('<tr><td[^>]*>Telefoonnummer\s*(?P<counter>\d).*<input[^>]*name="(?P<field>[^"]*)"[^>]*value="(?P<value>[^"]*)"[^>]*>')
                                                }
                                    }

    # Account data
    self.online_pages['contract'] = {'urlpath' : 'simproperties.aspx' ,
                                    'regexes' : { 'data' : re.compile('<tr><td[^>]*>([^<]+)<\/td><td[^>]*>([^<]+)<\/td>'),
                                                  'mobilenumber': re.compile('Mijn Simpel voor (?P<mobile>\d{10})')
                                                }
                                    }

    # Account data
    self.online_pages['account'] = {'urlpath' : 'account.aspx' ,
                                    'regexes' : { 'data' : re.compile('<tr><td[^>]*>([^<]+)<\/td><td[^>]*>([^<]+)<\/td>')
                                                }
                                    }

    self.online_pages['options'] = {'urlpath' : 'simproperties_edit.aspx' ,
                                    'regexes' : { 'data'    : re.compile('<tr><td[^>]+>(?P<label>[^<]+)<\/td><td[^>]*><span[^>]*><select name="(?P<field>[^"]+)"[^>]*>(?P<options>.*?)<\/select>'),
                                                  'options' : re.compile('<option(?P<selected> selected="selected" | )?value="(?P<optionvalue>[^"]+)">(?P<optionname>[^>]+)<\/option>')
                                                }
                                    }

    self.__load_application_data()

    self.__history_fields = {'data_update_timeout', 'sms_usage','call_usage','data_usage','days_usage'}
    self.__load_application_history()

    self.__print_debug('Loaded app')
    self.__print_debug(self.application_data)

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

    self.opener.addheaders = [('User-agent', 'SimpelStatusScraper v.' + VERSION + ' on ' + platform.release())]
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
        if page == 'login' or page == 'options':
          continue

        self.__parse_data(page,self.__process_online_data(page,data))

      self.application_data['last_update'] = int(time.time())
      self.__add_history();
      self.__save_application_data()

  def __process_dotNet_form_fields(self,html):
    value_regex = re.compile('value="(?P<value>[^"]+)"')
    elements = {}
    # Get the form fields with keys
    for element in self.form_elements_regex.findall(html):
      elements[element[0]] = ''
      for value in value_regex.findall(element[1]):
        elements[element[0]] = value

    # Get the Javascript postback values
    elements_regex = re.compile('javascript:__doPostBack\(\'(?P<target>[^\']+)\',\'(?P<argument>[^\']*)\'\)')
    elements_data = elements_regex.findall(html)
    if elements_data:
      for element in elements_data:
        elements['__EVENTTARGET'] = element[0]
        elements['__EVENTARGUMENT'] = element[1]

    self.__print_debug('Return .Net Form elements')
    self.__print_debug(elements)
    return elements

  def __process_online_data(self,page,data = None):
    self.__print_debug('Process online data for page: ' + page)
    if page not in self.online_pages:
      self.__print_debug('Process online data for page ' + page + ' failed due it is not known by the app')
      return None

    html = ''
    post_data = None

    if data is not None:
      self.__print_debug('Processing post data for page: ' + page)
      self.__print_debug(data)

      self.__print_debug('Parsing dotNet form fields for page: ' + page)
      dotNetData = self.__process_dotNet_form_fields(self.__process_online_data(page))
      newdata = {}

      for originalfield in data:
        for dotNetfield in dotNetData:
          if dotNetfield.startswith('__'):
            newdata[dotNetfield] = dotNetData[dotNetfield]
          if originalfield in dotNetfield:
            newdata[dotNetfield] = data[originalfield]

      self.__print_debug('Finale post data for page: ' + page)
      self.__print_debug(newdata.copy())
      post_data = urllib.parse.urlencode(newdata.copy()).encode('utf-8')

    if MOCKDATA:
      self.__print_debug('Using MOCK Data for page ' + page)
      if post_data is not None:
        self.__print_debug('Using Postdata')
        self.__print_debug(post_data)

      html = MockData.getpage(page)
      # Using MOCK Data, login will always succeed.... :(
      if 'login' == page and data is not None:
        html = MockData.getpage('logincheck')
    else:
      response = self.opener.open(self.portal_url + '/' + self.online_pages[page]['urlpath'],post_data)
      html = response.read().decode('utf-8')

    # Moet nog worden uitgezocht.... hangt van de cookies en sessies af
    if page != 'login' and self.online_pages['login']['regexes']['login_detect'].search(html) is not None:
      #self.login_detect_regex.search(html):
      self.__notify_message('notification','Cookie expired, relogin for page' + page)
      if self.login():
        self.__print_debug('Recursive restart processing online data')
        html = self.__process_online_data(page,data)

    # Some cleaning up
    html = html.replace('\n','')
    html = re.sub('\s+', ' ', html)
    html = re.sub('>\s+<', '><', html)
    #self.__print_debug('Return HTML for page: ' + page + '\n' + html)
    return html.strip()

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
      if 'options' == type:
        self.__parse_options_data(html)

  # Credits: http://stackoverflow.com/questions/42950/get-last-day-of-the-month-in-python#13565185
  def __days_in_month(self,any_day):
    next_month = any_day.replace(day=28) + timedelta(days=4)  # this will never fail
    return int((next_month - timedelta(days=next_month.day)).day)

  def __parse_account_data(self,html):
    self.__print_debug('Parse account data')
    self.application_data['account'] = {}
    for regex_name in self.online_pages['account']['regexes']:
      for data in self.online_pages['account']['regexes'][regex_name].findall(html):
        self.application_data['account'][str(len(self.application_data['account'])) + '_' + data[0].strip()] = data[1].strip()

    self.__print_debug(self.application_data['account'])

  def __parse_usage_data(self,html):
    self.__print_debug('Parse usage data')
    self.application_data['sms_usage'] = {}
    self.application_data['call_usage'] = {}
    self.application_data['data_usage'] = {}

    for regex_name in self.online_pages['usage']['regexes']:
      for data in self.online_pages['usage']['regexes'][regex_name].findall(html):
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

    for regex_name in self.online_pages['contract']['regexes']:
      for data in self.online_pages['contract']['regexes'][regex_name].findall(html):
        fieldname = data[0].replace('*','').strip()
        if fieldname in contract_fields:
          self.application_data['contract'][str(len(self.application_data['contract'])) + '_' + fieldname] = data[1].replace('*','').strip()
        elif regex_name == 'mobilenumber':
          self.application_data['contract']['mobilenumber'] = data.strip()
        else:
          self.application_data['options'][str(len(self.application_data['options'])) + '_' + fieldname] = { 'id': None, 'current' : data[1].replace('*','').strip(), 'options' : None }

    self.__print_debug(self.application_data['contract'])
    self.__print_debug(self.application_data['options'])

  def __parse_options_data(self,html):
    self.__print_debug('Parse options data')
    self.application_data['options'] = {}

    for data in self.online_pages['options']['regexes']['data'].findall(html):
      fieldname = str(len(self.application_data['options']))  + '_' + data[0].replace('*','').strip()
      self.application_data['options'][fieldname] = { 'id': data[1], 'current' : '', 'options' : [] }
      # Parse the options data
      for options in self.online_pages['options']['regexes']['options'].findall(data[2]):
        if options[0].strip() != '':
          self.application_data['options'][fieldname]['current'] = options[2]
        self.application_data['options'][fieldname]['options'].append({'label':options[2],'value':options[1]})

      self.__print_debug(self.application_data['options'])

  def __parse_plafond_data(self,html):
    self.__print_debug('Parse plafond data')
    self.application_data['plafond'] = {}

    for regex_name in self.online_pages['plafond']['regexes']:
      for data in self.online_pages['plafond']['regexes'][regex_name].findall(html):
        if regex_name == 'data':
          self.application_data['plafond']['limit'] = data.strip()
        elif regex_name == 'excluded':
          self.application_data['plafond']['exclude_nr_' + data[0].strip()] = data[1].strip()

    self.__print_debug(self.application_data['plafond'])

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

  def set_credentials(self,username,password,loadinfo = False):
    self.set_username(username)
    self.set_password(password)
    return self.login(loadinfo)

  def get_username(self):
    return self.application_data['username']

  def get_password(self):
    return self.application_data['password']

  def login(self,loadinfo = False):
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

    self.login_ok = self.online_pages['login']['regexes']['login_check'].search(html)
    if self.login_ok:
      self.application_data['loggedinname'] = self.login_ok.group('loginname')
      self.__print_debug('Login successfull!! Username: ' + self.application_data['loggedinname'])
      if loadinfo:
        self.__get_online_data()

      self.login_ok = True

    return self.isLoggedIn()

  def isLoggedIn(self):
    return True == self.login_ok

  def __get_info(self,type):
    data = []
    for key in sorted(self.application_data[type]):
      data.append({'label':re.sub(r"^\d+_", "", key), 'value':self.application_data[type][key] })

    self.__print_debug(data)
    return data

  def get_account_info(self):
    return self.__get_info('account')

  def get_contract_info(self):
    return self.__get_info('contract')

  def get_mobile_options(self,edit = False):
    if edit:
      # Load .Net FORM data
      html = self.__process_online_data('options')
      self.__parse_data('options',html)

    data = self.__get_info('options')

    for key in data:
      self.__print_debug('Before mobile option data')
      self.__print_debug(key)
      if edit:
        key['options'] = key['value']['options']
        key['id'] = key['value']['id']

      key['value'] = key['value']['current']

      self.__print_debug('After mobile option data')
      self.__print_debug(key)

    return data

  def get_all_data(self,force_update = False):
    self.__get_online_data(force_update = force_update)
    return self.application_data

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
    self.login_ok = False
    self.history_data = {}

    if save:
      self.__save_application_data()
      self.__save_application_history()

    return True

scraper = SimpelScraper()
