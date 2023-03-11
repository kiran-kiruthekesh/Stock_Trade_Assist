
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_selectorWindow(object):
    def setupUi(self, selectorWindow, MainWindow):
        selectorWindow.setObjectName("selectorWindow")
        selectorWindow.resize(570, 410)
        selectorWindow.setStyleSheet("QWidget {\n"
        "    background-color: #17181c;\n"
        "}")
        self.centralwidget = QtWidgets.QWidget(selectorWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Main comboBox
        self.mainComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.mainComboBox.setGeometry(QtCore.QRect(170, 60, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mainComboBox.setFont(font)
        self.mainComboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mainComboBox.setMaxVisibleItems(5)
        self.mainComboBox.view().setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.mainComboBox.setEditable(True)
        self.mainComboBox.completer()
        self.mainComboBox.setMouseTracking(False)
        self.mainComboBox.setAutoFillBackground(False)
        self.mainComboBox.setStyleSheet("QComboBox {\n"
        "    background-color: #17181c ; \n"
        "    border-radius: 5px;\n"
        "   color : rgb(0, 199, 199);\n"
        "    border: 3px solid rgb(0, 199, 199);\n"
        "}\n"
        "QListView {"
        "color: white;"
        "background-color: white;"
        "border-radius: 5px;"
        "border: 3px solid rgb(0, 199, 199);"
        "}")
        self.mainComboBox.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.mainComboBox.setDuplicatesEnabled(False)
        self.mainComboBox.view().setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.mainComboBox.setFrame(True)
        self.mainComboBox.setObjectName("mainComboBox")

        # Sub comboBox
        self.subComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.subComboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.subComboBox.setGeometry(QtCore.QRect(170, 140, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.subComboBox.setFont(font)
        self.subComboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.subComboBox.setMaxVisibleItems(5)
        self.subComboBox.view().setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.subComboBox.setEditable(True)
        self.subComboBox.completer()
        self.subComboBox.setStyleSheet("QComboBox {\n"
        "    background-color: #17181c ; \n"
        "    border-radius: 5px;\n"
        "   color : rgb(0, 199, 199);\n"
        "    border: 3px solid rgb(0, 199, 199);\n"
        "}\n"
        "QListView {\n"
        "    color: black;\n"
        "    background-color: white;\n"
        "    border-radius: 5px;\n"
        "    border: 3px solid rgb(0, 199, 199);\n"
        "       border-radius: 5px;\n"
        "}\n"
        "")
        self.subComboBox.setObjectName("subComboBox")

        # Company name comboBox
        self.companyComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.companyComboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.companyComboBox.setGeometry(QtCore.QRect(170, 220, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.companyComboBox.setFont(font)
        self.companyComboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.companyComboBox.setMaxVisibleItems(5)
        self.companyComboBox.view().setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.companyComboBox.setEditable(True)
        self.companyComboBox.completer()
        self.companyComboBox.setStyleSheet("QComboBox {\n"
        "    background-color: #17181c ; \n"
        "    border-radius: 5px;\n"
        "   color : rgb(0, 199, 199);\n"
        "    border: 3px solid rgb(0, 199, 199);\n"
        "}\n"
        "QListView {\n"
        "    color: black;\n"
        "    background-color: white;\n"
        "    border-radius: 5px;\n"
        "    border: 3px solid rgb(0, 199, 199);\n"
        "       border-radius: 5px;\n"
        "}\n"
        "")
        self.companyComboBox.setObjectName("companyComboBox")

        # Button for submit
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(210, 300, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.submitButton.setFont(font)
        self.submitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submitButton.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(255, 255, 255) ; \n"
        "    border-radius: 15px;\n"
        "    border: 3px solid #4CAF50;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "  background-color: #4CAF50; \n"
        "  color: white;\n"
        "  border: 3px solid rgb(255, 255, 255);\n"
        "}\n"
        "")
        self.submitButton.setObjectName("submitButton")
        # Button for going back to main menu
        self.backButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.go_back(MainWindow, selectorWindow))
        self.backButton.setGeometry(QtCore.QRect(20, 10, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.backButton.setToolTip("Back")
        self.backButton.setFont(font)
        self.backButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backButton.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(255, 255, 255) ; \n"
        "    border-radius: 15px;\n"
        "    border: 3px solid rgb(255, 0, 0);\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "  background-color: rgb(255, 0, 0) ; \n"
        "    color: rgb(255, 0, 0);\n"
        "  color: white;\n"
        "  border: 3px solid rgb(255, 255, 255);\n"
        "}\n"
        "")
        self.backButton.setObjectName("backButton")
        selectorWindow.setCentralWidget(self.centralwidget)

        self.enableCompanySelectionCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.enableCompanySelectionCheckBox.setGeometry(QtCore.QRect(180, 190, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.enableCompanySelectionCheckBox.setFont(font)
        self.enableCompanySelectionCheckBox.setStyleSheet("QCheckBox {\n"
        "    background-color: #17181c ; \n"
        "   color : rgb(0, 199, 199);\n"
        "}")
        self.enableCompanySelectionCheckBox.setTristate(False)
        self.enableCompanySelectionCheckBox.setObjectName("enableCompanySelectionCheckBox")
        selectorWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(selectorWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 570, 22))
        self.menubar.setObjectName("menubar")
        selectorWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(selectorWindow)
        self.statusbar.setObjectName("statusbar")
        selectorWindow.setStatusBar(self.statusbar)

        self.retranslateUi(selectorWindow)
        QtCore.QMetaObject.connectSlotsByName(selectorWindow)


    def go_back(self, main_w, screener_w):
        main_w.show()
        screener_w.hide()

    def retranslateUi(self, selectorWindow):
        _translate = QtCore.QCoreApplication.translate
        selectorWindow.setWindowTitle(_translate("selectorWindow", "MainWindow"))
        self.submitButton.setText(_translate("selectorWindow", "SUBMIT"))
        self.backButton.setText(_translate("selectorWindow", "<<"))
        self.enableCompanySelectionCheckBox.setText(_translate("selectorWindow", " choose individual companies"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    selectorWindow = QtWidgets.QMainWindow()
    ui = Ui_selectorWindow()
    ui.setupUi(selectorWindow)
    selectorWindow.show()
    sys.exit(app.exec_())