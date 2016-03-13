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

Page {
    id: homePage

    BusyIndicator {
        id: loader
        anchors.centerIn: parent
        size: BusyIndicatorSize.Medium
        running: statusApp.dataLoading
    }

    // To enable PullDownMenu, place our content in a SilicaFlickable
    SilicaFlickable {
        anchors.fill: parent
        contentHeight: column.height + Theme.paddingLarge

        // Why is this necessary?
        contentWidth: parent.width

        VerticalScrollDecorator {}

        // PullDownMenu and PushUpMenu must be declared in SilicaFlickable, SilicaListView or SilicaGridView
        PullDownMenu {
            MenuItem {
                text: qsTr('Account information')
                onClicked: pageStack.push(Qt.resolvedUrl('Account.qml'))
            }
            MenuItem {
                text: qsTr('Contract information')
                onClicked: pageStack.push(Qt.resolvedUrl('Contract.qml'))
            }
            MenuItem {
                text: qsTr('Mobile Options')
                onClicked: pageStack.push(Qt.resolvedUrl('Options.qml'))
            }
        }

        PushUpMenu {
            MenuItem {
                text: qsTr('Force Update')
                onClicked: statusApp.updateMainData(true)
            }
            MenuItem {
                text: qsTr('Settings')
                onClicked: pageStack.push(Qt.resolvedUrl('Settings.qml'))
            }
            MenuItem {
                text: qsTr('History')
                onClicked: pageStack.push(Qt.resolvedUrl('History.qml'))
            }
            MenuItem {
                text: qsTr('About')
                onClicked: pageStack.push(Qt.resolvedUrl('About.qml'))
            }
        }

        // Place our content in a Column.  The PageHeader is always placed at the top
        // of the page, followed by our content.
        Column {
            id: column
            width: parent.width

            PageHeader {
                title: qsTr('Simpel account status')
            }

            Label {
                id: body
                text: qsTr('Here you can see your account status of your mobile plan at Simpel.nl') + '\n'
                wrapMode: Text.WordWrap
                horizontalAlignment: Text.AlignHCenter
                anchors {
                    left: parent.left
                    right: parent.right
                }
            }

            TextField {
                id: mobilenumberField
                placeholderText: qsTr('Loading...')
                text: statusApp.mobileData.mobilenumber
                label: qsTr('Mobile number')
                readOnly: true
                labelVisible: true
                anchors {
                    left: parent.left
                    right: parent.right
                }
            }

            TextField {
                id: mobilePlafond
                placeholderText: qsTr('Loading...')
                text: statusApp.mobileData.mobileplafond
                label: qsTr('Mobile plafond')
                readOnly: true
                labelVisible: true
                anchors {
                    left: parent.left
                    right: parent.right
                }
            }

            ProgressBar {
                id: callusageBar
                minimumValue: 0
                maximumValue: 100
                value: statusApp.mobileData.call_usage.percentage
                label: qsTr('Call usage: %L1 out of %L2').arg(statusApp.mobileData.call_usage.used).arg(statusApp.mobileData.call_usage.total)
                anchors {
                    left: parent.left
                    right: parent.right
                }
            }

            ProgressBar {
                id: smsusageBar
                minimumValue: 0
                maximumValue: 100
                value: statusApp.mobileData.sms_usage.percentage
                label: qsTr('SMS usage: %L1 out of %L2').arg(statusApp.mobileData.sms_usage.used).arg(statusApp.mobileData.sms_usage.total)
                anchors {
                    left: parent.left
                    right: parent.right
                }
            }

            ProgressBar {
                id: datausageBar
                minimumValue: 0
                maximumValue: 100
                value: statusApp.mobileData.data_usage.percentage
                label: qsTr('Internet usage: %1 out of %2').arg(statusApp.byteSize(statusApp.mobileData.data_usage.used)).arg(statusApp.byteSize(statusApp.mobileData.data_usage.total))
                anchors {
                    left: parent.left
                    right: parent.right
                }
            }

            ProgressBar {
                id: daysausageBar
                minimumValue: 0
                maximumValue: 100
                value: statusApp.mobileData.days_usage.percentage
                label: qsTr('Days usage: %L1 out of %L2').arg(statusApp.mobileData.days_usage.used).arg(statusApp.mobileData.days_usage.total)
                anchors {
                    left: parent.left
                    right: parent.right
                }
            }

            Label {
                id: spacer
                text: '\n'
                horizontalAlignment: Text.AlignHCenter
                anchors {
                    left: parent.left
                    right: parent.right
                    leftMargin: Theme.paddingLarge
                    rightMargin: Theme.paddingLarge
                }
            }

            TextField {
                id: lastUpdateField
                placeholderText: qsTr('Loading...')
                text: statusApp.mobileData.last_update === 0 ? qsTr('Loading...') : Qt.formatDateTime(statusApp.mobileData.last_update,'dddd dd-MMM-yyyy hh:mm:ss')
                label: qsTr('Last update')
                readOnly: true
                labelVisible: true
                anchors {
                    left: parent.left
                    right: parent.right
                }
            }
        }
    }
}
