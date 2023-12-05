from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def press_it(self,pressed):
        if pressed == 'C' :
            self.output_label.setText('0')
        else :
            if self.output_label.text() == '0' :
                self.output_label.setText("")
            self.output_label.setText(f'{self.output_label.text()}{pressed}')

    def dot_it(self):
        screen = self.output_label.text()
        if screen[-1] == '.':
                pass
        else:
                self.output_label.setText(f'{screen}.')

    def calculate(self):
        pass


    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(342, 448)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #----------------------------------------
                #output label
        #----------------------------------------
        self.output_label = QtWidgets.QLabel(self.centralwidget)
        self.output_label.setGeometry(QtCore.QRect(20, 10, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.output_label.setFont(font)
        self.output_label.setFrameShape(QtWidgets.QFrame.Box)
        self.output_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.output_label.setText("")
        self.output_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.output_label.setObjectName("output_label")

        #----------------------------------------
                #percent button
        #----------------------------------------
        self.percent_button = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.press_it('%'))
        self.percent_button.setGeometry(QtCore.QRect(20, 90, 61, 51))
        self.percent_button.setObjectName("percent_button")

        #----------------------------------------
                #cancel button
        #----------------------------------------
        self.cancel_button = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.press_it('C'))
        self.cancel_button.setGeometry(QtCore.QRect(100, 90, 61, 51))
        self.cancel_button.setObjectName("cancel_button")

        #----------------------------------------
                #back button
        #----------------------------------------
        self.back_button = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.press_it('<<'))
        self.back_button.setGeometry(QtCore.QRect(180, 90, 61, 51))
        self.back_button.setObjectName("back_button")

        #----------------------------------------
                #divison button
        #----------------------------------------
        self.division_button = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.press_it('/'))
        self.division_button.setGeometry(QtCore.QRect(260, 90, 61, 51))
        self.division_button.setObjectName("division_button")

        #----------------------------------------
                #nine button
        #----------------------------------------
        self.nine__button = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.press_it('9'))
        self.nine__button.setGeometry(QtCore.QRect(180, 160, 61, 51))
        self.nine__button.setObjectName("nine__button")

        #----------------------------------------
                #seven button
        #----------------------------------------
        self.seven_button = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.press_it('7'))
        self.seven_button.setGeometry(QtCore.QRect(20, 160, 61, 51))
        self.seven_button.setObjectName("seven_button")

        #----------------------------------------
                #eight button
        #----------------------------------------
        self.eight_button = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.press_it('8'))
        self.eight_button.setGeometry(QtCore.QRect(100, 160, 61, 51))
        self.eight_button.setObjectName("eight_button")

        #----------------------------------------
                #multipication button
        #----------------------------------------
        self.multipication__button = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.press_it('*'))
        self.multipication__button.setGeometry(QtCore.QRect(260, 160, 61, 51))
        self.multipication__button.setObjectName("multipication__button")

        #----------------------------------------
                #four button
        #----------------------------------------
        self.four_button = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.press_it('4'))
        self.four_button.setGeometry(QtCore.QRect(20, 230, 61, 51))
        self.four_button.setObjectName("four_button")

        #----------------------------------------
                #plus button
        #----------------------------------------
        self.plus_button = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.press_it('+'))
        self.plus_button.setGeometry(QtCore.QRect(260, 230, 61, 51))
        self.plus_button.setObjectName("plus_button")

        #----------------------------------------
                #five button
        #----------------------------------------
        self.five_button = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.press_it('5'))
        self.five_button.setGeometry(QtCore.QRect(100, 230, 61, 51))
        self.five_button.setObjectName("five_button")

        #----------------------------------------
                #six button
        #----------------------------------------
        self.six_button = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.press_it('6'))
        self.six_button.setGeometry(QtCore.QRect(180, 230, 61, 51))
        self.six_button.setObjectName("six_button")

        #----------------------------------------
                #three button
        #----------------------------------------
        self.three_button = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.press_it('3'))
        self.three_button.setGeometry(QtCore.QRect(180, 300, 61, 51))
        self.three_button.setObjectName("three_button")

        #----------------------------------------
                #minus button
        #----------------------------------------
        self.minus_button = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.press_it('-'))
        self.minus_button.setGeometry(QtCore.QRect(260, 300, 61, 51))
        self.minus_button.setObjectName("minus_button")

        #----------------------------------------
                #two button
        #----------------------------------------
        self.two_button = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.press_it('2'))
        self.two_button.setGeometry(QtCore.QRect(100, 300, 61, 51))
        self.two_button.setObjectName("two_button")

        #----------------------------------------
                #one button
        #----------------------------------------
        self.one_button = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.press_it('1'))
        self.one_button.setGeometry(QtCore.QRect(20, 300, 61, 51))
        self.one_button.setObjectName("one_button")

        #----------------------------------------
                #dot button
        #----------------------------------------
        self.dot_button = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.dot_it())
        self.dot_button.setGeometry(QtCore.QRect(180, 370, 61, 51))
        self.dot_button.setObjectName("dot_button")

        #----------------------------------------
                #plus_minus button
        #----------------------------------------
        self.plus_minus_button = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.press_it('+/-'))
        self.plus_minus_button.setGeometry(QtCore.QRect(20, 370, 61, 51))
        self.plus_minus_button.setObjectName("plus_minus_button")

        #----------------------------------------
                #equal button
        #----------------------------------------
        self.equal_button = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.press_it('='))
        self.equal_button.setGeometry(QtCore.QRect(260, 370, 61, 51))
        self.equal_button.setObjectName("equal_button")

        #----------------------------------------
                #zero button
        #----------------------------------------
        self.zero_button = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.press_it('0'))
        self.zero_button.setGeometry(QtCore.QRect(100, 370, 61, 51))
        self.zero_button.setObjectName("zero_button")


        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.percent_button.setText(_translate("MainWindow", "%"))
        self.cancel_button.setText(_translate("MainWindow", "C"))
        self.back_button.setText(_translate("MainWindow", "<<"))
        self.division_button.setText(_translate("MainWindow", "/"))
        self.nine__button.setText(_translate("MainWindow", "9"))
        self.seven_button.setText(_translate("MainWindow", "7"))
        self.eight_button.setText(_translate("MainWindow", "8"))
        self.multipication__button.setText(_translate("MainWindow", "X"))
        self.four_button.setText(_translate("MainWindow", "4"))
        self.plus_button.setText(_translate("MainWindow", "+"))
        self.five_button.setText(_translate("MainWindow", "5"))
        self.six_button.setText(_translate("MainWindow", "6"))
        self.three_button.setText(_translate("MainWindow", "3"))
        self.minus_button.setText(_translate("MainWindow", "-"))
        self.two_button.setText(_translate("MainWindow", "2"))
        self.one_button.setText(_translate("MainWindow", "1"))
        self.dot_button.setText(_translate("MainWindow", "."))
        self.plus_minus_button.setText(_translate("MainWindow", "+/-"))
        self.equal_button.setText(_translate("MainWindow", "="))
        self.zero_button.setText(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
