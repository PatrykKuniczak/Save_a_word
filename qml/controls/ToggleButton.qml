import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.5

Button{
    id: btnToggle

    property url btnIconSource: "../../images/svg_images/menu_icon.svg"
    property color btnColorDefault: "#58A4B0"
    property color btnColorMouseOver: "#23272E"
    property color btnColorPressed: "#00a1f1"

    QtObject{
        id: internal

        property var dynamicColor: if(btnToggle.down){
                                        btnToggle.down ? btnColorPressed : btnColorDefault
                                    }else{
                                        btnToggle.hovered ? btnColorMouseOver : btnColorDefault
                                    }

    }

    implicitWidth: 70
    implicitHeight: 60

    background: Rectangle{
        id: background_button


        color: internal.dynamicColor
        Image {
            id: button_icon
            source: btnIconSource
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            height: 25
            width: 25
            fillMode: Image.PreserveAspectFit
            visible: false
        }

        ColorOverlay{
            anchors.fill: button_icon
            source: button_icon
            color: "#ffffff"
            antialiasing: False
        }
    }
}
