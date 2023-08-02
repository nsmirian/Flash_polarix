# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'polarix_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(844, 645)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 20, 561, 411))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(580, 30, 231, 231))
        self.groupBox.setObjectName("groupBox")
        self.phase_min = QtWidgets.QLineEdit(self.groupBox)
        self.phase_min.setGeometry(QtCore.QRect(90, 50, 31, 22))
        self.phase_min.setObjectName("phase_min")
        self.phas_max = QtWidgets.QLineEdit(self.groupBox)
        self.phas_max.setGeometry(QtCore.QRect(90, 80, 31, 22))
        self.phas_max.setObjectName("phas_max")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 50, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 71, 21))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(30, 190, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setIconSize(QtCore.QSize(16, 19))
        self.pushButton.setObjectName("pushButton")
        self.phas_min2 = QtWidgets.QLineEdit(self.groupBox)
        self.phas_min2.setGeometry(QtCore.QRect(150, 50, 31, 22))
        self.phas_min2.setObjectName("phas_min2")
        self.phas_max2 = QtWidgets.QLineEdit(self.groupBox)
        self.phas_max2.setGeometry(QtCore.QRect(150, 80, 31, 22))
        self.phas_max2.setObjectName("phas_max2")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(20, 150, 191, 21))
        self.checkBox.setObjectName("checkBox")
        self.nshots = QtWidgets.QLineEdit(self.groupBox)
        self.nshots.setGeometry(QtCore.QRect(112, 170, 51, 22))
        self.nshots.setObjectName("nshots")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(50, 170, 60, 16))
        self.label_5.setObjectName("label_5")
        self.tpcolibration1 = QtWidgets.QLineEdit(self.groupBox)
        self.tpcolibration1.setGeometry(QtCore.QRect(90, 110, 31, 22))
        self.tpcolibration1.setObjectName("tpcolibration1")
        self.tpcolibration2 = QtWidgets.QLineEdit(self.groupBox)
        self.tpcolibration2.setGeometry(QtCore.QRect(150, 110, 31, 22))
        self.tpcolibration2.setObjectName("tpcolibration2")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(10, 110, 60, 16))
        self.label_10.setObjectName("label_10")
        self.phase_less_90 = QtWidgets.QCheckBox(self.groupBox)
        self.phase_less_90.setGeometry(QtCore.QRect(80, 20, 51, 21))
        self.phase_less_90.setObjectName("phase_less_90")
        self.phase_lar_90 = QtWidgets.QCheckBox(self.groupBox)
        self.phase_lar_90.setGeometry(QtCore.QRect(150, 20, 51, 21))
        self.phase_lar_90.setObjectName("phase_lar_90")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(590, 260, 231, 231))
        self.groupBox_2.setObjectName("groupBox_2")
        self.Ecolibration_bending = QtWidgets.QPushButton(self.groupBox_2)
        self.Ecolibration_bending.setGeometry(QtCore.QRect(10, 50, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Ecolibration_bending.setFont(font)
        self.Ecolibration_bending.setObjectName("Ecolibration_bending")
        self.Ecollibration_linac = QtWidgets.QPushButton(self.groupBox_2)
        self.Ecollibration_linac.setGeometry(QtCore.QRect(20, 130, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Ecollibration_linac.setFont(font)
        self.Ecollibration_linac.setObjectName("Ecollibration_linac")
        self.Delta_current_DC = QtWidgets.QLineEdit(self.groupBox_2)
        self.Delta_current_DC.setGeometry(QtCore.QRect(120, 20, 51, 22))
        self.Delta_current_DC.setObjectName("Delta_current_DC")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(40, 20, 61, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(180, 20, 60, 16))
        self.label_9.setObjectName("label_9")
        self.Delta_Vol_DC = QtWidgets.QLineEdit(self.groupBox_2)
        self.Delta_Vol_DC.setGeometry(QtCore.QRect(120, 100, 51, 22))
        self.Delta_Vol_DC.setObjectName("Delta_Vol_DC")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(20, 100, 101, 20))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(180, 100, 60, 16))
        self.label_12.setObjectName("label_12")
        self.Dispersion = QtWidgets.QLineEdit(self.groupBox_2)
        self.Dispersion.setGeometry(QtCore.QRect(100, 190, 61, 31))
        self.Dispersion.setObjectName("Dispersion")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(20, 200, 71, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(170, 200, 60, 16))
        self.label_14.setObjectName("label_14")
        self.xomment = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.xomment.setGeometry(QtCore.QRect(20, 450, 271, 151))
        self.xomment.setObjectName("xomment")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(300, 440, 271, 161))
        self.groupBox_3.setObjectName("groupBox_3")
        self.phas_min3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.phas_min3.setGeometry(QtCore.QRect(100, 30, 71, 22))
        self.phas_min3.setObjectName("phas_min3")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 30, 71, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(10, 60, 71, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit.setGeometry(QtCore.QRect(100, 60, 71, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 100, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 844, 21))
        self.menubar.setObjectName("menubar")
        self.menustirk_measurement = QtWidgets.QMenu(self.menubar)
        self.menustirk_measurement.setObjectName("menustirk_measurement")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menustirk_measurement.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "strik measurment"))
        self.label.setText(_translate("MainWindow", "min phase"))
        self.label_2.setText(_translate("MainWindow", "max phase"))
        self.pushButton.setText(_translate("MainWindow", "start measurement "))
        self.checkBox.setText(_translate("MainWindow", "n image shots be saved "))
        self.label_5.setText(_translate("MainWindow", "n shots"))
        self.tpcolibration1.setText(_translate("MainWindow", "1"))
        self.tpcolibration2.setText(_translate("MainWindow", "1"))
        self.label_10.setText(_translate("MainWindow", "time/pixel"))
        self.phase_less_90.setText(_translate("MainWindow", "<90"))
        self.phase_lar_90.setText(_translate("MainWindow", ">90"))
        self.groupBox_2.setTitle(_translate("MainWindow", "energy collibration "))
        self.Ecolibration_bending.setText(_translate("MainWindow", "measurement by Bending "))
        self.Ecollibration_linac.setText(_translate("MainWindow", "measurement by energy "))
        self.Delta_current_DC.setText(_translate("MainWindow", "20"))
        self.label_8.setText(_translate("MainWindow", "<p>&Delta; current "))
        self.label_9.setText(_translate("MainWindow", "A"))
        self.label_11.setText(_translate("MainWindow", "<p>&Delta; ACC67 Ampl"))
        self.label_12.setText(_translate("MainWindow", "MV"))
        self.Dispersion.setText(_translate("MainWindow", "0.8"))
        self.label_13.setText(_translate("MainWindow", "Dispersion"))
        self.label_14.setText(_translate("MainWindow", "mm/MeV"))
        self.groupBox_3.setTitle(_translate("MainWindow", "saving image "))
        self.label_6.setText(_translate("MainWindow", "min phase"))
        self.label_7.setText(_translate("MainWindow", "max phase"))
        self.pushButton_2.setText(_translate("MainWindow", "measurement "))
        self.menustirk_measurement.setTitle(_translate("MainWindow", "stirk measurement"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
