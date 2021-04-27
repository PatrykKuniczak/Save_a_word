import sys

from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QObject, QStringListModel


class main_window(QObject):
    def __init__(self):
        QObject.__init__(self)



# model = QStringListModel()
# model.setStringList(["hi", "ho"])
app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('qml\main.qml')

sys.exit(app.exec_())