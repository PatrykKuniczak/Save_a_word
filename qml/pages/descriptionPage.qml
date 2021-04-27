import QtQuick 2.0
import QtQuick.Controls 2.15
import '../controls'
Item {
    Rectangle {
        id: rectangle
        color: "#bce7fd"
        anchors.fill: parent

        Label {
            id: label
            color: "#546771"
            text: qsTr("Instrukcja obsługi i opis aplikacji")
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            anchors.bottomMargin: 434
            anchors.rightMargin: 300
            anchors.leftMargin: 300
            anchors.topMargin: 21
            font.pointSize: 16
        }
    }
}



/*##^##
Designer {
    D{i:0;autoSize:true;formeditorZoom:0.75;height:496;width:906}D{i:3}D{i:5}D{i:7}D{i:6}
D{i:8}D{i:9}
}
##^##*/
