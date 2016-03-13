#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from random import randint

def random(max):
  return int((randint(1, 200) / 100) * max)

def getpage(page):
  # Fake HTTP traffic duration for testing animation
  time.sleep(randint(2, 6))
  if 'login' == page:
    return data_login
  if 'logincheck' == page:
    return data_login_check
  if 'account' == page:
    return data_account
  if 'usage' == page:
    return data_usage
  if 'contract' == page:
    return data_contract
  if 'plafond' == page:
    return data_plafond
  if 'options' == page:
    return data_options.replace('\n','')

# Mock Data

data_options = """

<!DOCTYPE html>

<html>
<head><meta charset="utf-8" /><meta http-equiv="X-UA-Compatible" content="IE-edge,chrome=1" /><title>
        Mijn Simpel
</title><link href="/resources/css/defaults.css?v=002" rel="stylesheet" type="text/css" /><link href="/resources/css/master.css?v=002" rel="stylesheet" type="text/css" /><link href="/resources/css/cookiechecker.css?v=002" rel="stylesheet" type="text/css" />
    <!--[if lte IE 8]>
   <link href="/resources/css/cookiecheckerIE.css?v=002" rel="stylesheet" type="text/css" />
    <![endif]-->

    <script src="/resources/js/jquery-1.7.2.min.js" type="text/javascript"></script>
    <script src="/resources/js/jquery-ui-1.8.7.custom.min.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.corner.js" type="text/javascript"></script>
    <script src="/resources/js/prototypes.js" type="text/javascript"></script>
    <script src="/resources/js/validatie.js?v=003" type="text/javascript"></script>
    <script src="/resources/js/tooltip.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.tools.min.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.ui.datepicker-nl.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.reveal.cookie.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.reveal.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.reveal.contact.js" type="text/javascript"></script>
    <script src="/resources/js/cookiechecker.js" type="text/javascript"></script>
    <script src="/resources/js/checkiban.js" type="text/javascript"></script>

    <!-- Google Analyticsscript -->
    <script>(function (i, s, o, g, r, a, m) { i['GoogleAnalyticsObject'] = r; i[r] = i[r] || function () { (i[r].q = i[r].q || []).push(arguments) }, i[r].l = 1 * new Date(); a = s.createElement(o), m = s.getElementsByTagName(o)[0]; a.async = 1; a.src = g; m.parentNode.insertBefore(a, m) })(window, document, 'script', '//www.google-analytics.com/analytics.js', 'ga'); ga('create', 'UA-1956252-1', 'simpel.nl'); ga('send', 'pageview');</script>
    <!-- End Google Analyticsscript -->

    <script type="text/javascript">
        //<![CDATA[
        $(document).ready(function () {

                        $("form1").submit(function () {
                $(this).submit(function () {
                    return false;
                });
                return true;
            });


            doTooltip('.tooltiptarget');

            $(".tooltiptargetlink").tooltip({ position: 'left top', offset: [45, -15], effect: 'fade' });

            ValidateInitialize('select, input[type=checkbox], input[type=password], input[type=text]');
            $('.submit').bind('click', function (event) {
                if (!doValidateAll('select, input[type=checkbox], input[type=password], input[type=text]')) {
                    event.preventDefault();
                }
            });


            $('img#simpellogo').bind('click', function (event) {
                window.location.href = '/';
                event.preventDefault();
            });

            $('div.content').corner('10px');
            $('a.button').corner('5px');
            if ($.browser.msie && $.browser.version < 9) {
                $('.menu .selected').corner('4px');
            } else {
                $('.menu span, .menu li a').corner('4px');
            }

            $('.login').corner('5px bottom');

            $('table.classictable').each(function () {
                $(this).find('tr:even').addClass('alt');
            });
        });

        function getCookie(c_name) {
            var i, x, y, ARRcookies = document.cookie.split(";");
            for (i = 0; i < ARRcookies.length; i++) {
                x = ARRcookies[i].substr(0, ARRcookies[i].indexOf("="));
                y = ARRcookies[i].substr(ARRcookies[i].indexOf("=") + 1);
                x = x.replace(/^\s+|\s+$/g, "");
                if (x == c_name) {
                    return unescape(y);
                }
            }
        }

        //]]>
    </script>

    <script type="text/javascript">
        //<![CDATA[
        $(document).ready(function(){
             message('#error', 3, false, '', '');
             $('#simproperties').addClass('selected');


             $('tr.greyedout input[type=checkbox]').bind('change', function(){
                if($(this).attr('checked')){
                    $('tr.greyedout input[type=text], tr.greyedout input[type=password], tr.greyedout textarea').attr('disabled', '').parent('span').removeClass('disabled');;
                } else {
                    $('tr.greyedout input[type=text], tr.greyedout input[type=password], tr.greyedout textarea').val('0,00').attr('disabled', 'disabled').parent('span').addClass('disabled');

                }
             }).trigger('change');
        });
        //]]>
    </script>

    <!--[if IE 7]>
    <link rel="stylesheet" type="text/css" href="/static/css/IE7.css" />
    <style type="text/css">
        .showpassword {float:right; !important; margin-top:-20px;}
        .showpassword2 {witdh:220px;}
        span.formfield
        {
                background-color: #ededee;
                padding: 0px 0px 0px 0px;
                margin:0px 0px 0px 3px;
                background: transparent url(/resources/img/bg/forms/input_right.png) no-repeat top right;
                display: inline-block;
                width:405px !important;
        }

    </style>
    <![endif]-->
    <!--[if lt IE 8]>
        <style type="text/css">
            span.formfield{
                 background-position: right 1px !important;
            }

            span.formfield select{
                background-color: #ededee;
            }


        </style>
    <![endif]-->
    <!--[if IE 8]>
        <style type="text/css">
            span.formfield input[type="text"], span.formfield input[type="password"], span.formfield select{
                 font-size:17px !important;
            }
        </style>
    <![endif]-->

</head>
<body>
    <form name="aspnetForm" method="post" action="simproperties_edit.aspx" id="aspnetForm">
<div>
<input type="hidden" name="__EVENTTARGET" id="__EVENTTARGET" value="" />
<input type="hidden" name="__EVENTARGUMENT" id="__EVENTARGUMENT" value="" />
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwULLTE1Mjk4MzQzODQPZBYCZg9kFgICAw9kFgYCAQ8WAh4EVGV4dAXeATxkaXYgY2xhc3M9Im1lbnUiPjxzcGFuIGlkPSJtZW51X3RhcmlldmVuIj48YSBocmVmPSJodHRwOi8vd3d3LnNpbXBlbC5ubC9UYXJpZXZlbi5hc3B4IiB0YXJnZXQ9Il9ibGFuayI+dGFyaWV2ZW48L2E+PC9zcGFuPjxzcGFuIGlkPSJtZW51X2ZhcSI+PGEgaHJlZj0iaHR0cDovL3d3dy5zaW1wZWwubmwvZmFxLmFzcHgiIHRhcmdldD0iX2JsYW5rIj52cmFnZW48L2E+PC9zcGFuPjwvZGl2PmQCBQ8WAh8ABb8GPHVsIGNsYXNzPSJtZW51Ij48bGk+PGEgaWQ9ImhvbWUiIGhyZWY9Ii9sYW5kaW5nLmFzcHgiPmhvbWU8L2E+PC9saT48bGk+PGEgaWQ9ImFjY291bnQiIGhyZWY9Ii9hY2NvdW50LmFzcHgiPm1pam4gZ2VnZXZlbnM8L2E+PC9saT48bGk+PGEgaWQ9InNpbXByb3BlcnRpZXMiIGhyZWY9Ii9zaW1wcm9wZXJ0aWVzLmFzcHgiPmdlZ2V2ZW5zIGFib25uZW1lbnQ8L2E+PC9saT48bGk+PGEgaWQ9InVwZ3JhZGUiIGhyZWY9Ii91cGdyYWRlLmFzcHgiPndpanppZyBhYm9ubmVtZW50PC9hPjwvbGk+PGxpPjxhIGlkPSJiZWxwbGFmb25kIiBocmVmPSIvYmVscGxhZm9uZC5hc3B4Ij5wbGFmb25kPC9hPjwvbGk+PGxpPjxhIGlkPSJpbnZvaWNlcyIgaHJlZj0iL2ludm9pY2VzLmFzcHgiPmZhY3R1cmVuPC9hPjwvbGk+PGxpPjxhIGlkPSJjYWxsX2RldGFpbHMiIGhyZWY9Ii9yZXF1ZXN0X3NwZWNpZmljYXRpb25zLmFzcHgiPmJlbHNwZWNpZmljYXRpZTwvYT48L2xpPjxsaT48YSBpZD0iY3JlZGl0IiBocmVmPSIvY3JlZGl0LmFzcHgiPmFjdHVlZWwgdmVyYnJ1aWs8L2E+PC9saT48bGk+PGEgaWQ9ImNoYW5nZV9wYXNzd29yZCIgaHJlZj0iL3Bhc3N3b3JkX2VkaXQuYXNweCI+d2lqemlnIHdhY2h0d29vcmQ8L2E+PC9saT48bGk+PGEgaWQ9ImJsb2NrIiBocmVmPSIvYmxvY2suYXNweCI+Ymxva2tlZXIgbnVtbWVyPC9hPjwvbGk+PGxpPjxhIGlkPSJzaW1zd2FwIiBocmVmPSIvU2ltU3dhcC5hc3B4Ij52ZXJ2YW5nZW5kZSBTaW1rYWFydDwvYT48L2xpPjxsaT48YSBpZD0iY29udGFjdCIgaHJlZj0iL2NvbnRhY3QuYXNweCI+c3RlbCBqZSB2cmFhZzwvYT48L2xpPjwvdWw+ZAIHD2QWAgIDDxYCHwAFCjA2MjM0MjI0OTFkZAQwGRFC36voTwXcfMNVWViC1zGA" />
</div>

<script type="text/javascript">
//<![CDATA[
var theForm = document.forms['aspnetForm'];
if (!theForm) {
    theForm = document.aspnetForm;
}
function __doPostBack(eventTarget, eventArgument) {
    if (!theForm.onsubmit || (theForm.onsubmit() != false)) {
        theForm.__EVENTTARGET.value = eventTarget;
        theForm.__EVENTARGUMENT.value = eventArgument;
        theForm.submit();
    }
}
//]]>
</script>


<div>

        <input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="0C43016F" />
        <input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="/wEWFQLjwMqeAQLy5rPuDALt5rPuDALoser3CwL3ser3CwL4ser3CwLnser3CwL4ser3CwL7ser3CwLlser3CwL6ser3CwL6ser3CwL7ser3CwLkser3CwL4ser3CwLjser3CwL8ser3CwL9ser3CwLiser3CwKPg92dCwLHjbmPCxihlcVOYLsCqIGCfSeNpEOf9u6g" />
</div>
    <div class="container">
                <div class="header">
                        <img src="/resources/img/logo/simpellogo.png" alt="simpel" id="simpellogo" />
                        <div class="menu"><span id="menu_tarieven"><a href="http://www.simpel.nl/Tarieven.aspx" target="_blank">tarieven</a></span><span id="menu_faq"><a href="http://www.simpel.nl/faq.aspx" target="_blank">vragen</a></span></div>
                </div>

        <div class="contentcontainer">
            <div class="content errorbox" id="error">
                <div class="errorcontent">
                </div>
                <a href="#" class="close">x</a>
            </div>
            <div class="content" id="content">
                <div class="menucontainer">


                    <ul class="menu"><li><a id="home" href="/landing.aspx">home</a></li><li><a id="account" href="/account.aspx">mijn gegevens</a></li><li><a id="simproperties" href="/simproperties.aspx">gegevens abonnement</a></li><li><a id="upgrade" href="/upgrade.aspx">wijzig abonnement</a></li><li><a id="belplafond" href="/belplafond.aspx">plafond</a></li><li><a id="invoices" href="/invoices.aspx">facturen</a></li><li><a id="call_details" href="/request_specifications.aspx">belspecificatie</a></li><li><a id="credit" href="/credit.aspx">actueel verbruik</a></li><li><a id="change_password" href="/password_edit.aspx">wijzig wachtwoord</a></li><li><a id="block" href="/block.aspx">blokkeer nummer</a></li><li><a id="simswap" href="/SimSwap.aspx">vervangende Simkaart</a></li><li><a id="contact" href="/contact.aspx">stel je vraag</a></li></ul>
                </div>

    <h1>Bewerk gegevens van mobielnummer: 0623422491</h1>


    <h3>Diensten</h3>
    <table>
        <div id="ctl00_content_panOptions">

        </span></td><tr><td class="td0">Nummerweergave op specificatie</td><td class="td1" colspan="3"><span class="formfield"><select name="ctl00$content$ddlOption0" id="ctl00_content_ddlOption0" value="5" validation="select">
                <option selected="selected" value="1">Nummerweergave op specificaties afgeschermd</option>
                <option value="0">Nummerweergave op specificaties niet afgeschermd</option>

        </select></span></td></tr>
</div>
    </table>
    <table>
        <div id="ctl00_content_panServices">

        <tr><td class="td0">SMS</td><td class="td1" colspan="3"><span class="formfield"><select name="ctl00$content$ddlService0" id="ctl00_content_ddlService0" validation="select" value="1">
                <option value="0">SMS versturen geblokkeerd</option>
                <option selected="selected" value="1">SMS versturen toegestaan</option>

        </select></span></td><td class="td4" style="text-align:right;"><img style="border-width: 0px;" src="/resources/img/misc/tooltip.png" title="Als je kiest voor SMS toestaan, betekent dit dat je SMS-berichten kunt versturen vanaf je mobiele telefoon. SMS versturen geblokkeerd betekent dat je geen SMS-berichten kunt versturen vanaf je mobiele telefoon. Welke instelling je ook kiest, je kunt wel SMS-berichten ontvangen." class="tooltiptarget"></td></tr><tr><td class="td0">MMS</td><td class="td1" colspan="3"><span class="formfield"><select name="ctl00$content$ddlService1" id="ctl00_content_ddlService1" validation="select" value="2">
                <option value="1">MMS versturen toegestaan</option>
                <option selected="selected" value="0">MMS versturen niet toegestaan</option>

        </select></span></td><td class="td4" style="text-align:right;"><img style="border-width: 0px;" src="/resources/img/misc/tooltip.png" title="Als je kiest voor MMS versturen toestaan, betekent dit dat je MMS-berichten kunt versturen vanaf je mobiele telefoon. MMS versturen niet toestaan betekent dat je geen MMS-berichten kunt versturen vanaf je mobiele telefoon. Welke instelling je ook kiest, je kunt wel MMS-berichten ontvangen. LET OP: Je hebt voor het ontvangen en versturen van MMS-berichten, aparte instellingen nodig op je mobiele telefoon." class="tooltiptarget"></td></tr><tr><td class="td0">0900 entertainment</td><td class="td1" colspan="3"><span class="formfield"><select name="ctl00$content$ddlService2" id="ctl00_content_ddlService2" validation="select" value="3">
                <option selected="selected" value="2">0900 entertainment bellen geblokkeerd</option>

        </select></span></td><td class="td4" style="text-align:right;"><img style="border-width: 0px;" src="/resources/img/misc/tooltip.png" title="Als je kiest voor 0900 entertainment toegestaan, dan kun je gebruik maken van 0900 entertainment nummers. Deze optie komt beschikbaar wanneer je in totaal 3 facturen hebt voldaan. Let op: het verbruik van 0900 entertainment nummers valt buiten je bundel." class="tooltiptarget"></td></tr><tr><td class="td0">Inkomende gesprekken</td><td class="td1" colspan="3"><span class="formfield"><select name="ctl00$content$ddlService3" id="ctl00_content_ddlService3" validation="select" value="4">
                <option value="2">Alleen inkomende gesprekken in het buitenland geblokkeerd</option>
                <option selected="selected" value="0">Geen blokkade op inkomende gesprekken</option>
                <option value="1">Alle inkomende gesprekken geblokkeerd</option>

        </select></span></td><td class="td4" style="text-align:right;"><img style="border-width: 0px;" src="/resources/img/misc/tooltip.png" title="Als je kiest voor alle inkomende gesprekken geblokkeerd kun je niet meer gebeld worden. Als je kiest voor alleen inkomende gesprekken in het buitenland geblokkeerd kun je niet meer gebeld worden in het buitenland. Als je geen blokkade op inkomende gesprekken kiest kun je in binnen- en buitenland gebeld worden. Welke instelling je ook kiest, je kunt wel SMS-berichten ontvangen." class="tooltiptarget"></td></tr><tr><td class="td0">Uitgaande gesprekken</td><td class="td1" colspan="3"><span class="formfield"><select name="ctl00$content$ddlService4" id="ctl00_content_ddlService4" validation="select" value="5">
                <option value="2">Bellen naar het buitenland geblokkeerd</option>
                <option value="1">Alle uitgaande gesprekken geblokkeerd</option>
                <option selected="selected" value="0">Geen blokkade op uitgaande gesprekken</option>
                <option value="4">Bellen in het buitenland geblokkeerd</option>

        </select></span></td><td class="td4" style="text-align:right;"><img style="border-width: 0px;" src="/resources/img/misc/tooltip.png" title="Als je kiest voor alle uitgaande gesprekken geblokkeerd kun je niet meer bellen. Als je bellen in het buitenland geblokkeerd kiest kun je niet meer bellen in het buitenland. Als je bellen naar het buitenland geblokkeerd kiest kun je niet meer vanuit Nederland naar het buitenland bellen. Als je kiest voor geen blokkade op uitgaande gesprekken dan kun je in binnen en buitenland blijven bellen. Welke instelling je ook kiest, je kunt wel SMS-berichten ontvangen." class="tooltiptarget"></td></tr><tr><td class="td0">Buitenlandgebruik</td><td class="td1" colspan="3"><span class="formfield"><select name="ctl00$content$ddlService5" id="ctl00_content_ddlService5" validation="select" value="7">
                <option selected="selected" value="0">Geen blokkade in het buitenland</option>
                <option value="1">Toestel in het buitenland geblokkeerd</option>

        </select></span></td><td class="td4" style="text-align:right;"><img style="border-width: 0px;" src="/resources/img/misc/tooltip.png" title="Als je kiest voor toestel in het buitenland geblokkeerd kun je in het buitenland niet bellen of gebeld worden, SMSen en mobiel internetten." class="tooltiptarget"></td></tr><tr><td class="td0">Betaalde SMS diensten</td><td class="td1" colspan="3"><span class="formfield"><select name="ctl00$content$ddlService6" id="ctl00_content_ddlService6" validation="select" value="8">
                <option selected="selected" value="1">Betaalde SMS diensten niet toegestaan</option>
                <option value="0">Betaalde SMS diensten toegestaan</option>

        </select></span></td><td class="td4" style="text-align:right;"><img style="border-width: 0px;" src="/resources/img/misc/tooltip.png" title="Als je kiest voor het toestaan van betaalde SMS diensten is het mogelijk om betaalde sms diensten te ontvangen." class="tooltiptarget"></td></tr>
</div>
    </table>
    <a id="ctl00_content_lbSubmit" class="button submit" href="javascript:__doPostBack('ctl00$content$lbSubmit','')">Wijzig</a>

            </div>




            <div class="clear"></div>


             <div class="footer">
                            <span><a href="http://www.simpel.nl/contact.aspx" target="_blank">contact</a></span><span><a href="http://www.simpel.nl/privacyverklaring.aspx" target="_blank">privacyverklaring</a></span><span><a href="http://www.simpel.nl/Voorwaarden.aspx" target="_blank">voorwaarden</a></span>
                    </div>
                    <a id="ctl00_lbLogOut" class="login" href="javascript:__doPostBack('ctl00$lbLogOut','')">uitloggen</a>
        </div>
    </div>
    </form>
</body>
</html>
"""

