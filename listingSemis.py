#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 15:21:44 2018

@author: cedric
"""


from PyQt4 import QtGui, QtCore

import sys
from PyQt4.QtGui import QPainter, QPen
from PyQt4.QtCore import Qt

from itk import *
from fonctionFC import *

import listingSemisUI

import sqlite3

class MyModel(QtGui.QStandardItemModel):
 
    def data(self, index, role):
        value = QtGui.QStandardItemModel.data(self, index, role)        
        if role == QtCore.Qt.TextColorRole and index.column() == 1:
            return QtCore.QVariant(QtGui.QColor(QtCore.Qt.blue))
        return value
 
class Tableau:
    def __init__(self, nb_ligne):
        self.nb_ligne = nb_ligne
        self.nb_colonne = 4
        self.model=QtGui.QStandardItemModel(self.nb_ligne, self.nb_colonne)
        self.table = []
        self.initialiseModel()
        
 
    def initialiseModel(self):
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, QtCore.QVariant("Num semaine"))
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, QtCore.QVariant("Plante"))
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, QtCore.QVariant("Nb plants"))
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, QtCore.QVariant("Poids graine"))


        line = 0
        for id in self.table:
            self.addValue(self.model.index(line, 0),str(self.table[line][0]))
            self.addValue(self.model.index(line, 1),str(self.table[line][1]))
            self.addValue(self.model.index(line, 2),str(int(self.table[line][2])))
            self.addValue(self.model.index(line, 3),str(round(self.table[line][3],2)))

            line = line + 1
            

            
 
    def addValue(self,index,value):
        self.model.setData(index,QtCore.QVariant(value))



        
class formListingSemis(QtGui.QMainWindow, listingSemisUI.Ui_Form):
    def __init__(self, parent = None):
        super(formListingSemis,self).__init__(parent)
        self.setupUi(self)
        self.connectActions()
        self.liste_semis()
        self.tableSemis = []
        
        
 
    def connectActions(self):
        self.BP_recharge.clicked.connect(self.liste_semis)
        self.BP_print.clicked.connect(self.imprimer)


        
    def imprimer(self):
        self.liste_semis()
        printer = QtGui.QPrinter()
        printer.setOutputFileName("listingSemis.pdf")
        painter = QtGui.QPainter()
        painter.begin(printer)
        
        pen = QPen(Qt.black, 1, Qt.SolidLine)
        painter.setPen(pen)
        marge = 20
        col1 = 100
        posCol2 = marge + col1
        col2 = 250
        posCol3 = posCol2 + col2
        col3 = 100
        posCol4 = posCol3 + col3
        col4 = 100
        fin = posCol4 + col4
        
        
        pasY = 20
        
        line = 0
        posY = line * pasY
        painter.drawLine(marge, posY,fin, posY)
        painter.setFont(QtGui.QFont('Decorative', 10))
        painter.drawText(marge + 5, posY + 15, 'Num semaine') 
        painter.drawText(posCol2 + 5, posY + 15, 'Plante') 
        painter.drawText(posCol3 + 5, posY + 15, 'NB plants')
        painter.drawText(posCol4 + 5, posY + 15, 'Poids graine') 
        
        
        
        
        
        for id in self.tableSemis:
            posY = (line + 1) * pasY
            painter.drawLine(marge, posY,fin, posY)
            painter.setFont(QtGui.QFont('Decorative', 10))
            painter.drawText(marge + 5, posY + 15, str(self.tableSemis[line][0])) 
            painter.drawText(posCol2 + 5, posY + 15, str(self.tableSemis[line][1])) 
            painter.drawText(posCol3 + 5, posY + 15, str(round(self.tableSemis[line][2],0)))
            painter.drawText(posCol4 + 5, posY + 15, str(round(self.tableSemis[line][3],2))) 
            
            
            line = line + 1
        
        
        painter.drawLine(marge, 0,marge, (line + 1) * pasY)
        painter.drawLine(posCol2, 0,posCol2, (line + 1) * pasY)
        painter.drawLine(posCol3, 0,posCol3, (line + 1) * pasY)
        painter.drawLine(posCol4, 0,posCol4, (line + 1) * pasY)
        painter.drawLine(fin, 0,fin, (line + 1) * pasY)
        painter.drawLine(marge, (line + 1) * pasY,fin, (line + 1) * pasY)
        
        
        painter.end()
        

    def liste_semis(self):
        
        ouvrirBase()
        
        cursor.execute("""SELECT 
            [main].[plantation].[date_semis], 
            [main].[plante].[nom], 
            SUM (([main].[planche].[longueur] / [main].[plante].[dist_x]) * ([main].[planche].[largeur] / [main].[plante].[dist_y])) AS [nb],
            SUM ((([main].[planche].[longueur] / [main].[plante].[dist_x]) * ([main].[planche].[largeur] / [main].[plante].[dist_y])) / [main].[plante].[graineparg]) AS [poids]
        FROM   [main].[plante]
            INNER JOIN [main].[plantation] ON [main].[plante].[id_plante] = [main].[plantation].[fk_id_plante]
            INNER JOIN [main].[itk] ON [main].[plantation].[fk_id_itk] = [main].[itk].[id_itk]
            INNER JOIN [main].[affectPlanche] ON [main].[itk].[id_itk] = [main].[affectPlanche].[fk_id_itk]
            INNER JOIN [main].[planche] ON [main].[affectPlanche].[fk_id_planche] = [main].[planche].[id_planche]
        WHERE  [main].[plante].[annuelle] = 1
        GROUP  BY
            [main].[plantation].[date_semis], 
            [main].[plante].[nom]
        """)
        self.tableSemis = cursor.fetchall()
        fermerBase()
        
        nb_ligne = len(self.tableSemis)
        
        
        self.tableau=Tableau(nb_ligne + 1)

        self.tableau.table = self.tableSemis
        self.tableau.initialiseModel()
        self.tableView.setModel(self.tableau.model)
        self.tableView.setColumnWidth(1, 250)

        
    def main(self):
        
        self.show()
        
        
        
        
        
if __name__ == '__main__':
    
    app = QtGui.QApplication(sys.argv)
    ApListing = formListingSemis()
    ApListing.main()
    app.exec_()
            
