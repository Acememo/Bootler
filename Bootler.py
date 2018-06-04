# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Bootler.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(109, 431)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(109, 431))
        MainWindow.setMaximumSize(QtCore.QSize(109, 431))
        MainWindow.setWindowTitle("")
        MainWindow.setStyleSheet("Fusion")

        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setMinimumSize(QtCore.QSize(91, 91))
        self.widget_2.setMaximumSize(QtCore.QSize(91, 91))
        self.widget_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_2.setObjectName("widget_2")

        
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 91, 91))
        self.pushButton.setMinimumSize(QtCore.QSize(91, 91))
        self.pushButton.setMaximumSize(QtCore.QSize(91, 91))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")

        
        self.verticalLayout.addWidget(self.widget_2, 0, QtCore.Qt.AlignHCenter)

        
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)

        
        self.verticalLayout.addItem(spacerItem)

        
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setMinimumSize(QtCore.QSize(91, 91))
        self.widget_3.setMaximumSize(QtCore.QSize(91, 91))
        self.widget_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_3.setObjectName("widget_3")

        
        self.widget = QtWidgets.QWidget(self.widget_3)
        self.widget.setGeometry(QtCore.QRect(0, 0, 91, 91))
        self.widget.setMinimumSize(QtCore.QSize(91, 91))
        self.widget.setMaximumSize(QtCore.QSize(91, 91))
        self.widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget.setObjectName("widget")

        
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 0, 91, 91))
        self.pushButton_2.setMinimumSize(QtCore.QSize(91, 91))
        self.pushButton_2.setMaximumSize(QtCore.QSize(91, 91))
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")

        
        self.verticalLayout.addWidget(self.widget_3, 0, QtCore.Qt.AlignHCenter)

        
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)

        
        self.verticalLayout.addItem(spacerItem1)

        
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setMinimumSize(QtCore.QSize(91, 91))
        self.widget_4.setMaximumSize(QtCore.QSize(91, 91))
        self.widget_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_4.setObjectName("widget_4")

        
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 0, 91, 91))
        self.pushButton_3.setMinimumSize(QtCore.QSize(91, 91))
        self.pushButton_3.setMaximumSize(QtCore.QSize(91, 91))
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")

        
        self.verticalLayout.addWidget(self.widget_4, 0, QtCore.Qt.AlignHCenter)

        
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")

        
        self.horizontalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)

        
        spacerItem2 = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)

        
        self.horizontalLayout_2.addItem(spacerItem2)

        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")

        
        self.horizontalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)

        
        spacerItem3 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)

        
        self.horizontalLayout_2.addItem(spacerItem3)

        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")

        
        self.horizontalLayout_2.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)

        
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        
        self.auto_OFF = QtWidgets.QRadioButton(self.centralwidget)

        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.auto_OFF.sizePolicy().hasHeightForWidth())

        
        self.auto_OFF.setSizePolicy(sizePolicy)
        self.auto_OFF.setText("")
        self.auto_OFF.setObjectName("auto_OFF")

        
        self.horizontalLayout.addWidget(self.auto_OFF, 0, QtCore.Qt.AlignHCenter)

        
        spacerItem4 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)

        
        self.horizontalLayout.addItem(spacerItem4)

        
        self.auto_ONOFF_box = QtWidgets.QCheckBox(self.centralwidget)

        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.auto_ONOFF_box.sizePolicy().hasHeightForWidth())

        
        self.auto_ONOFF_box.setSizePolicy(sizePolicy)
        self.auto_ONOFF_box.setText("")
        self.auto_ONOFF_box.setIconSize(QtCore.QSize(16, 16))
        self.auto_ONOFF_box.setChecked(True)
        self.auto_ONOFF_box.setObjectName("auto_ONOFF_box")

        
        self.horizontalLayout.addWidget(self.auto_ONOFF_box, 0, QtCore.Qt.AlignHCenter)

        
        spacerItem5 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)

        
        self.horizontalLayout.addItem(spacerItem5)

        
        self.auto_ON = QtWidgets.QRadioButton(self.centralwidget)

        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.auto_ON.sizePolicy().hasHeightForWidth())

        
        self.auto_ON.setSizePolicy(sizePolicy)
        self.auto_ON.setAutoFillBackground(False)
        self.auto_ON.setText("")
        self.auto_ON.setChecked(True)
        self.auto_ON.setObjectName("auto_ON")

        
        self.horizontalLayout.addWidget(self.auto_ON, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.horizontalLayout)

        
        MainWindow.setCentralWidget(self.centralwidget)

        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label_2.setText(_translate("MainWindow", "Off"))
        self.label.setText(_translate("MainWindow", "Auto"))
        self.label_3.setText(_translate("MainWindow", "On"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