data_plafond = """

<!DOCTYPE html>

<html>
<head><meta charset="utf-8" /><meta http-equiv="X-UA-Compatible" content="IE-edge,chrome=1" /><title>
        Mijn Simpel
</title><link href="/resources/css/defaults.css?v=002" rel="stylesheet" type="text/css" /><link href="/resources/css/master.css?v=002" rel="stylesheet" type="text/css" /><link href="/resources/css/cookiechecker.css?v=002" rel="stylesheet" type="text/css" />
    <!--[if lte IE 8]>
   <link href="/resources/css/cookiecheckerIE.css?v=002" rel="stylesheet" type="text/css" />
    <![endif]-->

    <script src="/resources/js/jquery-1.7.2.min.js" type="text/javascript"></script>
    <script src="/resources/js/jquery-ui-1.8.7.custom.min.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.corner.js" type="text/javascript"></script>
    <script src="/resources/js/prototypes.js" type="text/javascript"></script>
    <script src="/resources/js/validatie.js?v=003" type="text/javascript"></script>
    <script src="/resources/js/tooltip.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.tools.min.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.ui.datepicker-nl.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.reveal.cookie.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.reveal.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.reveal.contact.js" type="text/javascript"></script>
    <script src="/resources/js/cookiechecker.js" type="text/javascript"></script>
    <script src="/resources/js/checkiban.js" type="text/javascript"></script>

    <!-- Google Analyticsscript -->
    <script>(function (i, s, o, g, r, a, m) { i['GoogleAnalyticsObject'] = r; i[r] = i[r] || function () { (i[r].q = i[r].q || []).push(arguments) }, i[r].l = 1 * new Date(); a = s.createElement(o), m = s.getElementsByTagName(o)[0]; a.async = 1; a.src = g; m.parentNode.insertBefore(a, m) })(window, document, 'script', '//www.google-analytics.com/analytics.js', 'ga'); ga('create', 'UA-1956252-1', 'simpel.nl'); ga('send', 'pageview');</script>
    <!-- End Google Analyticsscript -->

    <script type="text/javascript">
        //<![CDATA[
        $(document).ready(function () {

                        $("form1").submit(function () {
                $(this).submit(function () {
                    return false;
                });
                return true;
            });


            doTooltip('.tooltiptarget');

            $(".tooltiptargetlink").tooltip({ position: 'left top', offset: [45, -15], effect: 'fade' });

            ValidateInitialize('select, input[type=checkbox], input[type=password], input[type=text]');
            $('.submit').bind('click', function (event) {
                if (!doValidateAll('select, input[type=checkbox], input[type=password], input[type=text]')) {
                    event.preventDefault();
                }
            });


            $('img#simpellogo').bind('click', function (event) {
                window.location.href = '/';
                event.preventDefault();
            });

            $('div.content').corner('10px');
            $('a.button').corner('5px');
            if ($.browser.msie && $.browser.version < 9) {
                $('.menu .selected').corner('4px');
            } else {
                $('.menu span, .menu li a').corner('4px');
            }

            $('.login').corner('5px bottom');

            $('table.classictable').each(function () {
                $(this).find('tr:even').addClass('alt');
            });
        });

        function getCookie(c_name) {
            var i, x, y, ARRcookies = document.cookie.split(";");
            for (i = 0; i < ARRcookies.length; i++) {
                x = ARRcookies[i].substr(0, ARRcookies[i].indexOf("="));
                y = ARRcookies[i].substr(ARRcookies[i].indexOf("=") + 1);
                x = x.replace(/^\s+|\s+$/g, "");
                if (x == c_name) {
                    return unescape(y);
                }
            }
        }

        //]]>
    </script>

    <script type="text/javascript">
        //<![CDATA[
        $(document).ready(function(){
             message('#error', 3, false, '', '');
             $('#belplafond').addClass('selected');


              //set tooltip for password field
             $('#tooltip1').text('Het nummer dat je hier invult dient te beginnen met 31 (dit is de landencode van Nederland) zoals in dit voorbeeld: 31612345678');
             $('#tooltip2').text('Het nummer dat je hier invult dient te beginnen met 31 (dit is de landencode van Nederland) zoals in dit voorbeeld: 31612345678');
             $('#tooltip3').text('Het nummer dat je hier invult dient te beginnen met 31 (dit is de landencode van Nederland) zoals in dit voorbeeld: 31612345678');

            $('.btn').bind('click', function (event) {
                if (!doValidateAll('select')) {
                    event.preventDefault();
                }
            });
            $('.btn2').bind('click', function (event) {
                if (!doValidateAll('input[type=text], input[type=password]')) {
                    event.preventDefault();
                }
            });
        });
        //]]>
    </script>

    <style>
        span.formfield input[type="text"], span.formfield input[type="password"], span.formfield select {
            width: 220px;
        }

        .announcement
    {
        -moz-border-radius: 10px; /* Firefox */
        -webkit-border-radius: 10px; /* Safari, Chrome */
        border-radius: 10px 10px 10px 10px;
        border: 1px solid rgb(169, 57, 139);
        padding: 8px;
        margin-top: 35px;
    }

    </style>

    <!--[if IE 7]>
    <link rel="stylesheet" type="text/css" href="/static/css/IE7.css" />
    <style type="text/css">
        .showpassword {float:right; !important; margin-top:-20px;}
        .showpassword2 {witdh:220px;}
        span.formfield
        {
                background-color: #ededee;
                padding: 0px 0px 0px 0px;
                margin:0px 0px 0px 3px;
                background: transparent url(/resources/img/bg/forms/input_right.png) no-repeat top right;
                display: inline-block;
                width:405px !important;
        }

    </style>
    <![endif]-->
    <!--[if lt IE 8]>
        <style type="text/css">
            span.formfield{
                 background-position: right 1px !important;
            }

            span.formfield select{
                background-color: #ededee;
            }


        </style>
    <![endif]-->
    <!--[if IE 8]>
        <style type="text/css">
            span.formfield input[type="text"], span.formfield input[type="password"], span.formfield select{
                 font-size:17px !important;
            }
        </style>
    <![endif]-->

</head>
<body>
    <form name="aspnetForm" method="post" action="belplafond.aspx" id="aspnetForm">
<div>
<input type="hidden" name="__EVENTTARGET" id="__EVENTTARGET" value="" />
<input type="hidden" name="__EVENTARGUMENT" id="__EVENTARGUMENT" value="" />
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwUJLTE5ODE2NDY3D2QWAmYPZBYCAgMPZBYGAgEPFgIeBFRleHQF3gE8ZGl2IGNsYXNzPSJtZW51Ij48c3BhbiBpZD0ibWVudV90YXJpZXZlbiI+PGEgaHJlZj0iaHR0cDovL3d3dy5zaW1wZWwubmwvVGFyaWV2ZW4uYXNweCIgdGFyZ2V0PSJfYmxhbmsiPnRhcmlldmVuPC9hPjwvc3Bhbj48c3BhbiBpZD0ibWVudV9mYXEiPjxhIGhyZWY9Imh0dHA6Ly93d3cuc2ltcGVsLm5sL2ZhcS5hc3B4IiB0YXJnZXQ9Il9ibGFuayI+dnJhZ2VuPC9hPjwvc3Bhbj48L2Rpdj5kAgUPFgIfAAW/Bjx1bCBjbGFzcz0ibWVudSI+PGxpPjxhIGlkPSJob21lIiBocmVmPSIvbGFuZGluZy5hc3B4Ij5ob21lPC9hPjwvbGk+PGxpPjxhIGlkPSJhY2NvdW50IiBocmVmPSIvYWNjb3VudC5hc3B4Ij5taWpuIGdlZ2V2ZW5zPC9hPjwvbGk+PGxpPjxhIGlkPSJzaW1wcm9wZXJ0aWVzIiBocmVmPSIvc2ltcHJvcGVydGllcy5hc3B4Ij5nZWdldmVucyBhYm9ubmVtZW50PC9hPjwvbGk+PGxpPjxhIGlkPSJ1cGdyYWRlIiBocmVmPSIvdXBncmFkZS5hc3B4Ij53aWp6aWcgYWJvbm5lbWVudDwvYT48L2xpPjxsaT48YSBpZD0iYmVscGxhZm9uZCIgaHJlZj0iL2JlbHBsYWZvbmQuYXNweCI+cGxhZm9uZDwvYT48L2xpPjxsaT48YSBpZD0iaW52b2ljZXMiIGhyZWY9Ii9pbnZvaWNlcy5hc3B4Ij5mYWN0dXJlbjwvYT48L2xpPjxsaT48YSBpZD0iY2FsbF9kZXRhaWxzIiBocmVmPSIvcmVxdWVzdF9zcGVjaWZpY2F0aW9ucy5hc3B4Ij5iZWxzcGVjaWZpY2F0aWU8L2E+PC9saT48bGk+PGEgaWQ9ImNyZWRpdCIgaHJlZj0iL2NyZWRpdC5hc3B4Ij5hY3R1ZWVsIHZlcmJydWlrPC9hPjwvbGk+PGxpPjxhIGlkPSJjaGFuZ2VfcGFzc3dvcmQiIGhyZWY9Ii9wYXNzd29yZF9lZGl0LmFzcHgiPndpanppZyB3YWNodHdvb3JkPC9hPjwvbGk+PGxpPjxhIGlkPSJibG9jayIgaHJlZj0iL2Jsb2NrLmFzcHgiPmJsb2trZWVyIG51bW1lcjwvYT48L2xpPjxsaT48YSBpZD0ic2ltc3dhcCIgaHJlZj0iL1NpbVN3YXAuYXNweCI+dmVydmFuZ2VuZGUgU2lta2FhcnQ8L2E+PC9saT48bGk+PGEgaWQ9ImNvbnRhY3QiIGhyZWY9Ii9jb250YWN0LmFzcHgiPnN0ZWwgamUgdnJhYWc8L2E+PC9saT48L3VsPmQCBw9kFgYCAQ8WAh8ABQowNjIzNDIyNDkxZAIDD2QWAgIFDxYCHwAFqwM8dHI+PHRkIGNsYXNzPSJ0ZDAiPlBsYWZvbmQ8L3RkPjx0ZCBjbGFzcz0idGQxIj48c3BhbiBjbGFzcz0iZm9ybWZpZWxkIiBzdHlsZT0iZm9udC1zaXplOjE4cHg7IGNvbG9yOiM2NjY2NjY7Ij7igqwgMTIsNTA8c3Bhbj48L3RkPjx0ZCBjbGFzcz0idGQ0Ij48aW1nIHNyYz0iL3Jlc291cmNlcy9pbWcvbWlzYy90b29sdGlwLnBuZyIgY2xhc3M9InRvb2x0aXB0YXJnZXQiIHRpdGxlPSJIZXQgUGxhZm9uZCBrYW4gYWxsZWVuIGluZ2VzdGVsZCB3b3JkZW4gbWV0IHN0YXBwZW4gdmFuIOKCrCAyLDUwIGJvdmVub3AgamUgbWFhbmRiZWRyYWcgZW4gZGllbnQgbWluaW1hYWwg4oKsIDEwIHRlIGJlZHJhZ2VuLiBNZWVyIGluZm8gaGllcm92ZXI/IEtpamsgb3Agb256ZSB3ZWJzaXRlIGJpaiBDb250cm9sZSBvdmVyIGplIGtvc3RlbiIgLz48L3RkPjwvdHI+ZAIFDxYCHgdWaXNpYmxlZxYEAgIPFgIfAAUKMDYyMzQyMjQ5MWQCBQ8WAh8BZ2Rkd0Jh0ImT8a2AhVRgZscnRg6lqB4=" />
</div>

<script type="text/javascript">
//<![CDATA[
var theForm = document.forms['aspnetForm'];
if (!theForm) {
    theForm = document.aspnetForm;
}
function __doPostBack(eventTarget, eventArgument) {
    if (!theForm.onsubmit || (theForm.onsubmit() != false)) {
        theForm.__EVENTTARGET.value = eventTarget;
        theForm.__EVENTARGUMENT.value = eventArgument;
        theForm.submit();
    }
}
//]]>
</script>


<div>

        <input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="0438F5CB" />
        <input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="/wEWBwKc18q6BwL0+5uXBQK4qKpjArionmMCuKiiYwKPg92dCwLHjbmPC3RqmWjScfOTz8xcr9uF3FosF4/A" />
</div>
    <div class="container">
                <div class="header">
                        <img src="/resources/img/logo/simpellogo.png" alt="simpel" id="simpellogo" />
                        <div class="menu"><span id="menu_tarieven"><a href="http://www.simpel.nl/Tarieven.aspx" target="_blank">tarieven</a></span><span id="menu_faq"><a href="http://www.simpel.nl/faq.aspx" target="_blank">vragen</a></span></div>
                </div>

        <div class="contentcontainer">
            <div class="content errorbox" id="error">
                <div class="errorcontent">
                </div>
                <a href="#" class="close">x</a>
            </div>
            <div class="content" id="content">
                <div class="menucontainer">


                    <ul class="menu"><li><a id="home" href="/landing.aspx">home</a></li><li><a id="account" href="/account.aspx">mijn gegevens</a></li><li><a id="simproperties" href="/simproperties.aspx">gegevens abonnement</a></li><li><a id="upgrade" href="/upgrade.aspx">wijzig abonnement</a></li><li><a id="belplafond" href="/belplafond.aspx">plafond</a></li><li><a id="invoices" href="/invoices.aspx">facturen</a></li><li><a id="call_details" href="/request_specifications.aspx">belspecificatie</a></li><li><a id="credit" href="/credit.aspx">actueel verbruik</a></li><li><a id="change_password" href="/password_edit.aspx">wijzig wachtwoord</a></li><li><a id="block" href="/block.aspx">blokkeer nummer</a></li><li><a id="simswap" href="/SimSwap.aspx">vervangende Simkaart</a></li><li><a id="contact" href="/contact.aspx">stel je vraag</a></li></ul>
                </div>

<div class="top_corner_nr">Mijn Simpel voor 0624789621</div>

    <h1>Plafond</h1>

        Het Plafond zorgt ervoor dat je altijd controle hebt over de gebruikskosten van jezelf of bijvoorbeeld dat van je kind. Je kunt zelf de limiet hieronder instellen en altijd weer aanpassen. Het Plafond geldt voor alle abonnementskosten en gebruikskosten samen. Dus niet alleen voor bellen, maar ook voor sms'en of internetten.
        <br /><br /><strong>Advies:</strong> kies je Plafond bedrag iets hoger dan je abonnementskosten, omdat je anders bijvoorbeeld niet in– en/of naar het buitenland of naar 0900-informatie nummers kunt bellen (omdat dit soort telefoon gesprekken niet binnen je vaste abonnementskosten vallen).


    <table style="margin-top:20px;">
        <tr><td class="td0">Plafond</td><td class="td1"><span class="formfield" style="font-size:18px; color:#666666;">€ 12,50<span></td><td class="td4"><img src="/resources/img/misc/tooltip.png" class="tooltiptarget" title="Het Plafond kan alleen ingesteld worden met stappen van € 2,50 bovenop je maandbedrag en dient minimaal € 10 te bedragen. Meer info hierover? Kijk op onze website bij Controle over je kosten" /></td></tr>
    </table>
    <div style="margin-top:-12px; margin-bottom:90px">
    <a id="ctl00_content_lbModify" class="button btn" href="javascript:__doPostBack('ctl00$content$lbModify','')">Wijzig</a>
    </div>



     <h1>3 nummers instellen voor 0624789621 </h1>

      Het kan natuurlijk wel eens gebeuren dat je het Plafond bereikt. Wanneer dit gebeurt wordt al het uitgaand en inkomend verkeer dat zorgt voor extra kosten geblokkeerd.
      Als je ook je belbundel volledig hebt verbruikt, heeft Simpel er voor gezorgd dat je nog 3 nummers kunt bellen als het &#233;cht nodig is. Handig voor ouders met kinderen! <i>Voor het bellen naar deze telefoonnummers,
      na het bereiken van het Plafond en het verbruiken van je belbundel, geldt het buitenbundeltarief</i>.

    <h3>Geef hieronder maximaal 3 nummers op</h3>
    <table>
        <tr>
            <td class="td0">Telefoonnummer 1</td>
            <td class="td1" colspan="3"><span class="formfield"><input name="ctl00$content$txtWhiteListNumber01" type="text" maxlength="12" id="ctl00_content_txtWhiteListNumber01" optional="true" validation="whitelist" validationname="" /></span></td>
            <td class="td4"><img id="ctl00_content_imgtxtWhiteListNumber01" class="tooltiptarget" src="/resources/img/misc/tooltip.png" style="border-width:0px;" /></td>
        </tr>
        <tr>
            <td class="td0">Telefoonnummer 2</td>
            <td class="td1" colspan="3"><span class="formfield"><input name="ctl00$content$txtWhiteListNumber02" type="text" maxlength="12" id="ctl00_content_txtWhiteListNumber02" optional="true" validation="whitelist" validationname="" /></span></td>
           <td class="td4"><img id="ctl00_content_imgtxtWhiteListNumber02" class="tooltiptarget" src="/resources/img/misc/tooltip.png" style="border-width:0px;" /></td>
        </tr>
        <tr>
            <td class="td0">Telefoonnummer 3</td>
            <td class="td1" colspan="3"><span class="formfield"><input name="ctl00$content$txtWhiteListNumber03" type="text" maxlength="12" id="ctl00_content_txtWhiteListNumber03" optional="true" validation="whitelist" validationname="" /></span></td>
           <td class="td4"><img id="ctl00_content_imgtxtWhiteListNumber03" class="tooltiptarget" src="/resources/img/misc/tooltip.png" style="border-width:0px;" /></td>
        </tr>
    </table>
    <a id="ctl00_content_lbSubmit" class="button btn2" href="javascript:__doPostBack('ctl00$content$lbSubmit','')">Opslaan</a>

            </div>




            <div class="clear"></div>


             <div class="footer">
                            <span><a href="http://www.simpel.nl/contact.aspx" target="_blank">contact</a></span><span><a href="http://www.simpel.nl/privacyverklaring.aspx" target="_blank">privacyverklaring</a></span><span><a href="http://www.simpel.nl/Voorwaarden.aspx" target="_blank">voorwaarden</a></span>
                    </div>
                    <a id="ctl00_lbLogOut" class="login" href="javascript:__doPostBack('ctl00$lbLogOut','')">uitloggen</a>
        </div>
    </div>
    </form>
</body>
</html>
"""

