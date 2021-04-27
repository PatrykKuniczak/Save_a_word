import QtQuick 2.0
import QtQuick.Controls 2.15

import "../controls"

Item {
    Rectangle {
        id: rectangle
        color: "#2e324a"
        anchors.fill: parent

        Label {
            id: label
            color: "#8f9091"
            text: qsTr("Generate mp3 from text")
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            anchors.rightMargin: 300
            anchors.leftMargin: 300
            anchors.topMargin: 50
            font.pointSize: 16
        }

        Rectangle {
            id: inputRectangle
            color: "#1e2130"
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: label.bottom
            anchors.bottom: parent.bottom
            anchors.rightMargin: 100
            anchors.leftMargin: 100
            anchors.bottomMargin: 100
            anchors.topMargin: 10
            radius: 10

            TextArea {
                id: textInput
                color: "#eae1e1"
                text: qsTr("")
                anchors.fill: parent
                font.pixelSize: 12
                horizontalAlignment: Text.AlignLeft
                verticalAlignment: Text.AlignTop
                wrapMode: Text.WordWrap
                font.hintingPreference: Font.PreferDefaultHinting
                antialiasing: true
                selectByMouse: true
                overwriteMode: false
                anchors.rightMargin: 10
                anchors.leftMargin: 10
                anchors.bottomMargin: 10
                anchors.topMargin: 10

                }
            }


        GenButton {
            x: 300
            width: 200
            height: 5

            text: "Generate"
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            font.pointSize: 13
            btnIconSource: "../../images/svg_images/gen_icon.svg"
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.bottomMargin: 35
            anchors.topMargin: 412
            btnColorDefault: "#6066a3"
            onClicked: {
                backend.genText(textInput.text)
            }


        }
        Connections{
            target: backend

        }
    }

}



/*##^##
Designer {
    D{i:0;autoSize:true;formeditorZoom:0.75;height:480;width:800}
}
##^##*/
