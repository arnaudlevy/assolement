#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 09:51:58 2018

@author: cedric
"""
from PyQt4 import QtGui, QtCore
import sys
from fonctionFC import *

import actionUI

import sqlite3


class Action():
    def __init__(self,id_action):
        self.id_action = id_action
        self.nom = 'New action'
        self.dataAction ={}
        
        if id_action > 0:
            self.lireAction(id_action)
        
    def data(self):
        #ecrire les données de l'objet dans un dictionnaire pour la bdd
        print 'data'
        self.dataAction['id_action']= self.id_action
        self.dataAction['nom']= str(self.nom)

        
    def lireAction(self,id_action):
        print 'lireData'
        self.id_action = id_action
        ouvrirBase()
        cursor.execute("""SELECT id_action, nom FROM action WHERE id_action=?""", (id_action,))
        response = cursor.fetchone()
        
        self.nom = response[1]

        fermerBase()
        
    def ecrireAction(self):
        print 'ecrireData'
        
        self.data()
                
        ouvrirBase()
        cursor.execute("""UPDATE action SET nom = :nom WHERE id_action = :id_action""", self.dataAction)
        conn.commit()
        
        fermerBase() 

        
    def supAction(self):
        print 'supAction'
        id_action = int(self.id_action)
        ouvrirBase()
        cursor.execute("""DELETE FROM action WHERE (((action.id_action)=?))""", (id_action,))
        fermerBase()

    def newAction(self):
        print 'newAction'
        self.nom = 'New Action'
       
        self.data()
       
        ouvrirBase()
        cursor.execute("""INSERT INTO action (nom) VALUES(:nom)""", self.dataAction)
        conn.commit()

        return(cursor.lastrowid)        

        
        
class formAction(QtGui.QWidget, actionUI.Ui_Form):
    def __init__(self, parent = None):
        super(formAction, self).__init__(parent)
        self.setupUi(self)
        self.connectActions()
        self.positionList = 0
        self.action_active = Action(self.positionList)
        self.idAction = ''
        self.nbAction = 0
        self.dataAction ={}
        self.tableAction = []
        
        self.parcoursList()
        self.lireAction()
                

        
        
    def parcoursList(self):
        print 'parcoursList'
        ouvrirBase()
        cursor.execute("""SELECT id_action, nom FROM action ORDER BY nom""")
        self.tableAction = cursor.fetchall()
               
        cursor.execute("""SELECT COUNT(id_action) FROM action""")
        self.nbAction = cursor.fetchone()[0]
        fermerBase()
        
       
        
    def connectActions(self):
        self.bp_prevAction.clicked.connect(self.prevAction)
        self.bp_nextAction.clicked.connect(self.nextAction)
        self.bp_newAction.clicked.connect(self.newAction)
        self.bp_supAction.clicked.connect(self.supAction)
        self.bp_saveAction.clicked.connect(self.saveAction)
       
              
    def saveAction(self):
        print 'saveAction'
        self.lectureChamps()

        self.action_active.ecrireAction()
             

        
    def prevAction(self):
        print'prevAction'
       
        if self.positionList == 0 :
            print "on est au début"
            return
        
        self.positionList = self.positionList - 1                
        self.lireAction()
        
        
    def nextAction(self):
        print 'nextAction'
        self.parcoursList()
        
        if self.positionList > self.nbAction -2 :
            print "c'est la derniere action"
            self.positionList = self.nbAction - 2
            return
        
        self.positionList = self.positionList + 1
        self.lireAction()

        
    def lireAction(self):
        id_action = self.tableAction[self.positionList][0]
    
        self.action_active.lireAction(id_action)
        self.ecritureChamps()
        

        
    def newAction(self):
        print 'newAction'
        newAction = self.action_active.newAction()
        self.action_active = Action(newAction)
        self.action_active.id_action = newAction
        self.positionList = newAction
        
        self.parcoursList()
        self.ecritureChamps()        
       

        


        
    def supAction(self):       
        self.action_active.supAction()
               
        self.parcoursList()
        self.prevAction()
         
        
    def savedata(self):
        #ecrire les données de l'objet dans un dictionnaire pour la bdd
        print 'data'
        self.dataAction['id_action']= self.action_active.numId
        self.dataAction['nom']= str(self.action_active.nom)

      
        
    
    def ecritureChamps(self):
        print 'ecriture champs'
        self.line_actionNom.setText(self.action_active.nom)
    


    def lectureChamps(self):
        print 'lecture champs'
        self.action_active.nom = str(self.line_actionNom.text())
  
              


        
        
        
        
    def main(self):
        
        self.show()

    


        
if __name__ == '__main__':
    
    app = QtGui.QApplication(sys.argv)
    toto = formAction()
    toto.main()
    app.exec_()
