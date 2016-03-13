import QtQuick 2.0
import Sailfish.Silica 1.0

Item {
    id: listElement
    width: parent.width;
    height: label.height + value.height
    anchors {
        left: parent.left
        right: parent.right
        leftMargin: Theme.paddingLarge
        rightMargin: Theme.paddingLarge
    }
    Text {
        id: label
        text: labelName
        color: '#923178'
        font.bold: true
        width: parent.width;

    }
    Text {
        id: value
        text: '\n' + labelValue
        color: '#ffffff'
        width: parent.width;
        wrapMode: Text.WordWrap
    }
}
