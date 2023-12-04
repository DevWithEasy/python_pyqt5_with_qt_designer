from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(656, 418)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #hello_label
        self.hello_label = QtWidgets.QLabel(self.centralwidget)
        self.hello_label.setGeometry(QtCore.QRect(130, 30, 411, 91))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(26)
        self.hello_label.setFont(font)
        self.hello_label.setObjectName("hello_label")

        #hello_button
        self.hello_button = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.press_hello())
        self.hello_button.setGeometry(QtCore.QRect(190, 120, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.hello_button.setFont(font)
        self.hello_button.setObjectName("hello_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #hello button click handle
    def press_hello(self) :
        self.hello_label.setText('Hello PyQt5')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.hello_label.setText(_translate("MainWindow", "Hello QT Designer"))
        self.hello_button.setText(_translate("MainWindow", "Join QT World"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