data_contract = """

<!DOCTYPE html>

<html>
<head><meta charset="utf-8" /><meta http-equiv="X-UA-Compatible" content="IE-edge,chrome=1" /><title>
        Mijn Simpel
</title><link href="/resources/css/defaults.css?v=002" rel="stylesheet" type="text/css" /><link href="/resources/css/master.css?v=002" rel="stylesheet" type="text/css" /><link href="/resources/css/cookiechecker.css?v=002" rel="stylesheet" type="text/css" />
    <!--[if lte IE 8]>
   <link href="/resources/css/cookiecheckerIE.css?v=002" rel="stylesheet" type="text/css" />
    <![endif]-->

    <script src="/resources/js/jquery-1.7.2.min.js" type="text/javascript"></script>
    <script src="/resources/js/jquery-ui-1.8.7.custom.min.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.corner.js" type="text/javascript"></script>
    <script src="/resources/js/prototypes.js" type="text/javascript"></script>
    <script src="/resources/js/validatie.js?v=003" type="text/javascript"></script>
    <script src="/resources/js/tooltip.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.tools.min.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.ui.datepicker-nl.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.reveal.cookie.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.reveal.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.reveal.contact.js" type="text/javascript"></script>
    <script src="/resources/js/cookiechecker.js" type="text/javascript"></script>
    <script src="/resources/js/checkiban.js" type="text/javascript"></script>

    <!-- Google Analyticsscript -->
    <script>(function (i, s, o, g, r, a, m) { i['GoogleAnalyticsObject'] = r; i[r] = i[r] || function () { (i[r].q = i[r].q || []).push(arguments) }, i[r].l = 1 * new Date(); a = s.createElement(o), m = s.getElementsByTagName(o)[0]; a.async = 1; a.src = g; m.parentNode.insertBefore(a, m) })(window, document, 'script', '//www.google-analytics.com/analytics.js', 'ga'); ga('create', 'UA-1956252-1', 'simpel.nl'); ga('send', 'pageview');</script>
    <!-- End Google Analyticsscript -->

    <script type="text/javascript">
        //<![CDATA[
        $(document).ready(function () {

                        $("form1").submit(function () {
                $(this).submit(function () {
                    return false;
                });
                return true;
            });


            doTooltip('.tooltiptarget');

            $(".tooltiptargetlink").tooltip({ position: 'left top', offset: [45, -15], effect: 'fade' });

            ValidateInitialize('select, input[type=checkbox], input[type=password], input[type=text]');
            $('.submit').bind('click', function (event) {
                if (!doValidateAll('select, input[type=checkbox], input[type=password], input[type=text]')) {
                    event.preventDefault();
                }
            });


            $('img#simpellogo').bind('click', function (event) {
                window.location.href = '/';
                event.preventDefault();
            });

            $('div.content').corner('10px');
            $('a.button').corner('5px');
            if ($.browser.msie && $.browser.version < 9) {
                $('.menu .selected').corner('4px');
            } else {
                $('.menu span, .menu li a').corner('4px');
            }

            $('.login').corner('5px bottom');

            $('table.classictable').each(function () {
                $(this).find('tr:even').addClass('alt');
            });
        });

        function getCookie(c_name) {
            var i, x, y, ARRcookies = document.cookie.split(";");
            for (i = 0; i < ARRcookies.length; i++) {
                x = ARRcookies[i].substr(0, ARRcookies[i].indexOf("="));
                y = ARRcookies[i].substr(ARRcookies[i].indexOf("=") + 1);
                x = x.replace(/^\s+|\s+$/g, "");
                if (x == c_name) {
                    return unescape(y);
                }
            }
        }

        //]]>
    </script>

    <script type="text/javascript">
        //<![CDATA[
        $(document).ready(function(){
             message('#error', 3, false, '', '');
             $('#simproperties').addClass('selected');

        });
        //]]>
    </script>

    <!--[if IE 7]>
    <link rel="stylesheet" type="text/css" href="/static/css/IE7.css" />
    <style type="text/css">
        .showpassword {float:right; !important; margin-top:-20px;}
        .showpassword2 {witdh:220px;}
        span.formfield
        {
                background-color: #ededee;
                padding: 0px 0px 0px 0px;
                margin:0px 0px 0px 3px;
                background: transparent url(/resources/img/bg/forms/input_right.png) no-repeat top right;
                display: inline-block;
                width:405px !important;
        }

    </style>
    <![endif]-->
    <!--[if lt IE 8]>
        <style type="text/css">
            span.formfield{
                 background-position: right 1px !important;
            }

            span.formfield select{
                background-color: #ededee;
            }


        </style>
    <![endif]-->
    <!--[if IE 8]>
        <style type="text/css">
            span.formfield input[type="text"], span.formfield input[type="password"], span.formfield select{
                 font-size:17px !important;
            }
        </style>
    <![endif]-->

</head>
<body>
    <form name="aspnetForm" method="post" action="simproperties.aspx" id="aspnetForm">
<div>
<input type="hidden" name="__EVENTTARGET" id="__EVENTTARGET" value="" />
<input type="hidden" name="__EVENTARGUMENT" id="__EVENTARGUMENT" value="" />
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwUKMTg4MDQwNjE0OA9kFgJmD2QWAgIDD2QWBgIBDxYCHgRUZXh0Bd4BPGRpdiBjbGFzcz0ibWVudSI+PHNwYW4gaWQ9Im1lbnVfdGFyaWV2ZW4iPjxhIGhyZWY9Imh0dHA6Ly93d3cuc2ltcGVsLm5sL1RhcmlldmVuLmFzcHgiIHRhcmdldD0iX2JsYW5rIj50YXJpZXZlbjwvYT48L3NwYW4+PHNwYW4gaWQ9Im1lbnVfZmFxIj48YSBocmVmPSJodHRwOi8vd3d3LnNpbXBlbC5ubC9mYXEuYXNweCIgdGFyZ2V0PSJfYmxhbmsiPnZyYWdlbjwvYT48L3NwYW4+PC9kaXY+ZAIFDxYCHwAFvwY8dWwgY2xhc3M9Im1lbnUiPjxsaT48YSBpZD0iaG9tZSIgaHJlZj0iL2xhbmRpbmcuYXNweCI+aG9tZTwvYT48L2xpPjxsaT48YSBpZD0iYWNjb3VudCIgaHJlZj0iL2FjY291bnQuYXNweCI+bWlqbiBnZWdldmVuczwvYT48L2xpPjxsaT48YSBpZD0ic2ltcHJvcGVydGllcyIgaHJlZj0iL3NpbXByb3BlcnRpZXMuYXNweCI+Z2VnZXZlbnMgYWJvbm5lbWVudDwvYT48L2xpPjxsaT48YSBpZD0idXBncmFkZSIgaHJlZj0iL3VwZ3JhZGUuYXNweCI+d2lqemlnIGFib25uZW1lbnQ8L2E+PC9saT48bGk+PGEgaWQ9ImJlbHBsYWZvbmQiIGhyZWY9Ii9iZWxwbGFmb25kLmFzcHgiPnBsYWZvbmQ8L2E+PC9saT48bGk+PGEgaWQ9Imludm9pY2VzIiBocmVmPSIvaW52b2ljZXMuYXNweCI+ZmFjdHVyZW48L2E+PC9saT48bGk+PGEgaWQ9ImNhbGxfZGV0YWlscyIgaHJlZj0iL3JlcXVlc3Rfc3BlY2lmaWNhdGlvbnMuYXNweCI+YmVsc3BlY2lmaWNhdGllPC9hPjwvbGk+PGxpPjxhIGlkPSJjcmVkaXQiIGhyZWY9Ii9jcmVkaXQuYXNweCI+YWN0dWVlbCB2ZXJicnVpazwvYT48L2xpPjxsaT48YSBpZD0iY2hhbmdlX3Bhc3N3b3JkIiBocmVmPSIvcGFzc3dvcmRfZWRpdC5hc3B4Ij53aWp6aWcgd2FjaHR3b29yZDwvYT48L2xpPjxsaT48YSBpZD0iYmxvY2siIGhyZWY9Ii9ibG9jay5hc3B4Ij5ibG9ra2VlciBudW1tZXI8L2E+PC9saT48bGk+PGEgaWQ9InNpbXN3YXAiIGhyZWY9Ii9TaW1Td2FwLmFzcHgiPnZlcnZhbmdlbmRlIFNpbWthYXJ0PC9hPjwvbGk+PGxpPjxhIGlkPSJjb250YWN0IiBocmVmPSIvY29udGFjdC5hc3B4Ij5zdGVsIGplIHZyYWFnPC9hPjwvbGk+PC91bD5kAgcPZBYSAgEPFgIfAAUKMDYyMzQyMjQ5MWQCDQ8WAh8ABR1TaW1wZWwgb25iZXBlcmt0IGJlbGxlbnwgMCwwMGQCEQ8WAh4HVmlzaWJsZWhkAhMPFgIfAAUZM0cgaW50ZXJuZXQgJiBzbXMgYnVuZGVsc2QCFQ8WAh8ABS9TaW1wZWwgMTAwMCBNQiBpbnRlcm5ldCB8IDEwLDAwICsgb25iZXBlcmt0IHNtc2QCGw8WAh8ABQwyNCBtYWFuZChlbilkAiEPFgIfAAUKMjktMDItMjAxNmQCJw8WAh8ABQg5NzMxMTk1MGQCLQ8WAh8ABbQcPHRhYmxlIHN0eWxlPSJ3aWR0aDo3MzdweDsiPjx0cj48dGQgY2xhc3M9InRkMCI+TnVtbWVyd2VlcmdhdmUgb3Agc3BlY2lmaWNhdGllPC90ZD48dGQgY2xhc3M9InRkMSI+TnVtbWVyd2VlcmdhdmUgb3Agc3BlY2lmaWNhdGllcyBhZmdlc2NoZXJtZDwvdGQ+PC90cj48dHI+PHRkIGNsYXNzPSJ0ZDAiPlNNUzwvdGQ+PHRkIGNsYXNzPSJ0ZDEiPlNNUyB2ZXJzdHVyZW4gdG9lZ2VzdGFhbjwvdGQ+PHRkIGNsYXNzPSJ0ZDQiPjxpbWcgc3JjPSIvcmVzb3VyY2VzL2ltZy9taXNjL3Rvb2x0aXAucG5nIiBjbGFzcz0idG9vbHRpcHRhcmdldCIgdGl0bGU9IkFscyBqZSBraWVzdCB2b29yIFNNUyB0b2VzdGFhbiwgYmV0ZWtlbnQgZGl0IGRhdCBqZSBTTVMtYmVyaWNodGVuIGt1bnQgdmVyc3R1cmVuIHZhbmFmIGplIG1vYmllbGUgdGVsZWZvb24uIFNNUyB2ZXJzdHVyZW4gZ2VibG9ra2VlcmQgYmV0ZWtlbnQgZGF0IGplIGdlZW4gU01TLWJlcmljaHRlbiBrdW50IHZlcnN0dXJlbiB2YW5hZiBqZSBtb2JpZWxlIHRlbGVmb29uLiBXZWxrZSBpbnN0ZWxsaW5nIGplIG9vayBraWVzdCwgamUga3VudCB3ZWwgU01TLWJlcmljaHRlbiBvbnR2YW5nZW4uIiAvPjwvdGQ+PC90cj48dHI+PHRkIGNsYXNzPSJ0ZDAiPk1NUzwvdGQ+PHRkIGNsYXNzPSJ0ZDEiPk1NUyB2ZXJzdHVyZW4gbmlldCB0b2VnZXN0YWFuPC90ZD48dGQgY2xhc3M9InRkNCI+PGltZyBzcmM9Ii9yZXNvdXJjZXMvaW1nL21pc2MvdG9vbHRpcC5wbmciIGNsYXNzPSJ0b29sdGlwdGFyZ2V0IiB0aXRsZT0iQWxzIGplIGtpZXN0IHZvb3IgTU1TIHZlcnN0dXJlbiB0b2VzdGFhbiwgYmV0ZWtlbnQgZGl0IGRhdCBqZSBNTVMtYmVyaWNodGVuIGt1bnQgdmVyc3R1cmVuIHZhbmFmIGplIG1vYmllbGUgdGVsZWZvb24uIE1NUyB2ZXJzdHVyZW4gbmlldCB0b2VzdGFhbiBiZXRla2VudCBkYXQgamUgZ2VlbiBNTVMtYmVyaWNodGVuIGt1bnQgdmVyc3R1cmVuIHZhbmFmIGplIG1vYmllbGUgdGVsZWZvb24uIFdlbGtlIGluc3RlbGxpbmcgamUgb29rIGtpZXN0LCBqZSBrdW50IHdlbCBNTVMtYmVyaWNodGVuIG9udHZhbmdlbi4gTEVUIE9QOiBKZSBoZWJ0IHZvb3IgaGV0IG9udHZhbmdlbiBlbiB2ZXJzdHVyZW4gdmFuIE1NUy1iZXJpY2h0ZW4sIGFwYXJ0ZSBpbnN0ZWxsaW5nZW4gbm9kaWcgb3AgamUgbW9iaWVsZSB0ZWxlZm9vbi4iIC8+PC90ZD48L3RyPjx0cj48dGQgY2xhc3M9InRkMCI+MDkwMCBlbnRlcnRhaW5tZW50PC90ZD48dGQgY2xhc3M9InRkMSI+MDkwMCBlbnRlcnRhaW5tZW50IGJlbGxlbiBnZWJsb2trZWVyZDwvdGQ+PHRkIGNsYXNzPSJ0ZDQiPjxpbWcgc3JjPSIvcmVzb3VyY2VzL2ltZy9taXNjL3Rvb2x0aXAucG5nIiBjbGFzcz0idG9vbHRpcHRhcmdldCIgdGl0bGU9IkFscyBqZSBraWVzdCB2b29yIDA5MDAgZW50ZXJ0YWlubWVudCB0b2VnZXN0YWFuLCBkYW4ga3VuIGplIGdlYnJ1aWsgbWFrZW4gdmFuIDA5MDAgZW50ZXJ0YWlubWVudCBudW1tZXJzLiBEZXplIG9wdGllIGtvbXQgYmVzY2hpa2JhYXIgd2FubmVlciBqZSBpbiB0b3RhYWwgMyBmYWN0dXJlbiBoZWJ0IHZvbGRhYW4uIExldCBvcDogaGV0IHZlcmJydWlrIHZhbiAwOTAwIGVudGVydGFpbm1lbnQgbnVtbWVycyB2YWx0IGJ1aXRlbiBqZSBidW5kZWwuIiAvPjwvdGQ+PC90cj48dHI+PHRkIGNsYXNzPSJ0ZDAiPklua29tZW5kZSBnZXNwcmVra2VuPC90ZD48dGQgY2xhc3M9InRkMSI+R2VlbiBibG9ra2FkZSBvcCBpbmtvbWVuZGUgZ2VzcHJla2tlbjwvdGQ+PHRkIGNsYXNzPSJ0ZDQiPjxpbWcgc3JjPSIvcmVzb3VyY2VzL2ltZy9taXNjL3Rvb2x0aXAucG5nIiBjbGFzcz0idG9vbHRpcHRhcmdldCIgdGl0bGU9IkFscyBqZSBraWVzdCB2b29yIGFsbGUgaW5rb21lbmRlIGdlc3ByZWtrZW4gZ2VibG9ra2VlcmQga3VuIGplIG5pZXQgbWVlciBnZWJlbGQgd29yZGVuLiBBbHMgamUga2llc3Qgdm9vciBhbGxlZW4gaW5rb21lbmRlIGdlc3ByZWtrZW4gaW4gaGV0IGJ1aXRlbmxhbmQgZ2VibG9ra2VlcmQga3VuIGplIG5pZXQgbWVlciBnZWJlbGQgd29yZGVuIGluIGhldCBidWl0ZW5sYW5kLiBBbHMgamUgZ2VlbiBibG9ra2FkZSBvcCBpbmtvbWVuZGUgZ2VzcHJla2tlbiBraWVzdCBrdW4gamUgaW4gYmlubmVuLSBlbiBidWl0ZW5sYW5kIGdlYmVsZCB3b3JkZW4uIFdlbGtlIGluc3RlbGxpbmcgamUgb29rIGtpZXN0LCBqZSBrdW50IHdlbCBTTVMtYmVyaWNodGVuIG9udHZhbmdlbi4iIC8+PC90ZD48L3RyPjx0cj48dGQgY2xhc3M9InRkMCI+VWl0Z2FhbmRlIGdlc3ByZWtrZW48L3RkPjx0ZCBjbGFzcz0idGQxIj5HZWVuIGJsb2trYWRlIG9wIHVpdGdhYW5kZSBnZXNwcmVra2VuPC90ZD48dGQgY2xhc3M9InRkNCI+PGltZyBzcmM9Ii9yZXNvdXJjZXMvaW1nL21pc2MvdG9vbHRpcC5wbmciIGNsYXNzPSJ0b29sdGlwdGFyZ2V0IiB0aXRsZT0iQWxzIGplIGtpZXN0IHZvb3IgYWxsZSB1aXRnYWFuZGUgZ2VzcHJla2tlbiBnZWJsb2trZWVyZCBrdW4gamUgbmlldCBtZWVyIGJlbGxlbi4gQWxzIGplIGJlbGxlbiBpbiBoZXQgYnVpdGVubGFuZCBnZWJsb2trZWVyZCBraWVzdCBrdW4gamUgbmlldCBtZWVyIGJlbGxlbiBpbiBoZXQgYnVpdGVubGFuZC4gQWxzIGplIGJlbGxlbiBuYWFyIGhldCBidWl0ZW5sYW5kIGdlYmxva2tlZXJkIGtpZXN0IGt1biBqZSBuaWV0IG1lZXIgdmFudWl0IE5lZGVybGFuZCBuYWFyIGhldCBidWl0ZW5sYW5kIGJlbGxlbi4gQWxzIGplIGtpZXN0IHZvb3IgZ2VlbiBibG9ra2FkZSBvcCB1aXRnYWFuZGUgZ2VzcHJla2tlbiBkYW4ga3VuIGplIGluIGJpbm5lbiBlbiBidWl0ZW5sYW5kIGJsaWp2ZW4gYmVsbGVuLiBXZWxrZSBpbnN0ZWxsaW5nIGplIG9vayBraWVzdCwgamUga3VudCB3ZWwgU01TLWJlcmljaHRlbiBvbnR2YW5nZW4uIiAvPjwvdGQ+PC90cj48dHI+PHRkIGNsYXNzPSJ0ZDAiPkdQUlM8L3RkPjx0ZCBjbGFzcz0idGQxIj5HUFJTIG5pZXQgZ2VibG9ra2VlcmQ8L3RkPjwvdHI+PHRyPjx0ZCBjbGFzcz0idGQwIj5CdWl0ZW5sYW5kZ2VicnVpazwvdGQ+PHRkIGNsYXNzPSJ0ZDEiPkdlZW4gYmxva2thZGUgaW4gaGV0IGJ1aXRlbmxhbmQ8L3RkPjx0ZCBjbGFzcz0idGQ0Ij48aW1nIHNyYz0iL3Jlc291cmNlcy9pbWcvbWlzYy90b29sdGlwLnBuZyIgY2xhc3M9InRvb2x0aXB0YXJnZXQiIHRpdGxlPSJBbHMgamUga2llc3Qgdm9vciB0b2VzdGVsIGluIGhldCBidWl0ZW5sYW5kIGdlYmxva2tlZXJkIGt1biBqZSBpbiBoZXQgYnVpdGVubGFuZCBuaWV0IGJlbGxlbiBvZiBnZWJlbGQgd29yZGVuLCBTTVNlbiBlbiBtb2JpZWwgaW50ZXJuZXR0ZW4uIiAvPjwvdGQ+PC90cj48dHI+PHRkIGNsYXNzPSJ0ZDAiPkJldGFhbGRlIFNNUyBkaWVuc3RlbjwvdGQ+PHRkIGNsYXNzPSJ0ZDEiPkJldGFhbGRlIFNNUyBkaWVuc3RlbiBuaWV0IHRvZWdlc3RhYW48L3RkPjx0ZCBjbGFzcz0idGQ0Ij48aW1nIHNyYz0iL3Jlc291cmNlcy9pbWcvbWlzYy90b29sdGlwLnBuZyIgY2xhc3M9InRvb2x0aXB0YXJnZXQiIHRpdGxlPSJBbHMgamUga2llc3Qgdm9vciBoZXQgdG9lc3RhYW4gdmFuIGJldGFhbGRlIFNNUyBkaWVuc3RlbiBpcyBoZXQgbW9nZWxpamsgb20gYmV0YWFsZGUgc21zIGRpZW5zdGVuIHRlIG9udHZhbmdlbi4iIC8+PC90ZD48L3RyPjwvdGFibGU+ZGS7YqCrTl2WnEUuwIGnA5Mvrnmw7Q==" />
</div>

<script type="text/javascript">
//<![CDATA[
var theForm = document.forms['aspnetForm'];
if (!theForm) {
    theForm = document.aspnetForm;
}
function __doPostBack(eventTarget, eventArgument) {
    if (!theForm.onsubmit || (theForm.onsubmit() != false)) {
        theForm.__EVENTTARGET.value = eventTarget;
        theForm.__EVENTARGUMENT.value = eventArgument;
        theForm.submit();
    }
}
//]]>
</script>


<div>

        <input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="79120594" />
        <input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="/wEWAwLt3rPuCgKPg92dCwLHjbmPC6VRxFhgu4b00LHDRWrVFxbCa5Pi" />
</div>
    <div class="container">
                <div class="header">
                        <img src="/resources/img/logo/simpellogo.png" alt="simpel" id="simpellogo" />
                        <div class="menu"><span id="menu_tarieven"><a href="http://www.simpel.nl/Tarieven.aspx" target="_blank">tarieven</a></span><span id="menu_faq"><a href="http://www.simpel.nl/faq.aspx" target="_blank">vragen</a></span></div>
                </div>

        <div class="contentcontainer">
            <div class="content errorbox" id="error">
                <div class="errorcontent">
                </div>
                <a href="#" class="close">x</a>
            </div>
            <div class="content" id="content">
                <div class="menucontainer">


                    <ul class="menu"><li><a id="home" href="/landing.aspx">home</a></li><li><a id="account" href="/account.aspx">mijn gegevens</a></li><li><a id="simproperties" href="/simproperties.aspx">gegevens abonnement</a></li><li><a id="upgrade" href="/upgrade.aspx">wijzig abonnement</a></li><li><a id="belplafond" href="/belplafond.aspx">plafond</a></li><li><a id="invoices" href="/invoices.aspx">facturen</a></li><li><a id="call_details" href="/request_specifications.aspx">belspecificatie</a></li><li><a id="credit" href="/credit.aspx">actueel verbruik</a></li><li><a id="change_password" href="/password_edit.aspx">wijzig wachtwoord</a></li><li><a id="block" href="/block.aspx">blokkeer nummer</a></li><li><a id="simswap" href="/SimSwap.aspx">vervangende Simkaart</a></li><li><a id="contact" href="/contact.aspx">stel je vraag</a></li></ul>
                </div>

<div class="top_corner_nr">Mijn Simpel voor 0634456383</div>
    <h1>Gegevens abonnement</h1>







    <h3>&nbsp;</h3>
    <table style="width:637px">
        <tr>
            <td class="td0">Abonnement</td>
            <td class="td1">Simpel onbeperkt bellen| 0,00</td>
            <td class="td4"></td>
        </tr>

        <tr>
            <td class="td0">3G internet & sms bundels</td>
            <td class="td1">Simpel 1000 MB internet | 10,00 + onbeperkt sms</td>
            <td class="td4"></td>
        </tr>

        <tr>
            <td class="td0">Contractsduur</td>
            <td class="td1">24 maand(en)</td>
            <td class="td4"></td>
        </tr>
        <tr>
            <td class="td0">Ingangsdatum eerste contract*</td>
            <td class="td1">29-02-2016</td>
            <td class="td4"></td>
        </tr>
        <tr>
            <td class="td0">PUKcode</td>
            <td class="td1">62321257</td>
            <td class="td4"><img id="ctl00_content_imgPukcode" class="tooltiptarget" title="Als je de pincode op je telefoon 3 keer verkeerd hebt ingetoetst, is de simkaart geblokkeerd. Je kunt de blokkade opheffen met de 8-cijferige PUKcode." src="/resources/img/misc/tooltip.png" style="border-width:0px;" /></td>
        </tr>
    </table>
    <h3>&nbsp;</h3>
        <table style="width:737px;"><tr><td class="td0">Nummerweergave op specificatie</td><td class="td1">Nummerweergave op specificaties afgeschermd</td></tr><tr><td class="td0">SMS</td><td class="td1">SMS versturen toegestaan</td><td class="td4"><img src="/resources/img/misc/tooltip.png" class="tooltiptarget" title="Als je kiest voor SMS toestaan, betekent dit dat je SMS-berichten kunt versturen vanaf je mobiele telefoon. SMS versturen geblokkeerd betekent dat je geen SMS-berichten kunt versturen vanaf je mobiele telefoon. Welke instelling je ook kiest, je kunt wel SMS-berichten ontvangen." /></td></tr><tr><td class="td0">MMS</td><td class="td1">MMS versturen niet toegestaan</td><td class="td4"><img src="/resources/img/misc/tooltip.png" class="tooltiptarget" title="Als je kiest voor MMS versturen toestaan, betekent dit dat je MMS-berichten kunt versturen vanaf je mobiele telefoon. MMS versturen niet toestaan betekent dat je geen MMS-berichten kunt versturen vanaf je mobiele telefoon. Welke instelling je ook kiest, je kunt wel MMS-berichten ontvangen. LET OP: Je hebt voor het ontvangen en versturen van MMS-berichten, aparte instellingen nodig op je mobiele telefoon." /></td></tr><tr><td class="td0">0900 entertainment</td><td class="td1">0900 entertainment bellen geblokkeerd</td><td class="td4"><img src="/resources/img/misc/tooltip.png" class="tooltiptarget" title="Als je kiest voor 0900 entertainment toegestaan, dan kun je gebruik maken van 0900 entertainment nummers. Deze optie komt beschikbaar wanneer je in totaal 3 facturen hebt voldaan. Let op: het verbruik van 0900 entertainment nummers valt buiten je bundel." /></td></tr><tr><td class="td0">Inkomende gesprekken</td><td class="td1">Geen blokkade op inkomende gesprekken</td><td class="td4"><img src="/resources/img/misc/tooltip.png" class="tooltiptarget" title="Als je kiest voor alle inkomende gesprekken geblokkeerd kun je niet meer gebeld worden. Als je kiest voor alleen inkomende gesprekken in het buitenland geblokkeerd kun je niet meer gebeld worden in het buitenland. Als je geen blokkade op inkomende gesprekken kiest kun je in binnen- en buitenland gebeld worden. Welke instelling je ook kiest, je kunt wel SMS-berichten ontvangen." /></td></tr><tr><td class="td0">Uitgaande gesprekken</td><td class="td1">Geen blokkade op uitgaande gesprekken</td><td class="td4"><img src="/resources/img/misc/tooltip.png" class="tooltiptarget" title="Als je kiest voor alle uitgaande gesprekken geblokkeerd kun je niet meer bellen. Als je bellen in het buitenland geblokkeerd kiest kun je niet meer bellen in het buitenland. Als je bellen naar het buitenland geblokkeerd kiest kun je niet meer vanuit Nederland naar het buitenland bellen. Als je kiest voor geen blokkade op uitgaande gesprekken dan kun je in binnen en buitenland blijven bellen. Welke instelling je ook kiest, je kunt wel SMS-berichten ontvangen." /></td></tr><tr><td class="td0">GPRS</td><td class="td1">GPRS niet geblokkeerd</td></tr><tr><td class="td0">Buitenlandgebruik</td><td class="td1">Geen blokkade in het buitenland</td><td class="td4"><img src="/resources/img/misc/tooltip.png" class="tooltiptarget" title="Als je kiest voor toestel in het buitenland geblokkeerd kun je in het buitenland niet bellen of gebeld worden, SMSen en mobiel internetten." /></td></tr><tr><td class="td0">Betaalde SMS diensten</td><td class="td1">Betaalde SMS diensten niet toegestaan</td><td class="td4"><img src="/resources/img/misc/tooltip.png" class="tooltiptarget" title="Als je kiest voor het toestaan van betaalde SMS diensten is het mogelijk om betaalde sms diensten te ontvangen." /></td></tr></table><br/>
    <a id="ctl00_content_lbSubmit" class="button submit" href="javascript:__doPostBack('ctl00$content$lbSubmit','')">Wijzig</a>
    <div>* Ben je een contractverlenging aangegaan? Dan vind je de ingangsdatum van je nieuwe contracttermijn in de bevestigingsmail. </div>

            </div>




            <div class="clear"></div>


             <div class="footer">
                            <span><a href="http://www.simpel.nl/contact.aspx" target="_blank">contact</a></span><span><a href="http://www.simpel.nl/privacyverklaring.aspx" target="_blank">privacyverklaring</a></span><span><a href="http://www.simpel.nl/Voorwaarden.aspx" target="_blank">voorwaarden</a></span>
                    </div>
                    <a id="ctl00_lbLogOut" class="login" href="javascript:__doPostBack('ctl00$lbLogOut','')">uitloggen</a>
        </div>
    </div>
    </form>
</body>
</html>
"""

