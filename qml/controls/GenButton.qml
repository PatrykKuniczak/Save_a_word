import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.5

Button{
    id: btnGen
    text: qsTr("Info")


    property url btnIconSource: "../../images/svg_images/menu_icon.svg"
    property color btnColorDefault: "#58A4B0"
    property color btnColorMouseOver: "#23272E"
    property color btnColorPressed: "#00a1f1"
    property int iconWidth: 18
    property int iconHeight: 18
    property color activeColor: "#2213bd"
    property color activeColorRight: "#2e324a"
    property bool isActive: true

    QtObject{
        id: internal

        property var dynamicColor: if(btnGen.down){
                                        btnGen.down ? btnColorPressed : btnColorDefault
                                    }else{
                                        btnGen.hovered ? btnColorMouseOver : btnColorDefault
                                    }

    }

    implicitWidth: 200
    implicitHeight: 35

    background: Rectangle{
        id: background_button
        color: internal.dynamicColor
        radius: 10

}
    contentItem: Item {
        id: content
        anchors.fill: parent

            Image {
                id: button_icon
                anchors.verticalCenterOffset: 0
                anchors.leftMargin: 26
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left
                source: btnIconSource
                sourceSize.width: iconWidth
                sourceSize.height: iconHeight
                height: iconHeight
                width: iconWidth
                fillMode: Image.PreserveAspectFit
                visible: true
                antialiasing: true

            }

            ColorOverlay{
                anchors.fill: button_icon
                source: button_icon
                anchors.verticalCenterOffset: 0
                anchors.leftMargin: 26
                color: "#ffffff"
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left
                antialiasing: true
                width: iconWidth
                height: iconHeight

            }

            Text {
                id: name
                text: btnGen.text
                font: btnGen.font
                color: "#ffffff"
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left
                anchors.leftMargin: 100
            }
        }
}


/*##^##
Designer {
    D{i:0;autoSize:true;formeditorZoom:0.75;height:35;width:200}
}
##^##*/
