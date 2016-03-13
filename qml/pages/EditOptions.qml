import QtQuick 2.0
import Sailfish.Silica 1.0

Dialog {
    id: editOptionsPage

    DialogHeader {
        id: header
        title: "Edit Mobile Options"
    }

    function loadPage() {
        var options = statusApp.getMobileOptions()
        statusApp.debug('loadOptions')
//        statusApp.debug(options)

        var QMLObject = '
        import QtQuick 2.0;
        import Sailfish.Silica 1.0;
        SilicaListView {
            anchors.topMargin: 200;
            anchors.fill: parent;
            model: VisualItemModel { ';
        for (var optionkey in options) {
            QMLObject += 'ComboBox {
                width: editOptionsPage.width;
                label: "' + options[optionkey]['label'] + '";
                menu: ContextMenu { ';

            var currentIndex, counter = 0;
            for (var optionValueKey in options[optionkey]['options']) {
                if (options[optionkey]['value'] == options[optionkey]['options'][optionValueKey]['label']) {
                    currentIndex = counter;
                }
                QMLObject += 'MenuItem { text: "' + options[optionkey]['options'][optionValueKey]['label'] + '"} ';
                counter++;
            }
            QMLObject += ' }
                           currentIndex: ' + currentIndex + ' }';
        }
        QMLObject += '} }';
        Qt.createQmlObject(QMLObject,editOptionsPage,"options");
    }

    Component.onCompleted: {
        loadPage();
    }
}
