# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plancheUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(613, 307)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.bp_last = QtGui.QPushButton(self.centralwidget)
        self.bp_last.setGeometry(QtCore.QRect(70, 210, 41, 27))
        self.bp_last.setObjectName(_fromUtf8("bp_last"))
        self.bp_next = QtGui.QPushButton(self.centralwidget)
        self.bp_next.setGeometry(QtCore.QRect(120, 210, 41, 27))
        self.bp_next.setObjectName(_fromUtf8("bp_next"))
        self.bp_new = QtGui.QPushButton(self.centralwidget)
        self.bp_new.setGeometry(QtCore.QRect(170, 210, 121, 27))
        self.bp_new.setObjectName(_fromUtf8("bp_new"))
        self.bp_save = QtGui.QPushButton(self.centralwidget)
        self.bp_save.setGeometry(QtCore.QRect(300, 210, 85, 27))
        self.bp_save.setObjectName(_fromUtf8("bp_save"))
        self.bp_sup = QtGui.QPushButton(self.centralwidget)
        self.bp_sup.setGeometry(QtCore.QRect(390, 210, 141, 27))
        self.bp_sup.setObjectName(_fromUtf8("bp_sup"))
        self.line_nom = QtGui.QLineEdit(self.centralwidget)
        self.line_nom.setGeometry(QtCore.QRect(160, 50, 113, 27))
        self.line_nom.setObjectName(_fromUtf8("line_nom"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 50, 111, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 91, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.line_longueur = QtGui.QLineEdit(self.centralwidget)
        self.line_longueur.setGeometry(QtCore.QRect(160, 90, 113, 27))
        self.line_longueur.setObjectName(_fromUtf8("line_longueur"))
        self.line_largeur = QtGui.QLineEdit(self.centralwidget)
        self.line_largeur.setGeometry(QtCore.QRect(160, 130, 113, 27))
        self.line_largeur.setObjectName(_fromUtf8("line_largeur"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 130, 91, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_surface = QtGui.QLabel(self.centralwidget)
        self.label_surface.setGeometry(QtCore.QRect(300, 110, 201, 17))
        self.label_surface.setObjectName(_fromUtf8("label_surface"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(290, 90, 3, 61))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 613, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Gestion des planches", None))
        self.bp_last.setText(_translate("MainWindow", "<<", None))
        self.bp_next.setText(_translate("MainWindow", ">>", None))
        self.bp_new.setText(_translate("MainWindow", "Nouvelle planche", None))
        self.bp_save.setText(_translate("MainWindow", "Enregistrer", None))
        self.bp_sup.setText(_translate("MainWindow", "Supprimer la planche", None))
        self.label.setText(_translate("MainWindow", "Nom de la planche", None))
        self.label_2.setText(_translate("MainWindow", "Longueur (m):", None))
        self.label_3.setText(_translate("MainWindow", "Largeur (m):", None))
        self.label_surface.setText(_translate("MainWindow", "La surface de la planche est de:", None))

