# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\dlaeh\personal_project\papago_thing/papago_test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from pynput.keyboard import Listener, Key, KeyCode


class Thread(QtCore.QThread):
    cnt=0
    running=False

    def on_press(key):
         pass
    #try:
    #    print('alphanumeric key {0} pressed'.format(
    #        key.char))
    #except AttributeError:
    #    print('special key {0} pressed'.format(
    #        key))


    def on_release_copy(key):
        import pyperclip
        from project_papago import PapagoApi
        papatras = PapagoApi()
        if key == KeyCode(char='\x03'): # 지금은 키코드로 컨트롤 c를 지정했지만 딕셔너리로 지정해서 함수를 불러올 수도 있는거 같다.
            # Stop listener
            text = pyperclip.paste()
            return papatras.get_trans(text=text)
    # Collect events until released
    with Listener(
            on_press=on_press,
            on_release=on_release_copy) as listener:
            listener.join()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setStyleSheet("background-color: rgba(255, 255, 255, 150);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 80, 591, 331))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 26))
        self.menubar.setObjectName("menubar")

        self.Thread1 = Thread()
        self.Thread1.start()

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



