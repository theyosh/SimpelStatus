/*
  Copyright (C) 2013 Jolla Ltd.
  Contact: Thomas Perl <thomas.perl@jollamobile.com>
  All rights reserved.

  You may use this file under the terms of BSD license as follows:

  Redistribution and use in source and binary forms, with or without
  modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the Jolla Ltd nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
  ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
  WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
  DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDERS OR CONTRIBUTORS BE LIABLE FOR
  ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
  (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
  ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

import QtQuick 2.0
import Sailfish.Silica 1.0
import io.thp.pyotherside 1.4
import 'pages'
import 'cover'

ApplicationWindow
{
    property variant mobileData: QtObject {
        id: mobileDataObject

        property string username
        property string password

        property int data_update_timeout: 4

        property string mobilenumber: qsTr('Loading...')
        property string mobileplafond: qsTr('Loading...')

        property variant last_update: 0

        property variant call_usage: QtObject {
            property int total: 0
            property int used: 0
            property int free: 0
            property int percentage: 0
        }

        property variant sms_usage: QtObject {
            property int total: 0
            property int used: 0
            property int free: 0
            property int percentage: 0
        }

        property variant data_usage: QtObject {
            property int total: 0
            property int used: 0
            property int free: 0
            property int percentage: 0
        }

        property variant days_usage: QtObject {
            property int total: 0
            property int used: 0
            property int free: 0
            property int percentage: 0
        }

        property bool voicemail_active
        property string voicemail_pin
        property string voicemail_email

        property bool callforward_active
        property string callforward_direct
        property string callforward_busy

        property string history: qsTr('Loading...')

        property ListModel contractoptions: ListModel { }
        property ListModel accountoptions: ListModel { }
        property ListModel mobileoptions: ListModel { }
    }

    property bool dataLoading: true
    property bool __debug: false
    property string version: '0.2'

    id: statusApp
    initialPage: Component { Home {} }
    cover: Component { CoverPage {} }

    function debug(message) {
        if (statusApp.__debug){
          console.log('[' + Qt.formatDateTime(new Date(),'yyyy-MM-dd HH:mm:ss') + '] QML Debug: ' + message);
        }
    }

    // Function for showing a nice notification on top of the screen. Animation is about 6 seconds
    function notificationMessage(message) {
        if (statusApp.__debug){
          debug('notificationMessage: ' + message);
        }
        notificationText.text = message
        notificationAnimation.running = true
    }

    // Start loading animation
    function startLoader() {
        statusApp.dataLoading = true
    }

    // Stop loading animation
    function stopLoader() {
        statusApp.dataLoading = false
    }

    // Function for updating the data from other pages
    function updateMainData(force_update) {
        if (python.isLoggedIn()) {
            force_update = force_update ? force_update : false;
            python.updateData(force_update)
        } else {
            force_settings_page()
        }
    }

    function getMobileOptions() {
        return python.getEditOptions()
    }

    function saveMobileOptions() {
        python.saveOptions()
    }

    // Check if the needed credentials are availabe. If not, go to the settings screen
    function force_settings_page() {
        stopLoader()
        if (statusApp.pageStack.busy) {
            statusApp.pageStack.completeAnimation();
        }
        statusApp.pageStack.push(Qt.resolvedUrl('pages/Settings.qml'));
    }

    function saveSettings(username,password,data_update_timeout) {
        return python.saveSettings(username,password,data_update_timeout);
    }

    function resetSettings() {
        return python.resetSettings();
    }

    // Function for human readable bite sizes
    function byteSize(bytes) {
        var untis = ['B','KB','MB','GB']
        var indicator = ''
        var counter = 0
        if (bytes < 0) {
            indicator = '-'
            bytes *= -1
        }
        while (bytes / 1000 > 1) {
            counter++
            bytes = bytes / 1000
        }
        return indicator + bytes + '' + untis[counter]
    }

    Item {
        id: notificationPlaceHolder
        width: Screen.width
        height: 45
        opacity: 0
        anchors {
            top: Screen.top
            left: Screen.left
        }

        Rectangle {
            width: parent.width
            height: parent.height
            color: Theme.highlightColor
            opacity: 0.4
            anchors {
                top: parent.top
                left: parent.left
            }
        }
        Label {
            id: notificationText
            text: ''
            wrapMode: Text.WordWrap
            font.pixelSize: Theme.fontSizeSmall
            horizontalAlignment: Text.AlignHCenter
            width: parent.width
            height: parent.height
            anchors {
                top: parent.top
                left: parent.left
                topMargin: 1
                leftMargin: Theme.paddingSmall
                rightMargin: Theme.paddingSmall
            }
        }

        // this is a standalone animation, it's not running by default
        SequentialAnimation {
            id: notificationAnimation
            running: false
            PropertyAnimation { id: animationIn;   target: notificationPlaceHolder; property: 'opacity'; to: 1; duration: 2000 }
            PropertyAnimation { id: animationStay; target: notificationPlaceHolder; property: 'opacity'; to: 1; duration: 2000 }
            PropertyAnimation { id: animationOut;  target: notificationPlaceHolder; property: 'opacity'; to: 0; duration: 2000 }
        }
    }

    Python {
        id: python

        Component.onCompleted: {
            setHandler('update-data', function(message) {
                debug('Got a data update from Python module: ' + message)
                updateData()
            });

            setHandler('notification', function(message) {
                debug('Got a notification from Python module: ' + message)
                notificationMessage(message)
            });

            addImportPath(Qt.resolvedUrl('python'));

            /* Module should auto start scraper daemon, and that should sent a signal*/
            debug('Start deamon!');

            importModule('SimpelScraper', function() {
                debug('Get credentials!');

                // Here we use synchronized calls, so that we are sure to get all the data at the right time
                var username = call_sync('SimpelScraper.scraper.get_username',[]);
                if (username !== undefined && username !== '') {
                    debug('Got username: ' + username);
                    mobileDataObject.username = username;
                }

                var password = call_sync('SimpelScraper.scraper.get_password',[]);
                if (password !== undefined && password !== '') {
                    debug('Got password: ' + password);
                    mobileDataObject.password = password;
                }

                checkCredentials(mobileDataObject.username,mobileDataObject.password)
            });
        }

        // Function to check if we are loggedin at the Mobile provider
        function isLoggedIn() {
            return call_sync('SimpelScraper.scraper.isLoggedIn', []);
        }

        function checkCredentials(username,password) {
            startLoader();
            debug('Check if logged in already?');
            call('SimpelScraper.scraper.set_credentials', [username,password], function(result) {
                if (result === true) {
                    debug('Yup, and now update data');
                    mobileDataObject.username = username;
                    mobileDataObject.password = password;
                    notificationMessage(qsTr('Login successfull. Loading data...'))
                    updateData();
                } else {
                    notificationMessage(qsTr('The loaded credentials are invalid'))
                    force_settings_page();
                }
            });
        }

        // Get the latest data from your Mobile operator
        function updateData(force_update) {
            startLoader();
            force_update = force_update ? force_update : false;

            call('SimpelScraper.scraper.get_all_data', [force_update],function(result){
                debug('Got raw data!');

                mobileDataObject.mobilenumber = result['contract']['mobilenumber'];
                mobileDataObject.mobileplafond = result['plafond']['limit'];

                mobileDataObject.call_usage.total = result['call_usage']['total'];
                mobileDataObject.call_usage.used = result['call_usage']['used'];
                mobileDataObject.call_usage.free = result['call_usage']['free'];
                mobileDataObject.call_usage.percentage = (mobileDataObject.call_usage.used / mobileDataObject.call_usage.total ) * 100;

                mobileDataObject.sms_usage.total = result['sms_usage']['total']
                mobileDataObject.sms_usage.used = result['sms_usage']['used']
                mobileDataObject.sms_usage.free = result['sms_usage']['free']
                mobileDataObject.sms_usage.percentage = (mobileDataObject.sms_usage.used / mobileDataObject.sms_usage.total ) * 100;

                mobileDataObject.data_usage.total = result['data_usage']['total']
                mobileDataObject.data_usage.used = result['data_usage']['used']
                mobileDataObject.data_usage.free = result['data_usage']['free']
                mobileDataObject.data_usage.percentage = (mobileDataObject.data_usage.used / mobileDataObject.data_usage.total ) * 100;

                mobileDataObject.days_usage.total = result['days_usage']['total']
                mobileDataObject.days_usage.used = result['days_usage']['used']
                mobileDataObject.days_usage.free = result['days_usage']['free']
                mobileDataObject.days_usage.percentage = (mobileDataObject.days_usage.used / mobileDataObject.days_usage.total ) * 100;

                mobileDataObject.data_update_timeout = result['data_update_timeout'] / 3600
                mobileDataObject.last_update = new Date(result['last_update'] * 1000)

                getAccount()
                getContract()
                getOptions()

                getHistory()

                notificationMessage(qsTr('Account data is up to date'))
                stopLoader();
            });
        }

        function saveSettings(username,password,data_update_timeout) {
            debug('Start saving settings');

            var login = true;
            if (data_update_timeout !== mobileDataObject.data_update_timeout) {
                call('SimpelScraper.scraper.set_data_update_timeout', [data_update_timeout],function(result){
                    if (result) {
                        mobileDataObject.data_update_timeout = data_update_timeout
                        notificationMessage(qsTr('Timeout set to %L1 hours').arg(mobileDataObject.data_update_timeout))
                    } else {
                        notificationMessage(qsTr('Error updating timeout'))
                    }
                });
            }

            if (username !== mobileDataObject.username || password !== mobileDataObject.password) {
                debug('Check new credentials...');
                checkCredentials(username,password)
            }
        }

        function getAccount() {
            call('SimpelScraper.scraper.get_account_info',[], function(result){
                debug('Got account info!');
                mobileDataObject.accountoptions.clear()
                for (var key in result) {
                    mobileDataObject.accountoptions.append({'labelName':result[key]['label'],'labelValue':result[key]['value']});
                }
            });
        }

        function getContract() {
            call('SimpelScraper.scraper.get_contract_info',[], function(result){
                debug('Got contract info!');
                mobileDataObject.contractoptions.clear()
                for (var key in result) {
                    mobileDataObject.contractoptions.append({'labelName':result[key]['label'],'labelValue':result[key]['value']});
                }
            });
        }

        function getOptions() {
            call('SimpelScraper.scraper.get_mobile_options',[], function(result){
                debug('Got mobile options info!');
                mobileDataObject.mobileoptions.clear()
                for (var key in result) {
                    mobileDataObject.mobileoptions.append({'labelName':result[key]['label'],'labelValue':result[key]['value']});
                }
            });
        }

        function getEditOptions() {
            return call_sync('SimpelScraper.scraper.get_mobile_options', [true]);
        }

        function getHistory() {
            call('SimpelScraper.scraper.get_history', [],function(result){
                var history = qsTr('Date      ///    Call left, SMS left, Data left') + '\n' + '================================' + '\n'
                for (var key in result) {
                    history = history + Qt.formatDate(new Date(result[key].last_update * 1000),'dd MMM yyyy')  + '       ///        ' + result[key].call_usage.free + ', ' + result[key].sms_usage.free + ', ' + byteSize(result[key].data_usage.free) + '\n'
                }
                mobileDataObject.history = history
            });
        }

        function resetSettings() {
            call('SimpelScraper.scraper.reset_settings', [],function(result){
                debug('Reset settings: ' + result);
                if (result === true) {
                    mobileDataObject.username = ''
                    mobileDataObject.password = ''

                    mobileDataObject.mobilenumber = ''
                    mobileDataObject.mobileplafond = ''

                    mobileDataObject.call_usage.total = 0
                    mobileDataObject.call_usage.used = 0
                    mobileDataObject.call_usage.free = 0
                    mobileDataObject.call_usage.percentage = 0

                    mobileDataObject.sms_usage.total = 0
                    mobileDataObject.sms_usage.used = 0
                    mobileDataObject.sms_usage.free = 0
                    mobileDataObject.sms_usage.percentage = 0

                    mobileDataObject.data_usage.total = 0
                    mobileDataObject.data_usage.used = 0
                    mobileDataObject.data_usage.free = 0
                    mobileDataObject.data_usage.percentage = 0

                    mobileDataObject.days_usage.total = 0
                    mobileDataObject.days_usage.used = 0
                    mobileDataObject.days_usage.free = 0
                    mobileDataObject.days_usage.percentage = 0

                    mobileDataObject.data_update_timeout = 4

                    mobileDataObject.history = 'loading...'

                    mobileDataObject.accountoptions.clear()
                    mobileDataObject.contractoptions.clear()

                    mobileDataObject.last_update = 0
                 }
            });
        }
    }
}
