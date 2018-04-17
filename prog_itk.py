#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 09:51:58 2018

@author: cedric
"""
from PyQt4 import QtGui, QtCore
import sys

import itkUI
from itk import *
from plante import *
from action import *
from fonctionFC import *

from affichage import PlanningPlante, PlanningAction

import sqlite3

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
    

        

class formItk(QtGui.QWidget, itkUI.Ui_Form):
    def __init__(self, parent = None):
        super(formItk, self).__init__(parent)
        self.setupUi(self)
        self.connectActions()
        self.nbItk = 1
        self.lastId = 0
        self.dataItk ={}
        self.tablePlante = []
        self.tableAction = []
        self.tablePlantation = []
        self.dataPlantation = {}
        self.dataIntervention = {}
        self.linePlante = 1
        self.lineAction = 1
        self.planningPlante = PlanningPlante()
        self.planningAction = PlanningAction()
        self.plantePlantee_active = PlantePlantee(1,1,1)
        self.actionProgrammee_active = ActionProgrammee(1,1,1,1)
        
        self.positionList = 0
        self.parcoursList()
        self.id_itk =self.trouveIdItk(self.positionList)
        self.itk_active = Itk()
        self.itk_active.lireItk(self.id_itk)
        
        self.affichage()
        self.rechargeItk()
        
 
        
    def trouveIdItk(self,line):
        id_itk = self.tableItk[line][0]
        return(id_itk)
        
    def trouveIdPlante(self,line):
        id_plante = self.tablePlante[line][0]
        return(id_plante)

    def trouveLinePlante(self,id_plante):
        line = 0
        for id in self.tablePlante:
            if id_plante == self.tablePlante[line][0]:
                return(line)
            line = line + 1
        
    def trouveIdAction(self,line):
        id_action = self.tableAction[line][0]
        return(id_action)
        
    def trouveLineAction(self,id_action):
        line = 0
        for id in self.tableAction:
            if id_action == self.tableAction[line][0]:
                return(line)
            line = line + 1
        


    def rechargeItk(self):
        self.lirePlante()
        self.lireAction()
        self.maj_plante()
        self.maj_action()
        self.lirePlantation(self.id_itk)
        self.lireIntervention(self.id_itk)
        self.ecritureChamps()
        self.itk_active.plantation.lirePlantes(self.itk_active.id_itk)
        self.itk_active.intervention.lireActions(self.itk_active.id_itk)

        self.majAffichage(1)
               
        
    def parcoursList(self):
        print 'parcoursList'
        ouvrirBase()
        
        cursor.execute("""SELECT id_itk, nom FROM itk ORDER BY nom""")
        self.tableItk = cursor.fetchall()
        
        cursor.execute("""SELECT COUNT(id_itk) FROM itk""")
        response = cursor.fetchone()
        self.nbItk = response[0]
        
        fermerBase()
        
        
#_____________Bouton______________        
        
        
    def connectActions(self):
        self.bp_prevItk.clicked.connect(self.prevItk)
        self.bp_nextItk.clicked.connect(self.nextItk)
        self.bp_newItk.clicked.connect(self.newItk)
        self.bp_supItk.clicked.connect(self.supItk)
        self.bp_saveItk.clicked.connect(self.saveItk)
        self.combo_idPlante.currentIndexChanged.connect(self.maj_plante)
        self.bp_savePlante.clicked.connect(self.savePlante)
        self.bp_addPlante.clicked.connect(self.addPlante)
        self.bp_supPlante.clicked.connect(self.supPlante)
        self.combo_idAction.currentIndexChanged.connect(self.maj_action)
        self.bp_saveAction.clicked.connect(self.saveAction)
        self.bp_addAction.clicked.connect(self.addAction)
        self.bp_supAction.clicked.connect(self.supAction)
        self.bp_plante.clicked.connect(self.affichePlante)
        self.bp_action.clicked.connect(self.afficheAction)
        

#_________BP Plante
        
    def savePlante(self):
        print 'savePlante'
        self.lectureChampsPlante()
        id_plantation = self.itk_active.plantation.tablePlantation[self.linePlante][0]
        
        self.plantePlantee_active.save(id_plantation)
        self.itk_active.lireItk(self.id_itk)
        self.rechargeItk()
    
        
    def addPlante(self):
        print 'addPlante'
        self.itk_active.plantation.addPlante(self.id_itk)
        self.rechargeItk()

    def supPlante(self):
        print 'supPlante'
        numId = int(self.trouveIdPlante(self.combo_nomPlante.currentIndex()))
        self.itk_active.plantation.supPlante(numId)
        self.rechargeItk()
       
#_________BP Action_________

    def saveAction(self):
        print 'saveAction'
        self.lectureChampsInterv()
        id_intervention = self.itk_active.intervention.tableAction[self.lineAction][0]
        self.actionProgrammee_active.save(id_intervention)
        self.itk_active.lireItk(self.id_itk)
        self.rechargeItk()
    
        
    def addAction(self):
        print 'addAction'
        self.itk_active.intervention.addAction(self.id_itk)
        self.rechargeItk()

    def supAction(self):
        print 'supAction'
        numId = int(self.trouveIdAction(self.combo_nomAction.currentIndex()))
        self.itk_active.intervention.supAction(numId)
        self.rechargeItk()

#___________BP Itk__________
              
    def saveItk(self):
        print 'saveItk'
        self.lectureChampsItk()
        self.itk_active.ecrireItk()

        
    def prevItk(self):
        print'prevItk'
        self.parcoursList()
       
        if self.positionList == 0 :
            print "on est au début"
            return
        
        self.positionList = self.positionList - 1
        self.afficheItk()
        
        
    def nextItk(self):
        print 'nextItk'
        self.parcoursList()
        
        if self.positionList > self.nbItk - 2:
            print "c'est la derniere Itk"
            self.positionList = self.nbItk - 2
            return
        
        self.positionList = self.positionList + 1
        self.afficheItk()

        
    def afficheItk(self):
        print 'affiche Itk'
        id_itk = self.trouveIdItk(self.positionList)
        print 'id_itk=' + str(id_itk)
        self.itk_active.lireItk(id_itk)
        self.id_itk = id_itk
        self.rechargeItk()
        
        

        
    def newItk(self):
        print 'newItk'
                      
        lastId = self.itk_active.newItk()
        self.itk_active = Itk(lastId)
        self.itk_active.id_itk = lastId
        self.positionList = lastId
        
        self.data()       
        self.parcoursList()

        self.rechargeItk()
        
         

        
    def supItk(self):       
        self.itk_active.supItk()
        print 'supItk'
        self.prevItk()
        self.parcoursList()

    
    def affichePlante(self):
        self.appPlante = QtGui.QWidget()
        self.uiPlante = formPlante()
        self.uiPlante.main()
        self.uiPlante.show()

        
    def afficheAction(self):
        self.appAction = QtGui.QWidget()
        self.uiAction = formAction()
        self.uiAction.main()
        self.uiAction.show()
        
      

#_________________Plante_______________        

    def lirePlante(self):
        print 'lirePlante'
        ouvrirBase()
        cursor.execute("""SELECT id_plante, nom FROM plante ORDER BY nom""")
        self.tablePlante = cursor.fetchall()
        fermerBase()
        self.combo_nomPlante.clear()
        for id in self.tablePlante:
            self.combo_nomPlante.addItem(id[1])
            #print str(id[0]) + '-' + str(id[1])
            
    def lectureChampsPlante(self):
        print 'lecture champs plante'
        self.linePlante = self.combo_idPlante.currentIndex()
        #lit données plantation et initialise l'objet
        self.plantePlantee_active.id_itk =  int(self.itk_active.id_itk)
        
        numId = int(self.trouveIdPlante(self.combo_nomPlante.currentIndex()))
        self.plantePlantee_active.plante = Plante(numId)
        self.plantePlantee_active.date_semis = int(self.line_semPlant.text())


        
    def lirePlantation(self,fk_id_itk):
        print 'lirePlantation'
        
        self.itk_active.plantation.lirePlantes(fk_id_itk)
        self.combo_idPlante.clear()
        line = 1
        for id in self.itk_active.plantation.tablePlantation:
            self.combo_idPlante.addItem(str(line))
            line = line + 1

                
    def maj_plante(self):
        print 'maj_plante'
        numLine = self.combo_idPlante.currentIndex()
        
        if self.itk_active.plantation.tablePlantation == []:
            print 'pas de plante'
            return
        numPlante = self.trouveLinePlante(self.itk_active.plantation.tablePlantation[numLine][2])
        self.combo_nomPlante.setCurrentIndex(int(numPlante))
        self.line_semPlant.setText(str(self.itk_active.plantation.tablePlantation[numLine][3]))
    
        
        
#_________________Action_______________

    def lireAction(self):
        print 'lireAction'
        ouvrirBase()
        cursor.execute("""SELECT id_action, nom FROM action ORDER BY nom""")
        self.tableAction = cursor.fetchall()
        fermerBase()
        self.combo_nomAction.clear()
        for id in self.tableAction:
            self.combo_nomAction.addItem(id[1])
            
            
    def lectureChampsInterv(self):
        print 'lecture champs action'
        self.lineAction = self.combo_idAction.currentIndex()
        #lit données plantation et initialise l'objet
        self.actionProgrammee_active.id_itk =  int(self.itk_active.id_itk)
        id_action = int(self.trouveIdAction(self.combo_nomAction.currentIndex()))
        self.actionProgrammee_active.action = Action(id_action)
        self.actionProgrammee_active.date = int(self.line_semAction.text())
        self.actionProgrammee_active.duree = int(self.line_dureeAction.text())

        
            
    def lireIntervention(self,fk_id_itk):
        print 'lireAction'
        
        self.itk_active.intervention.lireActions(fk_id_itk)
        self.combo_idAction.clear()
        line = 1
        for id in self.itk_active.intervention.tableAction:
            self.combo_idAction.addItem(str(line))
            line = line + 1

            
    def maj_action(self):
        print 'maj_action'
        numLine = self.combo_idAction.currentIndex()
        
        if self.itk_active.intervention.tableAction == []:
            print 'pas de plante'
            return
        numAction = self.trouveLineAction(self.itk_active.intervention.tableAction[numLine][2])

        self.combo_nomAction.setCurrentIndex(int(numAction))
        self.line_semAction.setText(str(self.itk_active.intervention.tableAction[numLine][3]))
        self.line_dureeAction.setText(str(self.itk_active.intervention.tableAction[numLine][4]))
        
        
        
        
#______________Affichage____________________              
        
    
    def ecritureChamps(self):
        print 'ecriture champs'
        self.line_nomIti.setText(self.itk_active.nom)


    def lectureChampsItk(self):
        print 'lecture champs'
        self.itk_active.nom = str(self.line_nomIti.text())
        self.dataItk['id_itk']= self.id_itk
        self.dataItk['nom']= str(self.line_nomIti.text())
    
        
    def affichage(self):
        print 'affichagePlante'
        
        largeur = 950
        firstFrame = 20
        marge = 50
        semaineAvant = 5
        semaineApres = 5
        epPlante = 20
        self.itk_active.lirePlante()
        nbPlante = self.itk_active.plantation.nbPlante
        nb_semaine = 52 + semaineAvant + semaineApres
        hFramePlante = (nbPlante ) * epPlante

        nbAction = 1
        hFrameAction = (nbAction ) * epPlante
        
        yFrameAction = firstFrame + hFramePlante + firstFrame / 4

        
        #Label Plante
        self.label_plante = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_plante.setText("Plante")

        
        #Frame zone plante
        self.zonePlante2 = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.zonePlante2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.zonePlante2.setFrameShadow(QtGui.QFrame.Raised)
        self.qp_Plante = QtGui.QPainter(self.scrollAreaWidgetContents)

        self.planningPlante = PlanningPlante(self.zonePlante2)
        self.planningPlante.itk_active = self.itk_active
        self.planningPlante.hauteur= hFramePlante
        self.planningPlante.largeur = largeur
        self.planningPlante.epPlante = epPlante
        self.planningPlante.nb_semaine = nb_semaine
        self.planningPlante.semaineAvant = semaineAvant
        #self.planningPlante.maj_affichage()
        
        
        #Label Action
        self.label_action = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_action.setText("Action")
        
        self.zoneAction = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.zoneAction.setFrameShape(QtGui.QFrame.StyledPanel)
        self.zoneAction.setFrameShadow(QtGui.QFrame.Raised)
        self.qp_Action = QtGui.QPainter(self.zoneAction)
        
        self.planningAction = PlanningAction(self.zoneAction)
        self.planningAction.itk_active = self.itk_active
        self.planningAction.hauteur= hFrameAction
        self.planningAction.largeur = largeur
        self.planningAction.epAction = epPlante
        self.planningAction.nb_semaine = nb_semaine
        self.planningAction.semaineAvant = semaineAvant
        #self.planningAction.maj_affichage()
        

    
        
    def  majAffichage(self,event):
        print 'majAffichage'
        largeur = 950
        firstFrame = 20
        marge = 50
        epPlante = 20
        self.itk_active.plantation.lirePlantes(self.itk_active.id_itk)
        nbPlante = self.itk_active.plantation.nbPlante
        
        self.itk_active.intervention.lireActions(self.itk_active.id_itk)
        nbAction = self.itk_active.intervention.nbAction
        
        hFramePlante = (nbPlante + 1.1) * epPlante

        hFrameAction = (nbAction + 1) * epPlante
        
        yFrameAction = firstFrame + hFramePlante + firstFrame / 4

   
        self.zonePlante2.setGeometry(QtCore.QRect(marge, firstFrame, largeur, hFramePlante))
        self.label_plante.setGeometry(QtCore.QRect(10, firstFrame, 40, 20))

        self.zoneAction.setGeometry(QtCore.QRect(marge, yFrameAction, largeur, hFrameAction))
        self.label_action.setGeometry(QtCore.QRect(10, yFrameAction, 40, 20))

        
        self.planningPlante.itk_active = self.itk_active
        self.planningPlante.maj_affichage(event)
        self.planningPlante.update()
        
        self.planningAction.itk_active = self.itk_active
        self.planningAction.maj_affichage(event)
        self.planningAction.update()
        

        
    def paintEvent(self, event):
        self.update()
        

        
    def main(self):
        self.show()
 

            
        
        
        

        
        
        
if __name__ == '__main__':
    
    app = QtGui.QApplication(sys.argv)
    toto = formItk()
    toto.main()
    app.exec_()
    sys.exit(app.exec_())