data_usage = """

<!DOCTYPE html>

<html>
<head><meta charset="utf-8" /><meta http-equiv="X-UA-Compatible" content="IE-edge,chrome=1" /><title>
        Mijn Simpel
</title><link href="/resources/css/defaults.css?v=002" rel="stylesheet" type="text/css" /><link href="/resources/css/master.css?v=002" rel="stylesheet" type="text/css" /><link href="/resources/css/cookiechecker.css?v=002" rel="stylesheet" type="text/css" />
    <!--[if lte IE 8]>
   <link href="/resources/css/cookiecheckerIE.css?v=002" rel="stylesheet" type="text/css" />
    <![endif]-->

    <script src="/resources/js/jquery-1.7.2.min.js" type="text/javascript"></script>
    <script src="/resources/js/jquery-ui-1.8.7.custom.min.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.corner.js" type="text/javascript"></script>
    <script src="/resources/js/prototypes.js" type="text/javascript"></script>
    <script src="/resources/js/validatie.js?v=003" type="text/javascript"></script>
    <script src="/resources/js/tooltip.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.tools.min.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.ui.datepicker-nl.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.reveal.cookie.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.reveal.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.reveal.contact.js" type="text/javascript"></script>
    <script src="/resources/js/cookiechecker.js" type="text/javascript"></script>
    <script src="/resources/js/checkiban.js" type="text/javascript"></script>

    <!-- Google Analyticsscript -->
    <script>(function (i, s, o, g, r, a, m) { i['GoogleAnalyticsObject'] = r; i[r] = i[r] || function () { (i[r].q = i[r].q || []).push(arguments) }, i[r].l = 1 * new Date(); a = s.createElement(o), m = s.getElementsByTagName(o)[0]; a.async = 1; a.src = g; m.parentNode.insertBefore(a, m) })(window, document, 'script', '//www.google-analytics.com/analytics.js', 'ga'); ga('create', 'UA-1956252-1', 'simpel.nl'); ga('send', 'pageview');</script>
    <!-- End Google Analyticsscript -->

    <script type="text/javascript">
        //<![CDATA[
        $(document).ready(function () {

                        $("form1").submit(function () {
                $(this).submit(function () {
                    return false;
                });
                return true;
            });


            doTooltip('.tooltiptarget');

            $(".tooltiptargetlink").tooltip({ position: 'left top', offset: [45, -15], effect: 'fade' });

            ValidateInitialize('select, input[type=checkbox], input[type=password], input[type=text]');
            $('.submit').bind('click', function (event) {
                if (!doValidateAll('select, input[type=checkbox], input[type=password], input[type=text]')) {
                    event.preventDefault();
                }
            });


            $('img#simpellogo').bind('click', function (event) {
                window.location.href = '/';
                event.preventDefault();
            });

            $('div.content').corner('10px');
            $('a.button').corner('5px');
            if ($.browser.msie && $.browser.version < 9) {
                $('.menu .selected').corner('4px');
            } else {
                $('.menu span, .menu li a').corner('4px');
            }

            $('.login').corner('5px bottom');

            $('table.classictable').each(function () {
                $(this).find('tr:even').addClass('alt');
            });
        });

        function getCookie(c_name) {
            var i, x, y, ARRcookies = document.cookie.split(";");
            for (i = 0; i < ARRcookies.length; i++) {
                x = ARRcookies[i].substr(0, ARRcookies[i].indexOf("="));
                y = ARRcookies[i].substr(ARRcookies[i].indexOf("=") + 1);
                x = x.replace(/^\s+|\s+$/g, "");
                if (x == c_name) {
                    return unescape(y);
                }
            }
        }

        //]]>
    </script>

    <script type="text/javascript">
        //<![CDATA[
        $(document).ready(function(){
            message('#error', 3, false, '', '');
            $('#credit').addClass('selected');

            $('#bellen').progressbar({ value: 0 });
            $('#sms').progressbar({ value:  0 });
            $('#internet').progressbar({ value:  2});
            //$('#buitenland').progressbar({ value: 0 });

        });
        //]]>
    </script>
    <style type="text/css">
        .announcement {
            -moz-border-radius: 10px; /* Firefox */
            -webkit-border-radius: 10px; /* Safari, Chrome */
            border-radius: 10px 10px 10px 10px;
            border: 1px solid rgb(169, 57, 139);
            padding: 8px;
            margin-top: 5px;
        }

        .bar_item {
            width: 600px;
        }

        .bar_desc {
            width: 100%;
            color: #A9398B;
            margin-top: 7px;
            font-weight: bold;
        }

        .bar_load {
            width: 100%;
            border-radius: 0px !important;
            border: 1px solid #000000 !important;
            position: relative;
            margin-top:7px;
        }

            .bar_load .ui-corner-left {
                border-radius: 0px !important;
            }

            .bar_load .ui-widget-header {
                border: 1px solid #000000;
            }

        .progress-label {
            position: absolute;
            left: 38%;
            top: -21px;
        }
    </style>

    <!--[if IE 7]>
    <link rel="stylesheet" type="text/css" href="/static/css/IE7.css" />
    <style type="text/css">
        .showpassword {float:right; !important; margin-top:-20px;}
        .showpassword2 {witdh:220px;}
        span.formfield
        {
                background-color: #ededee;
                padding: 0px 0px 0px 0px;
                margin:0px 0px 0px 3px;
                background: transparent url(/resources/img/bg/forms/input_right.png) no-repeat top right;
                display: inline-block;
                width:405px !important;
        }

    </style>
    <![endif]-->
    <!--[if lt IE 8]>
        <style type="text/css">
            span.formfield{
                 background-position: right 1px !important;
            }

            span.formfield select{
                background-color: #ededee;
            }


        </style>
    <![endif]-->
    <!--[if IE 8]>
        <style type="text/css">
            span.formfield input[type="text"], span.formfield input[type="password"], span.formfield select{
                 font-size:17px !important;
            }
        </style>
    <![endif]-->

</head>
<body>
    <form name="aspnetForm" method="post" action="credit.aspx" id="aspnetForm">
<div>
<input type="hidden" name="__EVENTTARGET" id="__EVENTTARGET" value="" />
<input type="hidden" name="__EVENTARGUMENT" id="__EVENTARGUMENT" value="" />
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwULLTIwMDQ5ODAzNjUPZBYCZg9kFgQCAQ9kFgICCQ9kFggCCQ8WAh4EVGV4dAUBMGQCCw8WAh8ABQEwZAINDxYCHwAFATJkAg8PFgIfAAUBMGQCAw9kFgYCAQ8WAh8ABd4BPGRpdiBjbGFzcz0ibWVudSI+PHNwYW4gaWQ9Im1lbnVfdGFyaWV2ZW4iPjxhIGhyZWY9Imh0dHA6Ly93d3cuc2ltcGVsLm5sL1RhcmlldmVuLmFzcHgiIHRhcmdldD0iX2JsYW5rIj50YXJpZXZlbjwvYT48L3NwYW4+PHNwYW4gaWQ9Im1lbnVfZmFxIj48YSBocmVmPSJodHRwOi8vd3d3LnNpbXBlbC5ubC9mYXEuYXNweCIgdGFyZ2V0PSJfYmxhbmsiPnZyYWdlbjwvYT48L3NwYW4+PC9kaXY+ZAIFDxYCHwAFvwY8dWwgY2xhc3M9Im1lbnUiPjxsaT48YSBpZD0iaG9tZSIgaHJlZj0iL2xhbmRpbmcuYXNweCI+aG9tZTwvYT48L2xpPjxsaT48YSBpZD0iYWNjb3VudCIgaHJlZj0iL2FjY291bnQuYXNweCI+bWlqbiBnZWdldmVuczwvYT48L2xpPjxsaT48YSBpZD0ic2ltcHJvcGVydGllcyIgaHJlZj0iL3NpbXByb3BlcnRpZXMuYXNweCI+Z2VnZXZlbnMgYWJvbm5lbWVudDwvYT48L2xpPjxsaT48YSBpZD0idXBncmFkZSIgaHJlZj0iL3VwZ3JhZGUuYXNweCI+d2lqemlnIGFib25uZW1lbnQ8L2E+PC9saT48bGk+PGEgaWQ9ImJlbHBsYWZvbmQiIGhyZWY9Ii9iZWxwbGFmb25kLmFzcHgiPnBsYWZvbmQ8L2E+PC9saT48bGk+PGEgaWQ9Imludm9pY2VzIiBocmVmPSIvaW52b2ljZXMuYXNweCI+ZmFjdHVyZW48L2E+PC9saT48bGk+PGEgaWQ9ImNhbGxfZGV0YWlscyIgaHJlZj0iL3JlcXVlc3Rfc3BlY2lmaWNhdGlvbnMuYXNweCI+YmVsc3BlY2lmaWNhdGllPC9hPjwvbGk+PGxpPjxhIGlkPSJjcmVkaXQiIGhyZWY9Ii9jcmVkaXQuYXNweCI+YWN0dWVlbCB2ZXJicnVpazwvYT48L2xpPjxsaT48YSBpZD0iY2hhbmdlX3Bhc3N3b3JkIiBocmVmPSIvcGFzc3dvcmRfZWRpdC5hc3B4Ij53aWp6aWcgd2FjaHR3b29yZDwvYT48L2xpPjxsaT48YSBpZD0iYmxvY2siIGhyZWY9Ii9ibG9jay5hc3B4Ij5ibG9ra2VlciBudW1tZXI8L2E+PC9saT48bGk+PGEgaWQ9InNpbXN3YXAiIGhyZWY9Ii9TaW1Td2FwLmFzcHgiPnZlcnZhbmdlbmRlIFNpbWthYXJ0PC9hPjwvbGk+PGxpPjxhIGlkPSJjb250YWN0IiBocmVmPSIvY29udGFjdC5hc3B4Ij5zdGVsIGplIHZyYWFnPC9hPjwvbGk+PC91bD5kAgcPZBYEAgEPFgIfAAUKMDYyMzQyMjQ5MWQCBw8PFgIfAAXvCDxkaXYgY2xhc3M9ImJhcl9pdGVtIj4gICAgPHNwYW4gc3R5bGU9ImZvbnQtc2l6ZTogMTVweDsiPkJlbG1pbnV0ZW4gaW4gamUgYnVuZGVsPC9zcGFuPjxiciAvPiAgICA8YnIgLz4gICAgPGRpdiBjbGFzcz0iYmFyX2xvYWQiIGlkPSJiZWxsZW4iPiAgICAgICAgPGRpdiBjbGFzcz0icHJvZ3Jlc3MtbGFiZWwiPjxzcGFuPjAgbWludXRlbiB2ZXJicnVpa3Q8L3NwYW4+PC9kaXY+ICAgIDwvZGl2PiAgICA8ZGl2IGNsYXNzPSJiYXJfZGVzYyI+ICAgICAgICA8c3BhbiBzdHlsZT0iZmxvYXQ6IGxlZnQiPjA8L3NwYW4+ICAgICAgICA8c3BhbiBzdHlsZT0iZmxvYXQ6IHJpZ2h0Ij4xMDAwMCBtaW51dGVuPC9zcGFuPiAgICA8L2Rpdj48L2Rpdj4gPGJyIC8+IDxiciAvPiA8YnIgLz48ZGl2IGNsYXNzPSJiYXJfaXRlbSI+ICAgIDxzcGFuIHN0eWxlPSJmb250LXNpemU6IDE1cHg7Ij5TbXPigJlqZXMgaW4gamUgYnVuZGVsPC9zcGFuPjxiciAvPiAgICA8YnIgLz4gICAgPGRpdiBjbGFzcz0iYmFyX2xvYWQiIGlkPSJzbXMiPiAgICAgICAgPGRpdiBjbGFzcz0icHJvZ3Jlc3MtbGFiZWwiPjxzcGFuPjUgU01TJ2plcyB2ZXJicnVpa3Q8L3NwYW4+PC9kaXY+ICAgIDwvZGl2PiAgICA8ZGl2IGNsYXNzPSJiYXJfZGVzYyI+ICAgICAgICA8c3BhbiBzdHlsZT0iZmxvYXQ6IGxlZnQiPjA8L3NwYW4+ICAgICAgICA8c3BhbiBzdHlsZT0iZmxvYXQ6IHJpZ2h0Ij4xMDAwMCBTTVM8L3NwYW4+ICAgIDwvZGl2PjwvZGl2PiA8YnIgLz4gPGJyIC8+IDxiciAvPjxkaXYgY2xhc3M9ImJhcl9pdGVtIj4gICAgPHNwYW4gc3R5bGU9ImZvbnQtc2l6ZTogMTVweDsiPk1C4oCZcyBpbiBqZSBidW5kZWw8L3NwYW4+PGJyIC8+ICAgIDxiciAvPiAgICA8ZGl2IGNsYXNzPSJiYXJfbG9hZCIgaWQ9ImludGVybmV0Ij4gICAgICAgIDxkaXYgY2xhc3M9InByb2dyZXNzLWxhYmVsIj48c3Bhbj4xNyBNQiB2ZXJicnVpa3Q8L3NwYW4+PC9kaXY+ICAgIDwvZGl2PiAgICA8ZGl2IGNsYXNzPSJiYXJfZGVzYyI+ICAgICAgICA8c3BhbiBzdHlsZT0iZmxvYXQ6IGxlZnQiPjA8L3NwYW4+ICAgICAgICA8c3BhbiBzdHlsZT0iZmxvYXQ6IHJpZ2h0Ij4xMDAwIE1CPC9zcGFuPiAgICA8L2Rpdj48L2Rpdj4gPGJyIC8+IDxiciAvPiA8YnIgLz5kZGTBlxSBdS9Rjej4l3rGesoMkwKc0w==" />
</div>

<script type="text/javascript">
//<![CDATA[
var theForm = document.forms['aspnetForm'];
if (!theForm) {
    theForm = document.aspnetForm;
}
function __doPostBack(eventTarget, eventArgument) {
    if (!theForm.onsubmit || (theForm.onsubmit() != false)) {
        theForm.__EVENTTARGET.value = eventTarget;
        theForm.__EVENTARGUMENT.value = eventArgument;
        theForm.submit();
    }
}
//]]>
</script>


<div>

        <input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="69551C16" />
        <input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="/wEWAgKhyfWJBgLHjbmPC3rYQ4hBwg8ge8iw8ebE5njvVqP5" />
</div>
    <div class="container">
                <div class="header">
                        <img src="/resources/img/logo/simpellogo.png" alt="simpel" id="simpellogo" />
                        <div class="menu"><span id="menu_tarieven"><a href="http://www.simpel.nl/Tarieven.aspx" target="_blank">tarieven</a></span><span id="menu_faq"><a href="http://www.simpel.nl/faq.aspx" target="_blank">vragen</a></span></div>
                </div>

        <div class="contentcontainer">
            <div class="content errorbox" id="error">
                <div class="errorcontent">
                </div>
                <a href="#" class="close">x</a>
            </div>
            <div class="content" id="content">
                <div class="menucontainer">


                    <ul class="menu"><li><a id="home" href="/landing.aspx">home</a></li><li><a id="account" href="/account.aspx">mijn gegevens</a></li><li><a id="simproperties" href="/simproperties.aspx">gegevens abonnement</a></li><li><a id="upgrade" href="/upgrade.aspx">wijzig abonnement</a></li><li><a id="belplafond" href="/belplafond.aspx">plafond</a></li><li><a id="invoices" href="/invoices.aspx">facturen</a></li><li><a id="call_details" href="/request_specifications.aspx">belspecificatie</a></li><li><a id="credit" href="/credit.aspx">actueel verbruik</a></li><li><a id="change_password" href="/password_edit.aspx">wijzig wachtwoord</a></li><li><a id="block" href="/block.aspx">blokkeer nummer</a></li><li><a id="simswap" href="/SimSwap.aspx">vervangende Simkaart</a></li><li><a id="contact" href="/contact.aspx">stel je vraag</a></li></ul>
                </div>

<div class="top_corner_nr">Mijn Simpel voor 0643472392</div>
    <h1>Actueel verbruik</h1>


        <p>Onderstaand overzicht geeft je actueel verbuik / tegoed binnen je bundels weer. Dit is altijd tot je laatste gebruik bijgewerkt.</p>
        <p>Een specificatie van je verbruik kun je inzien bij de <a href="request_specifications.aspx">Belspecificatie</a>.</p></br>

    <table>
        <span id="ctl00_content_litCreditLeftVoice"><div class="bar_item">    <span style="font-size: 15px;">Belminuten in je bundel</span><br />    <br />    <div class="bar_load" id="bellen">        <div class="progress-label"><span>0 minuten verbruikt</span></div>    </div>    <div class="bar_desc">        <span style="float: left">0</span>        <span style="float: right">10000 minuten</span>    </div></div> <br /> <br /> <br /><div class="bar_item">    <span style="font-size: 15px;">Sms’jes in je bundel</span><br />    <br />    <div class="bar_load" id="sms">        <div class="progress-label"><span>5 SMS'jes verbruikt</span></div>    </div>    <div class="bar_desc">        <span style="float: left">0</span>        <span style="float: right">10000 SMS</span>    </div></div> <br /> <br /> <br /><div class="bar_item">    <span style="font-size: 15px;">MB’s in je bundel</span><br />    <br />    <div class="bar_load" id="internet">        <div class="progress-label"><span>17 MB verbruikt</span></div>    </div>    <div class="bar_desc">        <span style="float: left">0</span>        <span style="float: right">1000 MB</span>    </div></div> <br /> <br /> <br /></span>
    </table>
    <br />


            </div>




            <div class="clear"></div>


             <div class="footer">
                            <span><a href="http://www.simpel.nl/contact.aspx" target="_blank">contact</a></span><span><a href="http://www.simpel.nl/privacyverklaring.aspx" target="_blank">privacyverklaring</a></span><span><a href="http://www.simpel.nl/Voorwaarden.aspx" target="_blank">voorwaarden</a></span>
                    </div>
                    <a id="ctl00_lbLogOut" class="login" href="javascript:__doPostBack('ctl00$lbLogOut','')">uitloggen</a>
        </div>
    </div>
    </form>
</body>
</html>
"""

