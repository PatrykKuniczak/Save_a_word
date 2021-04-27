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
            text: qsTr("Dodawanie słów")
            anchors.top: parent.top
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            anchors.topMargin: 10
            anchors.horizontalCenter: parent.horizontalCenter
            font.pointSize: 16
        }

        Table {
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.topMargin: 166
            anchors.bottomMargin: 14
            objectName: 'table'
            headerModel: [ // widths must add to 1
                {text: 'Słowo nieprzetłumaczone',         width: 0.5},
                {text: 'Tłumaczenie',   width: 0.5},
            ]

            dataModel: [
                ['Red',   '#ff0000'],
                ['Green', '#00ff00'],
                ['Blue',  '#0000ff'],
                ['Red',   '#ff0000'],
                ['Green', '#00ff00'],
                ['Blue',  '#0000ff'],
                ['Red',   '#ff0000'],
                ['Green', '#00ff00'],
                ['Blue',  '#0000ff'],
                ['Red',   '#ff0000'],
                ['Green', '#00ff00'],
                ['Blue',  '#0000ff'],
                ['Red',   '#ff0000'],
                ['Green', '#00ff00'],
                ['Blue',  '#0000ff'],
                ['Red',   '#ff0000'],
                ['Green', '#00ff00'],
                ['Blue',  '#0000ff'],
            ]

            onClicked: print('onClicked', row, JSON.stringify(rowData))
        }

        Rectangle {
            id: rectangle1
            y: 88
            width: 219
            height: 50
            color: "#58a4b0"
            radius: 10
            anchors.left: parent.left
            anchors.leftMargin: 20

            TextInput {
                id: textInput
                text: qsTr("")
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

        Rectangle {
            id: rectangle2
            x: 576
            y: 88
            width: 219
            height: 50
            color: "#58a4b0"
            radius: 10
            TextInput {
                id: textInput1
                text: qsTr("")
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
            y: 88
            height: 50
            anchors.left: rectangle2.right
            anchors.right: rectangle2.left
            anchors.rightMargin: -300
            anchors.leftMargin: 30

        }

        ComboBox {
            id: comboBox
            y: 45
            width: 219
            height: 30
            anchors.left: parent.left
            anchors.bottom: rectangle1.top
            anchors.bottomMargin: 13
            anchors.leftMargin: 20
        }

        Label {
            id: label1
            color: "#546771"
            text: qsTr("Tabela")
            anchors.left: rectangle1.right
            anchors.right: rectangle2.left
            anchors.top: parent.top
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            anchors.rightMargin: 269
            anchors.leftMargin: 6
            font.pointSize: 12
            anchors.topMargin: 104
        }

        ComboBox {
            id: comboBox2
            x: 576
            y: 45
            width: 219
            height: 30
            anchors.bottom: rectangle2.top
            anchors.bottomMargin: 13
        }

        ComboBox {
            id: comboBox3
            x: 344
            width: 219
            height: 25
            anchors.left: rectangle1.right
            anchors.right: rectangle2.left
            anchors.top: parent.top
            anchors.topMargin: 101
            anchors.leftMargin: 105
            anchors.rightMargin: 14
        }
    }

}



/*##^##
Designer {
    D{i:0;autoSize:true;formeditorZoom:0.75;height:496;width:906}D{i:4}D{i:10}D{i:11}
D{i:12}
}
##^##*/
