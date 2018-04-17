# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listingActionUI.ui'
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
        Form.resize(692, 632)
        self.tableView = QtGui.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(20, 80, 631, 501))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 50, 201, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.BP_recharge = QtGui.QPushButton(Form)
        self.BP_recharge.setGeometry(QtCore.QRect(30, 590, 85, 27))
        self.BP_recharge.setObjectName(_fromUtf8("BP_recharge"))
        self.BP_print = QtGui.QPushButton(Form)
        self.BP_print.setGeometry(QtCore.QRect(140, 590, 121, 27))
        self.BP_print.setObjectName(_fromUtf8("BP_print"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Listing des actions", None))
        self.label.setText(_translate("Form", "Listing des actions", None))
        self.BP_recharge.setText(_translate("Form", "Recharger", None))
        self.BP_print.setText(_translate("Form", "Générer Pdf", None))

