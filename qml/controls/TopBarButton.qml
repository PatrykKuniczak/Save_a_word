import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.5

Button{
    id: btnTopBar

    property url btnIconSource: "../../images/svg_images/minimize_icon.svg"
    property color btnColorDefault: "#58A4B0"
    property color btnColorMouseOver: "#23272E"
    property color btnColorPressed: "#00a1f1"

    QtObject{
        id: internal

        property var dynamicColor: if(btnTopBar.down){
                                        btnTopBar.down ? btnColorPressed : btnColorDefault
                                    }else{
                                        btnTopBar.hovered ? btnColorMouseOver : btnColorDefault
                                    }

    }

    width: 35
    height: 35

    background: Rectangle{
        id: background_button


        color: internal.dynamicColor
        Image {
            id: button_icon
            source: btnIconSource
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            height: 16
            width: 16
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