data_login = """
<!DOCTYPE html>

<html>
<head><meta charset="utf-8" /><meta http-equiv="X-UA-Compatible" content="IE-edge,chrome=1" /><title>
        Login
</title><link href="/resources/css/defaults.css?v=002" rel="stylesheet" type="text/css" /><link href="/resources/css/master.css?v=002" rel="stylesheet" type="text/css" /><link href="/resources/css/cookiechecker.css?v=002" rel="stylesheet" type="text/css" />
    <!--[if lte IE 8]>
   <link href="/resources/css/cookiecheckerIE.css?v=002" rel="stylesheet" type="text/css" />
    <![endif]-->

    <script src="/resources/js/jquery-1.7.2.min.js" type="text/javascript"></script>
    <script src="/resources/js/jquery-ui-1.8.7.custom.min.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.corner.js" type="text/javascript"></script>
    <script src="/resources/js/prototypes.js" type="text/javascript"></script>
    <script src="/resources/js/validatie.js?v=003" type="text/javascript"></script>
    <script src="/resources/js/tooltip.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.tools.min.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.ui.datepicker-nl.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.reveal.cookie.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.reveal.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.reveal.contact.js" type="text/javascript"></script>
    <script src="/resources/js/cookiechecker.js" type="text/javascript"></script>
    <script src="/resources/js/checkiban.js" type="text/javascript"></script>

    <!-- Google Analyticsscript -->
    <script>(function (i, s, o, g, r, a, m) { i['GoogleAnalyticsObject'] = r; i[r] = i[r] || function () { (i[r].q = i[r].q || []).push(arguments) }, i[r].l = 1 * new Date(); a = s.createElement(o), m = s.getElementsByTagName(o)[0]; a.async = 1; a.src = g; m.parentNode.insertBefore(a, m) })(window, document, 'script', '//www.google-analytics.com/analytics.js', 'ga'); ga('create', 'UA-1956252-1', 'simpel.nl'); ga('send', 'pageview');</script>
    <!-- End Google Analyticsscript -->

    <script type="text/javascript">
        //<![CDATA[
        $(document).ready(function () {

                        $("form1").submit(function () {
                $(this).submit(function () {
                    return false;
                });
                return true;
            });


            doTooltip('.tooltiptarget');

            $(".tooltiptargetlink").tooltip({ position: 'left top', offset: [45, -15], effect: 'fade' });

            ValidateInitialize('select, input[type=checkbox], input[type=password], input[type=text]');
            $('.submit').bind('click', function (event) {
                if (!doValidateAll('select, input[type=checkbox], input[type=password], input[type=text]')) {
                    event.preventDefault();
                }
            });


            $('img#simpellogo').bind('click', function (event) {
                window.location.href = '/';
                event.preventDefault();
            });

            $('div.content').corner('10px');
            $('a.button').corner('5px');
            if ($.browser.msie && $.browser.version < 9) {
                $('.menu .selected').corner('4px');
            } else {
                $('.menu span, .menu li a').corner('4px');
            }

            $('.login').corner('5px bottom');

            $('table.classictable').each(function () {
                $(this).find('tr:even').addClass('alt');
            });
        });

        function getCookie(c_name) {
            var i, x, y, ARRcookies = document.cookie.split(";");
            for (i = 0; i < ARRcookies.length; i++) {
                x = ARRcookies[i].substr(0, ARRcookies[i].indexOf("="));
                y = ARRcookies[i].substr(ARRcookies[i].indexOf("=") + 1);
                x = x.replace(/^\s+|\s+$/g, "");
                if (x == c_name) {
                    return unescape(y);
                }
            }
        }

        //]]>
    </script>

    <style type="text/css">
        a
        {
             cursor:pointer !important;
        }
    </style>
    <script type="text/javascript">
        //<![CDATA[
        $(document).ready(function(){
            $('.forgotpasswordform').toggle();
            $('#error').toggle(false);

            //set usename field to be checked with 'name' rege
            $('#ctl00_content_txtLoginName').data('validation', 'none');
            //set password field to be checked with 'password' rege
            $('#ctl00_content_txtPassword').data('validation', 'password');

            //set tooltip for password field
                        $('#tooltip0').text('Je gebruikersnaam is niet veranderd. Je vindt je gebruikersnaam in de welkomstbrief of je kunt deze opvragen via de klantenservice.');

             message('#error', 3, false, '', '');

//             $('#ctl00_content_txtPassword, #ctl00_content_txtLoginName').bind('keydown keyup', function(event){
//                if(event.keyCode == 13){//if Enter is pressed
//                    if(doValidateAll('#login select, #login input[type=checkbox], #login input[type=password], #login input[type=text]')){
//                        __doPostBack('ctl00$content$lbSubmit','');
//                    }
//                }
//             });


             $('.submit').unbind().bind('click', function(event){
                if(!doValidateAll('#login select, #login input[type=checkbox], #login input[type=password], #login input[type=text]')){
                    event.preventDefault();
                }
             });

             $('.password').unbind().bind('click', function(event){
                if(!doValidateAll('#pass select, #pass input[type=checkbox], #pass input[type=password], #pass input[type=text]')){
                    event.preventDefault();
                }
             });


             $('.button').unbind().bind('click', function(event){
                 $('#ctl00_content_hdnLoginWW').val($('#ctl00_content_txtPassword').val());


             });
//            $('.linkshowforgotpasswordform').bind('click', function(event){
//                $('.forgotpasswordform').toggle();
//                event.preventDefault();
//             });

        });
        function passbox() {
               var input  =  document.getElementById('ctl00_content_txtPassword');
                var input2 = document.createElement('input');

            if(input.type == 'password'){
               with (input2){
                id = input.id;
                value = input.value;
                type = 'text';

                }
            }else{
            with (input2){
                id = input.id;
                value = input.value;
                type = 'password';
                }
          }


            return input.parentNode.replaceChild(input2,input);
            }

            function toggle_passbox() {
                if($('.linktoggle').text() == 'Toon wachtwoord' && $('#ctl00_content_txtPassword').val().length > 0)
                {
                    passbox();
                    $('.linktoggle').text('Verberg wachtwoord');
                }
                else if ($('.linktoggle').text() == 'Verberg wachtwoord' && $('#ctl00_content_txtPassword').val().length > 0){
                    passbox();
                     $('.linktoggle').text('Toon wachtwoord');
                }

                $('#ctl00_content_txtPassword').removeClass('invalid');
                if ($('#formpasswordval').hasClass('invalid'))
                {

                    $('#ctl00_content_txtPassword').addClass('invalid');

                }

                 $('#ctl00_content_txtPassword').removeClass('valid');
                if ($('#formpasswordval').hasClass('valid'))
                {

                    $('#ctl00_content_txtPassword').addClass('valid');

                }

             }
        //]]>
    </script>

    <!--[if IE 7]>
    <link rel="stylesheet" type="text/css" href="/static/css/IE7.css" />
    <style type="text/css">
        .showpassword {float:right; !important; margin-top:-20px;}
        .showpassword2 {witdh:220px;}
        span.formfield
        {
                background-color: #ededee;
                padding: 0px 0px 0px 0px;
                margin:0px 0px 0px 3px;
                background: transparent url(/resources/img/bg/forms/input_right.png) no-repeat top right;
                display: inline-block;
                width:405px !important;
        }

    </style>
    <![endif]-->
    <!--[if lt IE 8]>
        <style type="text/css">
            span.formfield{
                 background-position: right 1px !important;
            }

            span.formfield select{
                background-color: #ededee;
            }


        </style>
    <![endif]-->
    <!--[if IE 8]>
        <style type="text/css">
            span.formfield input[type="text"], span.formfield input[type="password"], span.formfield select{
                 font-size:17px !important;
            }
        </style>
    <![endif]-->

</head>
<body>
    <form name="aspnetForm" method="post" action="login.aspx" id="aspnetForm">
<div>
<input type="hidden" name="__EVENTTARGET" id="__EVENTTARGET" value="" />
<input type="hidden" name="__EVENTARGUMENT" id="__EVENTARGUMENT" value="" />
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwULLTE5MDIyMTM1OTQPZBYCZg9kFgICAw9kFggCAQ8WAh4EVGV4dAXeATxkaXYgY2xhc3M9Im1lbnUiPjxzcGFuIGlkPSJtZW51X3RhcmlldmVuIj48YSBocmVmPSJodHRwOi8vd3d3LnNpbXBlbC5ubC9UYXJpZXZlbi5hc3B4IiB0YXJnZXQ9Il9ibGFuayI+dGFyaWV2ZW48L2E+PC9zcGFuPjxzcGFuIGlkPSJtZW51X2ZhcSI+PGEgaHJlZj0iaHR0cDovL3d3dy5zaW1wZWwubmwvZmFxLmFzcHgiIHRhcmdldD0iX2JsYW5rIj52cmFnZW48L2E+PC9zcGFuPjwvZGl2PmQCBQ8WAh8AZWQCBw9kFgQCCQ8WAh8ABecBPHRkIGNsYXNzPSJ0ZDQiPjxpbWcgc3JjPSIvcmVzb3VyY2VzL2ltZy9taXNjL3Rvb2x0aXAucG5nIiBjbGFzcz0idG9vbHRpcHRhcmdldGxpbmsiIHRpdGxlPSJCZW4gamUgamUgZ2VicnVpa2Vyc25hYW0gdmVyZ2V0ZW4/IDxhIGhyZWY9aHR0cHM6Ly93d3cubWlqbnNpbXBlbC5ubC9yZXF1ZXN0X3VzZXJuYW1lLmFzcHg+S2xpayBkYW4gaGllcjwvYT4gb20gZGV6ZSBvcCB0ZSB2cmFnZW4uIiAvPjwvdGQ+ZAIPDxYCHwAFtAI8dGQgY2xhc3M9InRkNCI+PGltZyBzcmM9Ii9yZXNvdXJjZXMvaW1nL21pc2MvdG9vbHRpcC5wbmciIGNsYXNzPSJ0b29sdGlwdGFyZ2V0bGluayIgdGl0bGU9IkxldCBvcDogSmUga3VudCBoaWVyIG5pZXQgaW5sb2dnZW4gbWV0IGRlIGNvZGUgZGllIGplIHBlciBlLW1haWwgdmFuIG9ucyBoZWJ0IG9udHZhbmdlbi4gR2EgbmFhciA8YSBocmVmPWh0dHBzOi8vd3d3Lm1pam5zaW1wZWwubmwvd2FjaHR3b29yZC5hc3B4Pnd3dy5taWpuc2ltcGVsLm5sL3dhY2h0d29vcmQ8L2E+IGVuIG1hYWsgZWVuIHdhY2h0d29vcmQgYWFuLiIgLz48L3RkPmQCCw8PFgIeB1Zpc2libGVoZGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFGWN0bDAwJGNvbnRlbnQkY2hrUmVtZW1iZXIiAtwewvJHfbs3afCcHK6ltF2ULg==" />
</div>

<script type="text/javascript">
//<![CDATA[
var theForm = document.forms['aspnetForm'];
if (!theForm) {
    theForm = document.aspnetForm;
}
function __doPostBack(eventTarget, eventArgument) {
    if (!theForm.onsubmit || (theForm.onsubmit() != false)) {
        theForm.__EVENTTARGET.value = eventTarget;
        theForm.__EVENTARGUMENT.value = eventArgument;
        theForm.submit();
    }
}
//]]>
</script>


<div>

        <input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="C2EE9ABB" />
        <input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="/wEWBgK//L6QCAKclevVBgLaptSZDAKekIsoAo+D3Z0LArOJ2fsBv++E9+O/tQVgPxcFm4ZRqT9uu/c=" />
</div>
    <div class="container">
                <div class="header">
                        <img src="/resources/img/logo/simpellogo.png" alt="simpel" id="simpellogo" />
                        <div class="menu"><span id="menu_tarieven"><a href="http://www.simpel.nl/Tarieven.aspx" target="_blank">tarieven</a></span><span id="menu_faq"><a href="http://www.simpel.nl/faq.aspx" target="_blank">vragen</a></span></div>
                </div>

        <div class="contentcontainer">
            <div class="content errorbox" id="error">
                <div class="errorcontent">
                </div>
                <a href="#" class="close">x</a>
            </div>
            <div class="content" id="content">
                <div class="menucontainer">



                </div>

    <h1>Inloggen op Mijn Simpel</h1>
    <p></p>
    <table id="login">
        <tr>
            <td class="td0">Gebruikersnaam</td>
            <td class="td1" colspan="3"><span class="formfield formfieldie7"><input name="ctl00$content$txtLoginName" type="text" id="ctl00_content_txtLoginName" validation="text" validationname="" /></span></td>

            <td class="td4"><img src="/resources/img/misc/tooltip.png" class="tooltiptargetlink" title="Ben je je gebruikersnaam vergeten? <a href=https://www.mijnsimpel.nl/request_username.aspx>Klik dan hier</a> om deze op te vragen." /></td>
        </tr>
        <tr>
            <td class="td0">Wachtwoord</td>
            <td class="td1" colspan="3"><span class="formfield" id="formpasswordval"><input name="ctl00$content$txtPassword" type="password" id="ctl00_content_txtPassword" validation="text" validationname="" /></span></td>

           <td class="td4"><img src="/resources/img/misc/tooltip.png" class="tooltiptargetlink" title="Let op: Je kunt hier niet inloggen met de code die je per e-mail van ons hebt ontvangen. Ga naar <a href=https://www.mijnsimpel.nl/wachtwoord.aspx>www.mijnsimpel.nl/wachtwoord</a> en maak een wachtwoord aan." /></td>
        </tr>
        <tr>
            <td class="td0">Onthoud mij</td>
            <td class="td1" colspan="3"><span class="formfield nobg" style="width:50px;"><span optional="true" validationname="" style="display:inline-block;height:20px;width:50px;"><input id="ctl00_content_chkRemember" type="checkbox" name="ctl00$content$chkRemember" /></span></span><span class="showpassword"><a class="linktoggle" onclick="toggle_passbox()">Toon wachtwoord</a></span></td>


        </tr>


        <tr>
            <td class="td0"><a class="linkshowforgotpasswordform" href="/request_username.aspx">Gebruikersnaam opvragen?</a></td>
        </tr>
        <tr>
            <td class="td0"><a class="linkshowforgotpasswordform" href="/requestTempPassword.aspx">Wachtwoord vergeten?</a></td>
        </tr>
        <tr>
            <td class="td0"><a href="https://www.simpel.nl/static/pdf/Inlogprocedure.pdf" target="_blank" class="login_explained" onmouseover="$(this).html('Hulp nodig met inloggen? Klik hier voor een uitgebreid stappenplan');" onmouseout="$(this).html('uitleg');">uitleg</a></td>
        </tr>


    </table>
    <a id="ctl00_content_lbSubmit" class="button" href="javascript:__doPostBack('ctl00$content$lbSubmit','')">Login</a>
    <hr />


   <input type="hidden" name="ctl00$content$hdnLoginWW" id="ctl00_content_hdnLoginWW" />


            </div>




            <div class="clear"></div>


             <div class="footer">
                            <span><a href="http://www.simpel.nl/contact.aspx" target="_blank">contact</a></span><span><a href="http://www.simpel.nl/privacyverklaring.aspx" target="_blank">privacyverklaring</a></span><span><a href="http://www.simpel.nl/Voorwaarden.aspx" target="_blank">voorwaarden</a></span>
                    </div>

        </div>
    </div>
    </form>
</body>
</html>
"""

