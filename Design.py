

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Design.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QMessageBox, QGroupBox, QLabel, QLineEdit
from stringNames import *
from Device import *

#Main window
class Ui_MainWindow(object):
    #sets up basic ui with buttons: manual, graphs, settings and info
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(918, 645)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 81, 551))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        spacerItem = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)

        self.Manual = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Manual.setObjectName("Manual")
        self.verticalLayout.addWidget(self.Manual)

        self.Graphs = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Graphs.setObjectName("Graphs")
        self.verticalLayout.addWidget(self.Graphs)

        self.Settings = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Settings.setObjectName("Settings")
        self.verticalLayout.addWidget(self.Settings)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.Info = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Info.setObjectName("Info")
        self.verticalLayout.addWidget(self.Info)

        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 10, 781, 52))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.Logo = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Logo.setEnabled(True)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Logo.sizePolicy().hasHeightForWidth())

        self.Logo.setSizePolicy(sizePolicy)
        self.Logo.setMinimumSize(QtCore.QSize(0, 0))
        self.Logo.setMaximumSize(QtCore.QSize(300, 30))

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Logo.setFont(font)
        self.Logo.setAutoFillBackground(True)
        self.Logo.setFrameShape(QtWidgets.QFrame.Box)
        self.Logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Logo.setObjectName("Logo")
        self.horizontalLayout_2.addWidget(self.Logo)

        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)

        self.fSkyTemp = QtWidgets.QFrame(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fSkyTemp.sizePolicy().hasHeightForWidth())
        self.fSkyTemp.setSizePolicy(sizePolicy)
        self.fSkyTemp.setMinimumSize(QtCore.QSize(180, 100))
        self.fSkyTemp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fSkyTemp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fSkyTemp.setObjectName("fSkyTemp")

        self.Sky = QtWidgets.QLabel(self.fSkyTemp)
        self.Sky.setGeometry(QtCore.QRect(10, 20, 71, 16))
        self.Sky.setObjectName("Sky")

        self.TempUp = QtWidgets.QLabel(self.fSkyTemp)
        self.TempUp.setGeometry(QtCore.QRect(100, 20, 75, 13))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TempUp.sizePolicy().hasHeightForWidth())

        self.TempUp.setSizePolicy(sizePolicy)
        self.TempUp.setMinimumSize(QtCore.QSize(60, 0))
        self.TempUp.setObjectName("TempUp")

        self.horizontalLayout_2.addWidget(self.fSkyTemp)

        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(90, 60, 781, 501))   #90, 60, 781, 501
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.setupDeviceWindow()       #sets up device window

        self.Manual.clicked.connect(self.toggleManual)
        self.Graphs.clicked.connect(self.showGraphs)
        self.Settings.clicked.connect(self.setupSettingsWindow)
        self.Info.clicked.connect(self.showInfo)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #sets up the ui in which you can see the devices
    def setupDeviceWindow(self):
        self.Rolluik1Widget = QtWidgets.QWidget(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Rolluik1Widget.sizePolicy().hasHeightForWidth())

        self.Rolluik1Widget.setSizePolicy(sizePolicy)
        self.Rolluik1Widget.setMinimumSize(QtCore.QSize(200, 80))
        self.Rolluik1Widget.setMaximumSize(QtCore.QSize(400, 150))
        self.Rolluik1Widget.setMouseTracking(False)
        self.Rolluik1Widget.setAutoFillBackground(True)
        self.Rolluik1Widget.setObjectName("Rolluik1Widget")
        self.Rolluik1 = QtWidgets.QLabel(self.Rolluik1Widget)
        self.Rolluik1.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.Rolluik1.setObjectName("Rolluik1")

        self.Status1 = QtWidgets.QLabel(self.Rolluik1Widget)
        self.Status1.setGeometry(QtCore.QRect(150, 65, 100, 20))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Status1.sizePolicy().hasHeightForWidth())

        self.Status1.setSizePolicy(sizePolicy)
        self.Status1.setAcceptDrops(False)
        self.Status1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Status1.setAutoFillBackground(True)
        self.Status1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Status1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Status1.setTextFormat(QtCore.Qt.PlainText)
        self.Status1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.Status1.setObjectName("Status1")

        self.Rolluik1.raise_()
        self.Status1.raise_()
        self.gridLayout_3.addWidget(self.Rolluik1Widget, 0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)     #changes central widget
        self.retranslateUi(MainWindow)  # sets te text

    #sets up settingswidget that shows the settings
    def setupSettingsWindow(self):
        self.settingsWindowWidget = QtWidgets.QWidget(self.gridLayoutWidget)
        self.settingsWindowWidget.setMinimumSize(QtCore.QSize(400,160))
        self.settingsWindowWidget.setMaximumSize(QtCore.QSize(400,160))

        self.layout = QtWidgets.QFormLayout(self.settingsWindowWidget)
        self.minLight = QtWidgets.QLineEdit(self.settingsWindowWidget)
        self.minTemp = QtWidgets.QLineEdit(self.settingsWindowWidget)

        self.chgMinLight = QtWidgets.QPushButton(self.settingsWindowWidget)
        self.chgMinLight.setText("Change the min light value")

        self.chgMinTemp = QtWidgets.QPushButton(self.settingsWindowWidget)
        self.chgMinTemp.setText("Change the min temp value")

        self.goBack = QtWidgets.QPushButton(self.settingsWindowWidget)
        self.goBack.setText("Ok")
        self.goBack.clicked.connect(self.setupDeviceWindow)

        self.layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.minLight)
        self.layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.minTemp)
        self.layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.chgMinLight)
        self.layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.chgMinTemp)
        self.layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.goBack)

        self.gridLayout_3.removeWidget(self.Rolluik1Widget)
        self.Status1.hide()
        self.gridLayout_3.addWidget(self.settingsWindowWidget, 0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)  #changes central widget

    #sets te text
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Manual.setText(_translate("MainWindow", "Manual"))
        self.Graphs.setText(_translate("MainWindow", "Graphs"))
        self.Settings.setText(_translate("MainWindow", "Settings"))
        self.Info.setText(_translate("MainWindow", "Info"))
        self.Logo.setText(_translate("MainWindow", "Aeros Development"))
        self.Sky.setText(_translate("MainWindow", "Sky:  Sunny"))
        self.TempUp.setText(_translate("MainWindow", "Temp: 30C"))

        device1 = Device("rolluik 1", False, 0, 0)

        self.Rolluik1.setText(_translate("MainWindow", device1.getName()))
        self.Status1.setText(_translate("MainWindow", "Status: " + device1.getStatus()))

    #makes inputdialog in which you can enter a percentage
    def toggleManual(self):
        print("Popup that allows to roll out shutter")
        try:
            s = stringNames()
            s.setManualText("Give percentage", "percentage: ")
            string = s.getManualText()
            title_text = string.split(";")
            title = title_text[0]
            text = title_text[1]

            res, popup = QInputDialog(MainWindow).getInt(MainWindow, title, text ,0 , 0, 100, 1) #res is input result
            popup.exec()

        except:
            pass

    #changes the central widget to graphs widget
    def showGraphs(self):
        print("Shows 2 graphs, temp and light")

    #Makes popup with info
    def showInfo(self):
        info = QMessageBox()

        s = stringNames()
        s.setInfoText("Aeros Development", "we made this dashboard")
        string = s.getInfoText()
        title_text = string.split(";",)
        title = title_text[0]
        text = title_text[1]

        info.setIcon(QMessageBox.Information)
        info.setText(title)
        info.setInformativeText(text)
        info.setWindowTitle("Info")
        info.setStandardButtons(QMessageBox.Cancel)
        info.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())