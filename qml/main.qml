import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import 'controls'

Window {
    id: main_window
    width: 1000
    height: 580
    visible: true
    color: "#00000000"
    title: qsTr("Save a word")

    flags: Qt.Window | Qt.FramelessWindowHint

    property  int windowStatus: 0
    property int windowMargin: 10
    QtObject{
        id: internal
        function maximizeRestore(){
            if(windowStatus == 0){
                windowStatus = 1
                windowMargin = 0
                maximize.btnIconSource ="../images/svg_images/restore_icon.svg"
                main_window.showMaximized()
            }else{
                main_window.showNormal()
                windowStatus = 0
                windowMargin = 10
                maximize.btnIconSource ="../images/svg_images/maximize_icon.svg"
            }
        }

    }

    Rectangle {
        id: background
        color: "#bce7fd"
        border.color: "#1381b9"
        border.width: 2
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.rightMargin: windowMargin
        anchors.leftMargin: windowMargin
        anchors.bottomMargin: windowMargin
        anchors.topMargin: windowMargin

        Rectangle {
            id: app_container
            color: "#00000000"
            anchors.fill: parent
            anchors.rightMargin: 2
            anchors.leftMargin: 2
            anchors.bottomMargin: 2
            anchors.topMargin: 2

            Rectangle {
                id: top_bar
                height: 60
                color: "#58a4b0"
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.rightMargin: 0
                anchors.leftMargin: 0
                anchors.topMargin: 0


                ToggleButton {
                    onClicked: animationMenu.running = true

                }

                Rectangle {

                    id: top_bar_description
                    y: 12
                    height: 25
                    color: "#bcf3fd"
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.bottom: parent.bottom
                    anchors.rightMargin: 0
                    anchors.leftMargin: 70
                    anchors.bottomMargin: 0
                    DragHandler{
                        onActiveChanged: if(active){
                                             main_window.startSystemMove()
                                         }
                    }

                    Label {
                        id: label_info
                        height: 25
                        color: "#2f2f2f"
                        text: qsTr("Learn new languaghe faster")
                        anchors.left: parent.left
                        anchors.right: parent.right
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                        anchors.rightMargin: 300
                        anchors.leftMargin: 10
                        anchors.bottomMargin: 0
                        anchors.topMargin: 0
                    }
                }

                Rectangle {
                    id: title_bar
                    height: 35
                    color: "#00000000"
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.top: parent.top
                    anchors.rightMargin: 105
                    anchors.leftMargin: 70
                    anchors.topMargin: 0


                    Label {
                        id: label
                        color: "#282b2d"
                        text: qsTr("SAVE A WORD")
                        anchors.left: parent.left
                        anchors.right: parent.right
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                        font.family: "Verdana"
                        font.pointSize: 13
                        anchors.leftMargin: 5
                        anchors.rightMargin: 0
                        anchors.bottomMargin: 0
                        anchors.topMargin: 0
                    }

                    Row {
                        id: row
                        height: 35
                        anchors.left: label.right
                        anchors.right: parent.right
                        anchors.top: parent.top
                        anchors.leftMargin: 0
                        anchors.rightMargin: -105
                        anchors.topMargin: 0

                        TopBarButton {
                            id: minimize
                            onClicked: main_window.showMinimized()

                        }

                        TopBarButton {
                            id: maximize
                            btnIconSource: "../images/svg_images/maximize_icon.svg"
                            onClicked: internal.maximizeRestore()
                        }

                        TopBarButton {
                            id: close
                            btnColorMouseOver: "#c74be3"
                            btnIconSource: "../images/svg_images/close_icon.svg"
                            onClicked: main_window.close()
                        }
                    }
                }
            }

            Rectangle {
                id: content
                color: "#00000000"
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: top_bar.bottom
                anchors.bottom: parent.bottom
                anchors.topMargin: 0

                Rectangle {
                    id: left_menu
                    width: 70
                    color: "#58a4b0"
                    anchors.left: parent.left
                    anchors.top: parent.top
                    anchors.bottom: parent.bottom
                    anchors.leftMargin: 0
                    anchors.bottomMargin: 0
                    anchors.topMargin: 0

                    PropertyAnimation{
                        id: animationMenu
                        target: left_menu
                        property: "width"
                        to: if(left_menu.width == 70) return 200; else return 70
                        duration: 1000
                        easing.type: Easing.InOutQuint
                    }

                    Column {
                        id: column_menu
                        width: left_menu.width
                        anchors.left: parent.left
                        anchors.right: parent.right
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        anchors.rightMargin: 0
                        anchors.leftMargin: 0
                        anchors.bottomMargin: 0
                        anchors.topMargin: 0

                        LeftMenuBtn {
                            id: description
                            text: "Description"
                            btnIconSource: "../images/svg_images/home_icon.svg"
                            onClicked: {
                                working.isActive = false
                                info.isActive = false
                                description.isActive = true
                                stackView.push(Qt.resolvedUrl("pages/descriptionPage.qml"))
                            }

                        }

                        LeftMenuBtn {
                            id: working
                            text: "Generate"
                            anchors.top: description.bottom
                            isActive: false
                            btnIconSource: "../images/svg_images/working_icon.svg"
                            anchors.topMargin: 0
                            onClicked: {
                                description.isActive = false
                                info.isActive = false
                                working.isActive = true
                                stackView.push(Qt.resolvedUrl("pages/workingPage.qml"))
                            }

                        }

                        LeftMenuBtn {
                            id: info
                            text: "Info"
                            anchors.bottom: parent.bottom
                            isActive: false
                            btnIconSource: "../images/svg_images/info_icon.svg"
                            iconWidth: 18
                            iconHeight: 18
                            anchors.bottomMargin: 0
                            onClicked: {
                                description.isActive = false
                                working.isActive = false
                                info.isActive = true
                                stackView.push(Qt.resolvedUrl("pages/infoPage.qml"))
                            }
                        }
                    }
                }

                Rectangle {
                    id: pages
                    color: "#BCE7FD"
                    anchors.left: left_menu.right
                    anchors.right: parent.right
                    anchors.top: parent.top
                    anchors.bottom: parent.bottom
                    clip: true
                    anchors.rightMargin: 0
                    anchors.leftMargin: 0
                    anchors.bottomMargin: 0
                    anchors.topMargin: 0
                }
            }

        }
    }
}
