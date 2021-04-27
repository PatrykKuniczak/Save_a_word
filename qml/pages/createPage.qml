import QtQuick 2.0
import QtQuick.Controls 2.15
import '../controls'
Item {
    Rectangle {
        id: rectangle
        color: "#bce7fd"
        anchors.fill: parent
        anchors.rightMargin: 0
        anchors.bottomMargin: 0
        anchors.leftMargin: 0
        anchors.topMargin: 0

        Label {
            id: label
            color: "#546771"
            text: qsTr("Tworzenie tabel")
            anchors.top: parent.top
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            anchors.horizontalCenterOffset: 0
            anchors.topMargin: 23
            anchors.horizontalCenter: parent.horizontalCenter
            font.pointSize: 16
        }

        Rectangle {
            id: rectangle2
            x: 29
            y: 88
            width: 787
            height: 50
            color: "#58a4b0"
            radius: 10
            TextInput {
                id: textInput1
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                font.pixelSize: 12
                verticalAlignment: Text.AlignVCenter
                anchors.rightMargin: 8
                anchors.leftMargin: 14
                anchors.bottomMargin: 15
                anchors.topMargin: 15
            }
        }
        AddButton{
            x: 822
            y: 88
            width: 52
            height: 50
            anchors.right: rectangle2.left
            anchors.rightMargin: -845
            
        }
        
        Image {
            id: image
            x: 367
            y: 381
            width: 172
            height: 95
            source: "../../images/svg_images/database.svg"
            fillMode: Image.PreserveAspectFit
        }
    }

}



/*##^##
Designer {
    D{i:0;autoSize:true;height:496;width:906}
}
##^##*/