data_login_check = """

<!DOCTYPE html>

<html>
<head><meta charset="utf-8" /><meta http-equiv="X-UA-Compatible" content="IE-edge,chrome=1" /><title>
        Mijn Simpel
</title><link href="/resources/css/defaults.css?v=002" rel="stylesheet" type="text/css" /><link href="/resources/css/master.css?v=002" rel="stylesheet" type="text/css" /><link href="/resources/css/cookiechecker.css?v=002" rel="stylesheet" type="text/css" />
    <!--[if lte IE 8]>
   <link href="/resources/css/cookiecheckerIE.css?v=002" rel="stylesheet" type="text/css" />
    <![endif]-->

    <script src="/resources/js/jquery-1.7.2.min.js" type="text/javascript"></script>
    <script src="/resources/js/jquery-ui-1.8.7.custom.min.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.corner.js" type="text/javascript"></script>
    <script src="/resources/js/prototypes.js" type="text/javascript"></script>
    <script src="/resources/js/validatie.js?v=003" type="text/javascript"></script>
    <script src="/resources/js/tooltip.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.tools.min.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.ui.datepicker-nl.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.reveal.cookie.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.reveal.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.reveal.contact.js" type="text/javascript"></script>
    <script src="/resources/js/cookiechecker.js" type="text/javascript"></script>
    <script src="/resources/js/checkiban.js" type="text/javascript"></script>

    <!-- Google Analyticsscript -->
    <script>(function (i, s, o, g, r, a, m) { i['GoogleAnalyticsObject'] = r; i[r] = i[r] || function () { (i[r].q = i[r].q || []).push(arguments) }, i[r].l = 1 * new Date(); a = s.createElement(o), m = s.getElementsByTagName(o)[0]; a.async = 1; a.src = g; m.parentNode.insertBefore(a, m) })(window, document, 'script', '//www.google-analytics.com/analytics.js', 'ga'); ga('create', 'UA-1956252-1', 'simpel.nl'); ga('send', 'pageview');</script>
    <!-- End Google Analyticsscript -->

    <script type="text/javascript">
        //<![CDATA[
        $(document).ready(function () {

                        $("form1").submit(function () {
                $(this).submit(function () {
                    return false;
                });
                return true;
            });


            doTooltip('.tooltiptarget');

            $(".tooltiptargetlink").tooltip({ position: 'left top', offset: [45, -15], effect: 'fade' });

            ValidateInitialize('select, input[type=checkbox], input[type=password], input[type=text]');
            $('.submit').bind('click', function (event) {
                if (!doValidateAll('select, input[type=checkbox], input[type=password], input[type=text]')) {
                    event.preventDefault();
                }
            });


            $('img#simpellogo').bind('click', function (event) {
                window.location.href = '/';
                event.preventDefault();
            });

            $('div.content').corner('10px');
            $('a.button').corner('5px');
            if ($.browser.msie && $.browser.version < 9) {
                $('.menu .selected').corner('4px');
            } else {
                $('.menu span, .menu li a').corner('4px');
            }

            $('.login').corner('5px bottom');

            $('table.classictable').each(function () {
                $(this).find('tr:even').addClass('alt');
            });
        });

        function getCookie(c_name) {
            var i, x, y, ARRcookies = document.cookie.split(";");
            for (i = 0; i < ARRcookies.length; i++) {
                x = ARRcookies[i].substr(0, ARRcookies[i].indexOf("="));
                y = ARRcookies[i].substr(ARRcookies[i].indexOf("=") + 1);
                x = x.replace(/^\s+|\s+$/g, "");
                if (x == c_name) {
                    return unescape(y);
                }
            }
        }

        //]]>
    </script>

    <script type="text/javascript">
        //<![CDATA[
        $(document).ready(function(){
            message('#error', 3, false, '', '');
            $('#home').addClass('selected');
            $('#invoicetable').find('tbody tr td').not('.ctd5').bind('click', function(){
                window.location.href = '/invoices.aspx';
            });

            $('#invoicetable2').find('tbody tr td').not('.ctd5').bind('click', function(){
                window.location.href = '/invoices.aspx';
            });

            $('#invoicetable').find('tbody tr td.ctd5').bind('mouseenter', function(){
                $(this).parent('tr').addClass('nohover');
            }).bind('mouseleave', function(){
                $(this).parent('tr').removeClass('nohover');
            });

            $('#invoicetable2').find('tbody tr td.ctd5').bind('mouseenter', function(){
                $(this).parent('tr').addClass('nohover');
            }).bind('mouseleave', function(){
                $(this).parent('tr').removeClass('nohover');
            });
            //=========================================================
            //            $('.openinfolink').html('klik hier voor meer informatie');

            //            $('.openinfolink').click(function () {
            //               $(this).next().toggle();
            //            });
        });
        //]]>
    </script>
    <style type="text/css">
        .announcement {
            -moz-border-radius: 10px; /* Firefox */
            -webkit-border-radius: 10px; /* Safari, Chrome */
            border-radius: 10px 10px 10px 10px;
            border: 1px solid rgb(169, 57, 139);
            padding: 8px;
        }

        .announcementideal {
            -moz-border-radius: 10px; /* Firefox */
            -webkit-border-radius: 10px; /* Safari, Chrome */
            border-radius: 10px 10px 10px 10px;
            border: 1px solid rgb(169, 57, 139);
            padding: 4px 0px 4px 13px;
            width: 300px;
            margin-top: 15px;
        }

        div.content h3 {
            margin-bottom: 15px !important;
        }

        .openinfolink {
            text-decoration: underline;
            cursor: pointer;
            display: block;
            margin-left: 100px;
            color: #A9398B;
            width: 190px;
        }

            .openinfolink:hover {
                color: #000000;
            }

        .sub_content {
            background-color: #EDEDEE;
            width: 387px;
            display: block;
            margin-top: 10px;
            position: relative;
            margin: 19px 0 0 -142px;
        }

        .status_table {
            margin-left: 10px;
            width: 708px;
        }

            .status_table td {
                text-align: left;
                vertical-align: top;
            }

        .litmsisdn {
            width: 101px;
        }

        .invoicetd5 {
            padding-left: 12px;
        }

        .litreason {
            padding-left: 19px;
            width: 140px;
        }

        .ctd6 {
            padding-left: 17px;
        }
    </style>
        <script type="text/javascript" src="https://nowinteract-nowinteractnordi.netdna-ssl.com/imp3/simpel/imp_simpel.min.js"></script>

<script type="text/javascript">

 try {

IMP.initsite("nlsim160216pel","3");
IMP.trackInteract();
 }

catch (e) { }

</script>


    <!--[if IE 7]>
    <link rel="stylesheet" type="text/css" href="/static/css/IE7.css" />
    <style type="text/css">
        .showpassword {float:right; !important; margin-top:-20px;}
        .showpassword2 {witdh:220px;}
        span.formfield
        {
                background-color: #ededee;
                padding: 0px 0px 0px 0px;
                margin:0px 0px 0px 3px;
                background: transparent url(/resources/img/bg/forms/input_right.png) no-repeat top right;
                display: inline-block;
                width:405px !important;
        }

    </style>
    <![endif]-->
    <!--[if lt IE 8]>
        <style type="text/css">
            span.formfield{
                 background-position: right 1px !important;
            }

            span.formfield select{
                background-color: #ededee;
            }


        </style>
    <![endif]-->
    <!--[if IE 8]>
        <style type="text/css">
            span.formfield input[type="text"], span.formfield input[type="password"], span.formfield select{
                 font-size:17px !important;
            }
        </style>
    <![endif]-->

</head>
<body>
    <form name="aspnetForm" method="post" action="landing.aspx" id="aspnetForm">
<div>
<input type="hidden" name="__EVENTTARGET" id="__EVENTTARGET" value="" />
<input type="hidden" name="__EVENTARGUMENT" id="__EVENTARGUMENT" value="" />
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwULLTE2NDQxNDM0MDIPZBYCZg9kFgICAw9kFgYCAQ8WAh4EVGV4dAXeATxkaXYgY2xhc3M9Im1lbnUiPjxzcGFuIGlkPSJtZW51X3RhcmlldmVuIj48YSBocmVmPSJodHRwOi8vd3d3LnNpbXBlbC5ubC9UYXJpZXZlbi5hc3B4IiB0YXJnZXQ9Il9ibGFuayI+dGFyaWV2ZW48L2E+PC9zcGFuPjxzcGFuIGlkPSJtZW51X2ZhcSI+PGEgaHJlZj0iaHR0cDovL3d3dy5zaW1wZWwubmwvZmFxLmFzcHgiIHRhcmdldD0iX2JsYW5rIj52cmFnZW48L2E+PC9zcGFuPjwvZGl2PmQCBQ8WAh8ABb8GPHVsIGNsYXNzPSJtZW51Ij48bGk+PGEgaWQ9ImhvbWUiIGhyZWY9Ii9sYW5kaW5nLmFzcHgiPmhvbWU8L2E+PC9saT48bGk+PGEgaWQ9ImFjY291bnQiIGhyZWY9Ii9hY2NvdW50LmFzcHgiPm1pam4gZ2VnZXZlbnM8L2E+PC9saT48bGk+PGEgaWQ9InNpbXByb3BlcnRpZXMiIGhyZWY9Ii9zaW1wcm9wZXJ0aWVzLmFzcHgiPmdlZ2V2ZW5zIGFib25uZW1lbnQ8L2E+PC9saT48bGk+PGEgaWQ9InVwZ3JhZGUiIGhyZWY9Ii91cGdyYWRlLmFzcHgiPndpanppZyBhYm9ubmVtZW50PC9hPjwvbGk+PGxpPjxhIGlkPSJiZWxwbGFmb25kIiBocmVmPSIvYmVscGxhZm9uZC5hc3B4Ij5wbGFmb25kPC9hPjwvbGk+PGxpPjxhIGlkPSJpbnZvaWNlcyIgaHJlZj0iL2ludm9pY2VzLmFzcHgiPmZhY3R1cmVuPC9hPjwvbGk+PGxpPjxhIGlkPSJjYWxsX2RldGFpbHMiIGhyZWY9Ii9yZXF1ZXN0X3NwZWNpZmljYXRpb25zLmFzcHgiPmJlbHNwZWNpZmljYXRpZTwvYT48L2xpPjxsaT48YSBpZD0iY3JlZGl0IiBocmVmPSIvY3JlZGl0LmFzcHgiPmFjdHVlZWwgdmVyYnJ1aWs8L2E+PC9saT48bGk+PGEgaWQ9ImNoYW5nZV9wYXNzd29yZCIgaHJlZj0iL3Bhc3N3b3JkX2VkaXQuYXNweCI+d2lqemlnIHdhY2h0d29vcmQ8L2E+PC9saT48bGk+PGEgaWQ9ImJsb2NrIiBocmVmPSIvYmxvY2suYXNweCI+Ymxva2tlZXIgbnVtbWVyPC9hPjwvbGk+PGxpPjxhIGlkPSJzaW1zd2FwIiBocmVmPSIvU2ltU3dhcC5hc3B4Ij52ZXJ2YW5nZW5kZSBTaW1rYWFydDwvYT48L2xpPjxsaT48YSBpZD0iY29udGFjdCIgaHJlZj0iL2NvbnRhY3QuYXNweCI+c3RlbCBqZSB2cmFhZzwvYT48L2xpPjwvdWw+ZAIHD2QWCgIFD2QWAmYPFgIfAGVkAgcPZBYCZg8WAh8AZWQCCQ8WAh8ABQxKLkcuIFJ1YmluZ2hkAg0PZBYEAgIPFgIeB1Zpc2libGVnFgYCAw8WAh8ABQJKYWQCBQ8WAh8BZxYCAgMPFgIfAAUVTnVtbWVyYmVob3VkIGFmZ2Vyb25kZAIGDxYCHwFnFgICAQ8WAh8ABRAyOSBmZWJydWFyaSAyMDE2ZAIDDxYCHwFoFgICBQ8WAh8AZWQCDw8WAh8BaBYCAgIPFgIfAWhkZFoTPQC3S0NrGlX40XtHKnc0wNq8" />
</div>

<script type="text/javascript">
//<![CDATA[
var theForm = document.forms['aspnetForm'];
if (!theForm) {
    theForm = document.aspnetForm;
}
function __doPostBack(eventTarget, eventArgument) {
    if (!theForm.onsubmit || (theForm.onsubmit() != false)) {
        theForm.__EVENTTARGET.value = eventTarget;
        theForm.__EVENTARGUMENT.value = eventArgument;
        theForm.submit();
    }
}
//]]>
</script>


<div>

        <input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="318D363F" />
        <input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="/wEWAgKNtN/zBALHjbmPC0exwhLgcZF1rVrfWHoWQuV0lHF9" />
</div>
    <div class="container">
                <div class="header">
                        <img src="/resources/img/logo/simpellogo.png" alt="simpel" id="simpellogo" />
                        <div class="menu"><span id="menu_tarieven"><a href="http://www.simpel.nl/Tarieven.aspx" target="_blank">tarieven</a></span><span id="menu_faq"><a href="http://www.simpel.nl/faq.aspx" target="_blank">vragen</a></span></div>
                </div>

        <div class="contentcontainer">
            <div class="content errorbox" id="error">
                <div class="errorcontent">
                </div>
                <a href="#" class="close">x</a>
            </div>
            <div class="content" id="content">
                <div class="menucontainer">


                    <ul class="menu"><li><a id="home" href="/landing.aspx">home</a></li><li><a id="account" href="/account.aspx">mijn gegevens</a></li><li><a id="simproperties" href="/simproperties.aspx">gegevens abonnement</a></li><li><a id="upgrade" href="/upgrade.aspx">wijzig abonnement</a></li><li><a id="belplafond" href="/belplafond.aspx">plafond</a></li><li><a id="invoices" href="/invoices.aspx">facturen</a></li><li><a id="call_details" href="/request_specifications.aspx">belspecificatie</a></li><li><a id="credit" href="/credit.aspx">actueel verbruik</a></li><li><a id="change_password" href="/password_edit.aspx">wijzig wachtwoord</a></li><li><a id="block" href="/block.aspx">blokkeer nummer</a></li><li><a id="simswap" href="/SimSwap.aspx">vervangende Simkaart</a></li><li><a id="contact" href="/contact.aspx">stel je vraag</a></li></ul>
                </div>

                <script type="text/javascript">
            var axel = Math.random() + "";
            var a = axel * 10000000000000;
            document.write('<iframe src="https://4979363.fls.doubleclick.net/activityi;src=4979363;type=mijns0;cat=mijns0;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;ord=' + a + '?" width="1" height="1" frameborder="0" style="display:none"></iframe>');
        </script>
        <noscript>
        <iframe src="https://4979363.fls.doubleclick.net/activityi;src=4979363;type=mijns0;cat=mijns0;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;ord=1?" width="1" height="1" frameborder="0" style="display:none"></iframe>
        </noscript>
    <h1>
        Home</h1>



    <p>Welkom <strong>
        Yoshie Master</strong>,</p>
    <p>
        Welkom op je persoonlijke ‘Mijn Simpel’ pagina. Je kunt hier je gegevens bekijken en wijzigen.<br />
        Na ongeveer 15 minuten zijn je wijzigingen doorgevoerd.
    </p>

    <div style="margin-left: -10px;">


            <h2 style="padding-top: 10px; margin-left: 10px;">Status abonnement</h2>

                <table style="margin-left: 10px; width: 688px;">
                    <tr>
                        <td style="width: 119px;">
                            <h3>Nummerbehoud aangevraagd:</h3></td>
                        <td style="width: 161px;">
                            Ja</td>
                        <td>&nbsp;</td>
                        <td>&nbsp;</td>
                    </tr>

                        <tr>
                            <td style="width: 119px;">
                                <h3>Status/Reden Nummerbehoud:</h3></td>
                            <td colspan="2">
                                Nummerbehoud afgerond</td>
                            <td>&nbsp;</td>
                            <td>&nbsp;</td>
                        </tr>

                        <tr>
                            <td style="width: 119px;">
                                <h3>Datum uitvoering nummerbehoud:</h3>
                            </td>
                            <td style="width: 161px;">
                                29 februari 2016</td>
                            <td>&nbsp;</td>
                            <td>&nbsp;</td>
                        </tr>

                </table>



    </div>

    <script src="https://www.wtp101.com/pixel?id=4754" type="text/javascript"></script>

            </div>




            <div class="clear"></div>


             <div class="footer">
                            <span><a href="http://www.simpel.nl/contact.aspx" target="_blank">contact</a></span><span><a href="http://www.simpel.nl/privacyverklaring.aspx" target="_blank">privacyverklaring</a></span><span><a href="http://www.simpel.nl/Voorwaarden.aspx" target="_blank">voorwaarden</a></span>
                    </div>
                    <a id="ctl00_lbLogOut" class="login" href="javascript:__doPostBack('ctl00$lbLogOut','')">uitloggen</a>
        </div>
    </div>
    </form>
</body>
</html>
"""

