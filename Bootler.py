# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Bootler.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import pyqtgraph as pg
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

############### For debuging ##################
global devID
devID = "Temperature"
global daTx
daTx = np.random.normal(size=(10,1000))
global curve,data,ptr
data = daTx
ptr = 0
###############################################

global gCount
gCount = 0


class Ui_MainWindow(object):
    global daTx
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
        MainWindow.setStyleSheet("background-color:#dccdc;")

        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

# Bootler Button
# widget and button

        self.widget_bootbtn = QtWidgets.QWidget(self.centralwidget)
        self.widget_bootbtn.setMinimumSize(QtCore.QSize(91, 91))
        self.widget_bootbtn.setMaximumSize(QtCore.QSize(91, 91))
        self.widget_bootbtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_bootbtn.setObjectName("widget_bootbtn")

        
        self.bootButton = QtWidgets.QPushButton(self.widget_bootbtn)
        self.bootButton.setGeometry(QtCore.QRect(0, 0, 91, 91))
        self.bootButton.setMinimumSize(QtCore.QSize(91, 91))
        self.bootButton.setMaximumSize(QtCore.QSize(91, 91))
        self.bootButton.setText("")
        self.bootButton.setObjectName("bootButton")
        self.bootButton.setIcon(QIcon('pic.png'))
        self.bootButton.setIconSize(QSize(65,65));
        self.bootButton.setStyleSheet("background-color:#cdc9c9;");

        
        self.verticalLayout.addWidget(self.widget_bootbtn, 0, QtCore.Qt.AlignHCenter)

# End of Bootler Button

        
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)

        
        self.verticalLayout.addItem(spacerItem)
        
# Temperature Button
# widget and button
# its widget_3 > widget > tempButton
        
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

        
        self.tempButton = QtWidgets.QPushButton(self.widget)
        self.tempButton.setGeometry(QtCore.QRect(0, 0, 91, 91))
        self.tempButton.setMinimumSize(QtCore.QSize(91, 91))
        self.tempButton.setMaximumSize(QtCore.QSize(91, 91))
        self.tempButton.setStyleSheet("")
        self.tempButton.setText("")
        self.tempButton.setObjectName("tempButton")
        self.tempButton.setIcon(QIcon('tmp.png'))
        self.tempButton.setIconSize(QSize(65,65));
        self.tempButton.setCheckable(True)
        self.tempButton.clicked.connect(self.temp_Clicked)
        self.tempButton.setStyleSheet("background-color:#cdc9c9;;");

        
        self.verticalLayout.addWidget(self.widget_3, 0, QtCore.Qt.AlignHCenter)

# End Temperature Button

        
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)

        
        self.verticalLayout.addItem(spacerItem1)

# Luminesence Button
# widget and button
        
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setMinimumSize(QtCore.QSize(91, 91))
        self.widget_4.setMaximumSize(QtCore.QSize(91, 91))
        self.widget_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_4.setObjectName("widget_4")

        
        self.lumiButton = QtWidgets.QPushButton(self.widget_4)
        self.lumiButton.setGeometry(QtCore.QRect(0, 0, 91, 91))
        self.lumiButton.setMinimumSize(QtCore.QSize(91, 91))
        self.lumiButton.setMaximumSize(QtCore.QSize(91, 91))
        self.lumiButton.setText("")
        self.lumiButton.setObjectName("lumiButton")
        self.lumiButton.setIcon(QIcon('depth.png'))
        self.lumiButton.setIconSize(QSize(65,65));
        self.lumiButton.setStyleSheet("background-color:#cdc9c9;;");

        
        self.verticalLayout.addWidget(self.widget_4, 0, QtCore.Qt.AlignHCenter)

# End Luminesence Button

        
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

# Auto managment layout
        
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

# End of Auto Management layout
        
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
    


    def temp_Clicked(self):
        global gCount
        if gCount == 0:
            self.make_Ugraph_window(devID)
            gCount += 1
        else:
            update_Ugraph_window()
            gCount += 1
        if self.tempButton.isChecked:
            self.tempButton.setChecked(False)
            if gCount == 1:
                self.kill_Ugraph_window()
        else:
            self.tempButton.setChecked(True)

    def make_Ugraph_window(self, devID):
        global daTx
        self.win = pg.GraphicsWindow(title="Graphics")
        self.win.resize(800,600)
        self.win.setWindowTitle('Plotting sensor '+devID)
        self.call_Ugraph(devID, daTx)

    def update_Ugraph_window():
        if gCount < 2:
            self.win.resize(800,1200)
        else:
            self.win.resize(800,600)
            
    def kill_Ugraph_window(self):
            try:
                self.win.hide
            except Exception as e:
                print(str(e))
    def call_Ugraph(self, devID, daTx):
        global curve,data,ptr
        global p6
        try:
            p6 = self.win.addPlot(title="Sensor "+devID)
            curve = p6.plot(pen='y')
            data = daTx
            ptr = 0
            timer = QtCore.QTimer()
            timer.timeout.connect(self.update)
            timer.start(50)
            p6.plot(daTx)
        except Exception as e:
            print(str(e))
        
    def update():
       global curve, data, ptr, p6,daTx
       daTx = np.random.normal(size=(10,1000))
       curve.setData(data[ptr%10])
       if ptr == 0:
           p6.enableAutoRange('xy', False)  ## stop auto-scaling after the first data set is plotted
       ptr += 1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



