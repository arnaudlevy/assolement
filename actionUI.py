# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'actionUI.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(557, 197)
        self.centralwidget = QtGui.QWidget(Form)
        self.centralwidget.setGeometry(QtCore.QRect(0, 30, 561, 167))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.bp_prevAction = QtGui.QPushButton(self.centralwidget)
        self.bp_prevAction.setGeometry(QtCore.QRect(20, 100, 41, 27))
        self.bp_prevAction.setObjectName(_fromUtf8("bp_prevAction"))
        self.bp_nextAction = QtGui.QPushButton(self.centralwidget)
        self.bp_nextAction.setGeometry(QtCore.QRect(70, 100, 41, 27))
        self.bp_nextAction.setObjectName(_fromUtf8("bp_nextAction"))
        self.bp_newAction = QtGui.QPushButton(self.centralwidget)
        self.bp_newAction.setGeometry(QtCore.QRect(120, 100, 111, 27))
        self.bp_newAction.setObjectName(_fromUtf8("bp_newAction"))
        self.bp_supAction = QtGui.QPushButton(self.centralwidget)
        self.bp_supAction.setGeometry(QtCore.QRect(240, 100, 171, 27))
        self.bp_supAction.setObjectName(_fromUtf8("bp_supAction"))
        self.bp_saveAction = QtGui.QPushButton(self.centralwidget)
        self.bp_saveAction.setGeometry(QtCore.QRect(420, 100, 121, 27))
        self.bp_saveAction.setObjectName(_fromUtf8("bp_saveAction"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 71, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.line_actionNom = QtGui.QLineEdit(self.centralwidget)
        self.line_actionNom.setGeometry(QtCore.QRect(100, 40, 401, 27))
        self.line_actionNom.setObjectName(_fromUtf8("line_actionNom"))
        self.menubar = QtGui.QMenuBar(Form)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 557, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.statusbar = QtGui.QStatusBar(Form)
        self.statusbar.setGeometry(QtCore.QRect(0, 0, 3, 22))
        self.statusbar.setObjectName(_fromUtf8("statusbar"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Action", None))
        self.bp_prevAction.setText(_translate("Form", "<<", None))
        self.bp_nextAction.setText(_translate("Form", ">>", None))
        self.bp_newAction.setText(_translate("Form", "Nouvelle action", None))
        self.bp_supAction.setText(_translate("Form", "Supprimer l\'action en cours", None))
        self.bp_saveAction.setText(_translate("Form", "Enregistre l\'action", None))
        self.label.setText(_translate("Form", "Nom action", None))