data_account = """


<!DOCTYPE html>

<html>
<head><meta charset="utf-8" /><meta http-equiv="X-UA-Compatible" content="IE-edge,chrome=1" /><title>
        Mijn Simpel
</title><link href="/resources/css/defaults.css?v=002" rel="stylesheet" type="text/css" /><link href="/resources/css/master.css?v=002" rel="stylesheet" type="text/css" /><link href="/resources/css/cookiechecker.css?v=002" rel="stylesheet" type="text/css" />
    <!--[if lte IE 8]>
   <link href="/resources/css/cookiecheckerIE.css?v=002" rel="stylesheet" type="text/css" />
    <![endif]-->

    <script src="/resources/js/jquery-1.7.2.min.js" type="text/javascript"></script>
    <script src="/resources/js/jquery-ui-1.8.7.custom.min.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.corner.js" type="text/javascript"></script>
    <script src="/resources/js/prototypes.js" type="text/javascript"></script>
    <script src="/resources/js/validatie.js?v=003" type="text/javascript"></script>
    <script src="/resources/js/tooltip.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.tools.min.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.ui.datepicker-nl.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.reveal.cookie.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.reveal.js" type="text/javascript"></script>
    <script src="/resources/js/jquery.reveal.contact.js" type="text/javascript"></script>
    <script src="/resources/js/cookiechecker.js" type="text/javascript"></script>
    <script src="/resources/js/checkiban.js" type="text/javascript"></script>

    <!-- Google Analyticsscript -->
    <script>(function (i, s, o, g, r, a, m) { i['GoogleAnalyticsObject'] = r; i[r] = i[r] || function () { (i[r].q = i[r].q || []).push(arguments) }, i[r].l = 1 * new Date(); a = s.createElement(o), m = s.getElementsByTagName(o)[0]; a.async = 1; a.src = g; m.parentNode.insertBefore(a, m) })(window, document, 'script', '//www.google-analytics.com/analytics.js', 'ga'); ga('create', 'UA-1956252-1', 'simpel.nl'); ga('send', 'pageview');</script>
    <!-- End Google Analyticsscript -->

    <script type="text/javascript">
        //<![CDATA[
        $(document).ready(function () {

                        $("form1").submit(function () {
                $(this).submit(function () {
                    return false;
                });
                return true;
            });


            doTooltip('.tooltiptarget');

            $(".tooltiptargetlink").tooltip({ position: 'left top', offset: [45, -15], effect: 'fade' });

            ValidateInitialize('select, input[type=checkbox], input[type=password], input[type=text]');
            $('.submit').bind('click', function (event) {
                if (!doValidateAll('select, input[type=checkbox], input[type=password], input[type=text]')) {
                    event.preventDefault();
                }
            });


            $('img#simpellogo').bind('click', function (event) {
                window.location.href = '/';
                event.preventDefault();
            });

            $('div.content').corner('10px');
            $('a.button').corner('5px');
            if ($.browser.msie && $.browser.version < 9) {
                $('.menu .selected').corner('4px');
            } else {
                $('.menu span, .menu li a').corner('4px');
            }

            $('.login').corner('5px bottom');

            $('table.classictable').each(function () {
                $(this).find('tr:even').addClass('alt');
            });
        });

        function getCookie(c_name) {
            var i, x, y, ARRcookies = document.cookie.split(";");
            for (i = 0; i < ARRcookies.length; i++) {
                x = ARRcookies[i].substr(0, ARRcookies[i].indexOf("="));
                y = ARRcookies[i].substr(ARRcookies[i].indexOf("=") + 1);
                x = x.replace(/^\s+|\s+$/g, "");
                if (x == c_name) {
                    return unescape(y);
                }
            }
        }

        //]]>
    </script>

    <script type="text/javascript">
        //<![CDATA[
        $(document).ready(function(){
             message('#error', 3, false, '', '');
             $('#account').addClass('selected');
        });
        //]]>
    </script>

    <!--[if IE 7]>
    <link rel="stylesheet" type="text/css" href="/static/css/IE7.css" />
    <style type="text/css">
        .showpassword {float:right; !important; margin-top:-20px;}
        .showpassword2 {witdh:220px;}
        span.formfield
        {
                background-color: #ededee;
                padding: 0px 0px 0px 0px;
                margin:0px 0px 0px 3px;
                background: transparent url(/resources/img/bg/forms/input_right.png) no-repeat top right;
                display: inline-block;
                width:405px !important;
        }

    </style>
    <![endif]-->
    <!--[if lt IE 8]>
        <style type="text/css">
            span.formfield{
                 background-position: right 1px !important;
            }

            span.formfield select{
                background-color: #ededee;
            }


        </style>
    <![endif]-->
    <!--[if IE 8]>
        <style type="text/css">
            span.formfield input[type="text"], span.formfield input[type="password"], span.formfield select{
                 font-size:17px !important;
            }
        </style>
    <![endif]-->

</head>
<body>
    <form name="aspnetForm" method="post" action="account.aspx" id="aspnetForm">
<div>
<input type="hidden" name="__EVENTTARGET" id="__EVENTTARGET" value="" />
<input type="hidden" name="__EVENTARGUMENT" id="__EVENTARGUMENT" value="" />
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwUJNjEyMDEzODQ0D2QWAmYPZBYCAgMPZBYGAgEPFgIeBFRleHQF3gE8ZGl2IGNsYXNzPSJtZW51Ij48c3BhbiBpZD0ibWVudV90YXJpZXZlbiI+PGEgaHJlZj0iaHR0cDovL3d3dy5zaW1wZWwubmwvVGFyaWV2ZW4uYXNweCIgdGFyZ2V0PSJfYmxhbmsiPnRhcmlldmVuPC9hPjwvc3Bhbj48c3BhbiBpZD0ibWVudV9mYXEiPjxhIGhyZWY9Imh0dHA6Ly93d3cuc2ltcGVsLm5sL2ZhcS5hc3B4IiB0YXJnZXQ9Il9ibGFuayI+dnJhZ2VuPC9hPjwvc3Bhbj48L2Rpdj5kAgUPFgIfAAW/Bjx1bCBjbGFzcz0ibWVudSI+PGxpPjxhIGlkPSJob21lIiBocmVmPSIvbGFuZGluZy5hc3B4Ij5ob21lPC9hPjwvbGk+PGxpPjxhIGlkPSJhY2NvdW50IiBocmVmPSIvYWNjb3VudC5hc3B4Ij5taWpuIGdlZ2V2ZW5zPC9hPjwvbGk+PGxpPjxhIGlkPSJzaW1wcm9wZXJ0aWVzIiBocmVmPSIvc2ltcHJvcGVydGllcy5hc3B4Ij5nZWdldmVucyBhYm9ubmVtZW50PC9hPjwvbGk+PGxpPjxhIGlkPSJ1cGdyYWRlIiBocmVmPSIvdXBncmFkZS5hc3B4Ij53aWp6aWcgYWJvbm5lbWVudDwvYT48L2xpPjxsaT48YSBpZD0iYmVscGxhZm9uZCIgaHJlZj0iL2JlbHBsYWZvbmQuYXNweCI+cGxhZm9uZDwvYT48L2xpPjxsaT48YSBpZD0iaW52b2ljZXMiIGhyZWY9Ii9pbnZvaWNlcy5hc3B4Ij5mYWN0dXJlbjwvYT48L2xpPjxsaT48YSBpZD0iY2FsbF9kZXRhaWxzIiBocmVmPSIvcmVxdWVzdF9zcGVjaWZpY2F0aW9ucy5hc3B4Ij5iZWxzcGVjaWZpY2F0aWU8L2E+PC9saT48bGk+PGEgaWQ9ImNyZWRpdCIgaHJlZj0iL2NyZWRpdC5hc3B4Ij5hY3R1ZWVsIHZlcmJydWlrPC9hPjwvbGk+PGxpPjxhIGlkPSJjaGFuZ2VfcGFzc3dvcmQiIGhyZWY9Ii9wYXNzd29yZF9lZGl0LmFzcHgiPndpanppZyB3YWNodHdvb3JkPC9hPjwvbGk+PGxpPjxhIGlkPSJibG9jayIgaHJlZj0iL2Jsb2NrLmFzcHgiPmJsb2trZWVyIG51bW1lcjwvYT48L2xpPjxsaT48YSBpZD0ic2ltc3dhcCIgaHJlZj0iL1NpbVN3YXAuYXNweCI+dmVydmFuZ2VuZGUgU2lta2FhcnQ8L2E+PC9saT48bGk+PGEgaWQ9ImNvbnRhY3QiIGhyZWY9Ii9jb250YWN0LmFzcHgiPnN0ZWwgamUgdnJhYWc8L2E+PC9saT48L3VsPmQCBw9kFhQCCQ8WAh8ABQY3NDk5NDJkAg8PFgIfAAUMSi5HLiBSdWJpbmdoZAIVDxYCHwAFFHNpbXBlbC5ubEB0aGV5b3NoLm5sZAIbDxYCHwAFDCszMTYyMzQyMjQ5MWQCIQ8WAh8ABQ1CcmVtc3RyYWF0IDgzZAInDxYCHwAFBjk3NDFFQmQCLQ8WAh8ABQlHUk9OSU5HRU5kAjUPFgIfAAUSTkwwOEFTTkIwNzA3MTcwNDAwZAI7DxYCHwAFB1JVQklOR0hkAkEPFgIfAAUVUzAwNzQ5OTQyMjAxNjAyMDYwMDAwZGQwa1FwfZwTV582Az5/uCNKbQnlww==" />
</div>

<script type="text/javascript">
//<![CDATA[
var theForm = document.forms['aspnetForm'];
if (!theForm) {
    theForm = document.aspnetForm;
}
function __doPostBack(eventTarget, eventArgument) {
    if (!theForm.onsubmit || (theForm.onsubmit() != false)) {
        theForm.__EVENTTARGET.value = eventTarget;
        theForm.__EVENTARGUMENT.value = eventArgument;
        theForm.submit();
    }
}
//]]>
</script>


<div>

        <input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="1D5EA448" />
        <input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="/wEWAwL/x/C+BQLlgvcBAseNuY8L/CszcZYQ8Mx0ZWKfTZsV9g8QwlM=" />
</div>
    <div class="container">
                <div class="header">
                        <img src="/resources/img/logo/simpellogo.png" alt="simpel" id="simpellogo" />
                        <div class="menu"><span id="menu_tarieven"><a href="http://www.simpel.nl/Tarieven.aspx" target="_blank">tarieven</a></span><span id="menu_faq"><a href="http://www.simpel.nl/faq.aspx" target="_blank">vragen</a></span></div>
                </div>

        <div class="contentcontainer">
            <div class="content errorbox" id="error">
                <div class="errorcontent">
                </div>
                <a href="#" class="close">x</a>
            </div>
            <div class="content" id="content">
                <div class="menucontainer">


                    <ul class="menu"><li><a id="home" href="/landing.aspx">home</a></li><li><a id="account" href="/account.aspx">mijn gegevens</a></li><li><a id="simproperties" href="/simproperties.aspx">gegevens abonnement</a></li><li><a id="upgrade" href="/upgrade.aspx">wijzig abonnement</a></li><li><a id="belplafond" href="/belplafond.aspx">plafond</a></li><li><a id="invoices" href="/invoices.aspx">facturen</a></li><li><a id="call_details" href="/request_specifications.aspx">belspecificatie</a></li><li><a id="credit" href="/credit.aspx">actueel verbruik</a></li><li><a id="change_password" href="/password_edit.aspx">wijzig wachtwoord</a></li><li><a id="block" href="/block.aspx">blokkeer nummer</a></li><li><a id="simswap" href="/SimSwap.aspx">vervangende Simkaart</a></li><li><a id="contact" href="/contact.aspx">stel je vraag</a></li></ul>
                </div>

    <h1>Mijn gegevens</h1>

    <h3>&nbsp;</h3>
    <table style="width:650px;">
        <tr>
            <td class="td0">Klantnummer</td>
            <td class="td1" colspan="3">842962</td>
            <td class="td4"></td>
        </tr>
        <tr>
            <td class="td0">Naam</td>
            <td class="td1" colspan="3">Yoshie Master</td>
            <td class="td4"></td>
        </tr>
        <tr>
            <td class="td0">E-mailadres</td>
            <td class="td1" colspan="3">some@email.adr</td>
            <td class="td4"></td>
        </tr>
        <tr>
            <td class="td0">Alternatief telefoonnummer</td>
            <td class="td1" colspan="3">+31643472392</td>
            <td class="td4"><img id="ctl00_content_imgContactTel" class="tooltiptarget" title="Op dit alternatieve telefoonnummer kan Simpel je bereiken, indien jouw Simpel nummer (nog) niet actief is." src="/resources/img/misc/tooltip.png" style="border-width:0px;" /></td>
        </tr>
    </table>
    <h3>&nbsp;</h3>
    <table>
        <tr>
            <td class="td0">Adres</td>
            <td class="td1" colspan="3">Een straat naam 5</td>
            <td class="td4"></td>
        </tr>
        <tr>
            <td class="td0">Postcode</td>
            <td class="td1" colspan="3">1234AB</td>
            <td class="td4"></td>
        </tr>
        <tr>
            <td class="td0">Woonplaats</td>
            <td class="td1" colspan="3">Stad</td>
            <td class="td4"></td>
        </tr>
    </table>


     <h3>&nbsp;</h3>
    <table>
        <tr>
            <td class="td0">IBAN / Rekeningnummer</td>
            <td class="td1" colspan="3">XY04ABCD53463234</td>
            <td class="td4"></td>
        </tr>
        <tr>
            <td class="td0">Ten name van</td>
            <td class="td1" colspan="3">Yoshie</td>
            <td class="td4"></td>
        </tr>
        <tr>
            <td class="td0">Kenmerk machtiging</td>
            <td class="td1" colspan="3">S3453634143452</td>
            <td class="td4"></td>
        </tr>
    </table>

    <a id="ctl00_content_lbEdit" class="button submit" href="javascript:__doPostBack('ctl00$content$lbEdit','')">Wijzig</a>

            </div>




            <div class="clear"></div>


             <div class="footer">
                            <span><a href="http://www.simpel.nl/contact.aspx" target="_blank">contact</a></span><span><a href="http://www.simpel.nl/privacyverklaring.aspx" target="_blank">privacyverklaring</a></span><span><a href="http://www.simpel.nl/Voorwaarden.aspx" target="_blank">voorwaarden</a></span>
                    </div>
                    <a id="ctl00_lbLogOut" class="login" href="javascript:__doPostBack('ctl00$lbLogOut','')">uitloggen</a>
        </div>
    </div>
    </form>
</body>
</html>

"""
