#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 10:36:25 2018

@author: cedric
"""

from PyQt4 import QtGui, QtCore
import sys

import ZODB
from ZODB.FileStorage import FileStorage
from ZODB.DB import DB
from ZODB.PersistentMapping import PersistentMapping

import persistent
import transaction


import plancheUI

class Planche(persistent.Persistent):
    def __init__(self,numId):
        self.numId = numId
        self.nom = ''
        self.longueur = 0.1
        self.largeur = 0.1
        self.surface = 0.1

        
class formPlanche(QtGui.QMainWindow, plancheUI.Ui_MainWindow):
    def __init__(self, parent = None):
        super(formPlanche,self).__init__(parent)
        self.setupUi(self)
        self.connectActions()
        self.planche_active = Planche('')
        self.nb_planche = 0
        self.positionList =0
        self.listePlanche =[]
        
        self.parcoursList()
        


        
        
    def connectActions(self):
        self.bp_last.clicked.connect(self.last)
        self.bp_next.clicked.connect(self.nextobj)
        self.bp_new.clicked.connect(self.new)
        self.bp_sup.clicked.connect(self.sup)
        self.bp_save.clicked.connect(self.save)        
        

    def parcoursList(self):
        self.nb_planche = 0
        self.listePlanche = []
        if len(planches)==0:
            print "il n'y a pas de planche"
            return
           
        for planche in planches.values():
            self.listePlanche.append(planche.numId)
            self.nb_planche = self.nb_planche + 1 
        
        print "nombre de planche:" + str(self.nb_planche)
        print self.listePlanche



    def save(self):
        self.lectureChamps()
        
        numId = self.positionList
        del(planches[numId])
        root['planches'] = planches
        
        transaction.commit()        
        
        print "planche en cours " + self.planche_active.nom
        
        self.planche_active.numId = numId
        
         
        planches[numId] = self.planche_active
        
        transaction.commit()
        
        self.parcoursList()
        
        print "Planche modifiée" + str(numId)

        
        
    def last(self):
        self.parcoursList()
        if self.positionList == 0 :
            print "on est au début"
            return
        
        self.positionList = self.positionList - 1
        numId = self.positionList
                
        self.planche_active = planches[numId]
        self.ecritureChamps()
 
              
        
        
    def nextobj(self):
        self.parcoursList()
        
        if self.positionList > (self.nb_planche-1):
            print "c'est la derniere planche"
            self.positionList = self.nb_planche -1
            return
        
        self.positionList = self.positionList + 1
        numId = self.positionList
        
        self.planche_active = planches[numId]
        self.ecritureChamps()
        print 'position ' + str(self.positionList)
        
        
    def new(self):
        self.line_nom.setText("new planche")
        self.lectureChamps()
        
        numId = self.nb_planche
        
        planches[numId] = Planche(numId)
        
        root["planches"] = planches
        transaction.commit()
        self.parcoursList()
        print "Planche ajoutée"
        
    def sup(self):
        numId = self.positionList
        
        pl =root['planches']     
        del(pl[numId])
        root['planches'] = pl
        
        
        transaction.commit()
        
        planches = root['planches']
        
        self.parcoursList()
        self.lastPlanche()
        
    
    def ecritureChamps(self):
        print 'ecriture champs'
        self.line_nom.setText(self.planche_active.nom)
        self.line_longueur.setText(str(self.planche_active.longueur))
        

    def lectureChamps(self):
        print 'lecture champs'
        self.planche_active.nom = self.line_nom.text()
        self.planche_active.longueur = self.line_longueur.text()
        
        
        
    def main(self):
        
        self.show()
        


        
# setup the database
storage=FileStorage("planche.fs")
db=DB(storage)
connection=db.open()
root=connection.root()        

# get the employees mapping, creating an empty mapping if
# necessary
if not root.has_key("planches"):
    root["planches"] = {}
planches=root["planches"]
        
def toto():
    toto = 1


        
        
        
        
if __name__ == '__main__':
    
    app = QtGui.QApplication(sys.argv)
    ApPlanche = formPlanche()
    ApPlanche.main()
    app.exec_()
    
            