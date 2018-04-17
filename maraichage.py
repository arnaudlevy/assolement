#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 08:35:59 2018

@author: cedric
"""

from PyQt4 import QtGui, QtCore
import sys

import maraichageUI
from itk import *
from prog_itk import *
from plante import *
from action import *
from planche import *
from affichage import *
from listingSemis import *
from listingRecolte import *
from listingAction import *
from listingPlantation import *

from fonctionFC import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
        


        
class formAssolement(QtGui.QMainWindow, maraichageUI.Ui_MainWindow):
    def __init__(self, parent = None):
        super(formAssolement, self).__init__(parent)
        self.setupUi(self)
        self.connectActions()
        
        self.tableAffect = []
        self.tableItk =[]
        self.tablePlanche =[]
        
        self.lineItk = 1
        self.linePlanche = 1
        self.marge = 0
        
        
        self.toto = ''
        
        
        self.positionList = 0
        self.parcoursList()
        self.id_affect = self.trouveIdAffect(self.positionList) 
        self.affect_active = AffectPlanches()
        self.affect_active.lireAffect(self.tableAffect[self.positionList][1])
        
        self.listPlanning = []
        
        self.rechargeAffect()
        self.affichage()




        
    def rechargeAffect(self):
        self.lireItk()
        self.lirePlanche()
        print 'table itk=' + str(self.tableItk)
        print 'table planche' + str(self.tablePlanche)
        self.maj_itk()
        self.maj_planche()
        self.id_planche = self.trouveIdPlanche_IdAffect(self.id_affect)
        self.affect_active.lireAffect(self.id_planche)
        #self.affichage()
        

        
    def trouveIdAffect(self,line):
        id_affect = self.tableAffect[line][0]
        print str(id_affect)
        return(id_affect) 

    def trouveIdAffect_IdPlanche(self,id_planche):
        line=0
        for id in self.tableAffect:
            if id_planche == self.tableAffect[line][1]:
                return(self.tableAffect[line][0])
            line = line + 1

    def trouveIdPlanche_IdAffect(self,id_affect):
        line=0
        for id in self.tableAffect:
            if id_affect == self.tableAffect[line][0]:
                return(self.tableAffect[line][1])
            line = line + 1
        
        
    def trouveIdItk(self,line):
        id_itk = self.tableItk[line][0]
        return(id_itk) 
 
    
    def trouveLineItk(self,id_itk):
        print 'trouveLineItk'
        line = 0
        for id in self.tableItk:
            if id_itk == self.tableItk[line][0]:
                return(line)
            line = line + 1

    def trouveIdPlanche(self,line):
        id_planche = self.tablePlanche[line][0]
        return(id_planche) 
        
    
    def trouveLinePlanche(self,id_planche):
        line = 0
        for id in self.tablePlanche:
            if id_planche == self.tablePlanche[line][0]:
                return(line)
            line = line + 1
         
 
    def parcoursList(self):
        print 'parcoursList'
        ouvrirBase()
        
        cursor.execute("""
        SELECT 
            [main].[affectPlanche].[id_affect], 
            [main].[affectPlanche].[fk_id_planche], 
            [main].[affectPlanche].[fk_id_itk]
        FROM   [main].[affectPlanche]
            INNER JOIN [main].[planche] ON [main].[planche].[id_planche] = [main].[affectPlanche].[fk_id_planche]
        ORDER  BY [main].[planche].[nom]
        """)
        self.tableAffect = cursor.fetchall()
        
        cursor.execute("""SELECT COUNT(id_affect) FROM affectPlanche""")
        response = cursor.fetchone()
        self.nbAffect = response[0]
        
        fermerBase()
        print 'tableAffect' + str(self.tableAffect)
              
        
        
        
        
        
#________________Bouton__________________

    def connectActions(self):
        self.BP_newPlanche.clicked.connect(self.newPlanche)
        self.BP_supPlanche.clicked.connect(self.supPlanche)
        self.BP_savePlanche.clicked.connect(self.savePlanche)
        self.comboPlanche.currentIndexChanged.connect(self.maj_planche)

        self.BP_itk.clicked.connect(self.afficheItk)
        self.comboItk.currentIndexChanged.connect(self.maj_itk)

        self.BP_planche.clicked.connect(self.affichePlanche)
        self.BP_listSemis.clicked.connect(self.listSemis)
        self.BP_listAction.clicked.connect(self.listAction)
        self.BP_listPlantation.clicked.connect(self.listPlantation)
        self.BP_listRecolte.clicked.connect(self.listRecolte)
        
        self.BP_recharge.clicked.connect(self.recharger)

        self.BP_plante.clicked.connect(self.affichePlante)
        self.BP_action.clicked.connect(self.afficheAction)
        
 
    def newPlanche(self):
        print 'newPlanche'
        
        lastId = self.affect_active.addAffect()
        self.affect_active = AffectPlanches()
        self.parcoursList()

        self.rechargeAffect()

        
    def supPlanche(self):
        print 'supPlanche'
        self.affect_active.supAffect()
        self.parcoursList()
        
        self.rechargeAffect()
        
        
        
    def savePlanche(self):
        print 'savePlanche'
        self.affect_active.saveAffect()
        self.rechargeAffect()
        
        
    def recharger(self):
        self.parcoursList()        
        self.rechargeAffect()
        
       
        
        
 #_________________Bouton navigation_______________


    def afficheItk(self):
        print 'itk'
        self.appItk = QtGui.QWidget()
        self.uiItk = formItk()
        self.uiItk.main()
        self.uiItk.show()
        
       
    def affichePlanche(self):
        print 'planche'
        self.appPlanche = QtGui.QWidget()
        self.uiPlanche = formPlanche()
        self.uiPlanche.main()
        self.uiPlanche.show()

        
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
         
        
        
    def listSemis(self):
        print 'listSemis'
        self.appListingSemis = QtGui.QWidget()
        self.uiListingSemis = formListingSemis()
        self.uiListingSemis.main()
        self.uiListingSemis.show()

        
    def listAction(self):
        print 'listAction'
        self.appListingAction = QtGui.QWidget()
        self.uiListingAction = formListingAction()
        self.uiListingAction.main()
        self.uiListingAction.show()


    def listPlantation(self):
        print 'listSemis'
        self.appListingPlantation = QtGui.QWidget()
        self.uiListingPlantation = formListingPlantation()
        self.uiListingPlantation.main()
        self.uiListingPlantation.show()        
        
    def listRecolte(self):
        print 'listRecolte'
        self.appListingRecolte = QtGui.QWidget()
        self.uiListingRecolte = formListingRecolte()
        self.uiListingRecolte.main()
        self.uiListingRecolte.show()
        
        
#____________ITK_____________________

    def lireItk(self):
        print 'lireItk'
        ouvrirBase()
        cursor.execute("""SELECT id_itk, nom FROM itk ORDER BY nom""")
        self.tableItk = cursor.fetchall()
        fermerBase()
        self.comboItk.clear()
        for id in self.tableItk:
            self.comboItk.addItem(id[1])
           
       
    def lectureChampsItk(self):
        print 'lecture champs plante'
        self.lineItk = self.comboItk.currentIndex()

        #lit données plantation et initialise l'objet
        
        numId = int(self.trouveIdItk(self.comboItk.currentIndex()))      
        self.affect_active.itk = Itk(numId)
        
        print str(self.affect_active.itk.nom)        

                
    def lireAffect(self,id_affect):
        print 'lirePlantation'
        
        self.affect_active.lireAffect(id_affect)
        self.comboItk.clear()
        line = 1
        for id in self.affect_active.tableAffect:
            self.comboPlanche.addItem(str(line))
            line = line + 1

        
        
    def maj_itk(self):
        print 'maj_itk'
        numItk = self.comboItk.currentIndex()
        
        self.id_itk = self.trouveIdItk(numItk)
        
        self.affect_active.itk.lireItk(self.id_itk)
        self.affichage()

                  
            
            
            
#____________Planche_____________________

    def lirePlanche(self):
        print 'lirePlanche'
        ouvrirBase()
        cursor.execute("""SELECT id_planche, nom FROM planche ORDER BY nom""")
        self.tablePlanche = cursor.fetchall()
        fermerBase()
        self.comboPlanche.clear()
        for id in self.tablePlanche:
            self.comboPlanche.addItem(id[1])
           

    def lectureChampsPlanche(self):
        print 'lecture champs planche'
        self.linePlanche = self.comboPlanche.currentIndex()
        #lit données plantation et initialise l'objet
        
        numId = int(self.trouveIdPlanche(self.comboPlanche.currentIndex()))      
        self.affect_active.planche = Planche()
        self.affect_active.planche.lirePlanche(numId)
        
        print str(self.affect_active.planche.nom)


    def maj_planche(self):
        print 'maj_planche'
        numPlanche = self.comboPlanche.currentIndex()
        
        
        id_planche = self.tablePlanche[numPlanche][0]
        
        id_affect = self.trouveIdAffect_IdPlanche(id_planche)
        self.affect_active.id_affect = id_affect
        self.affect_active.lireAffect(id_planche) 
        print 'planche=' + str(self.affect_active.planche.nom)

        id_itk = self.affect_active.itk.id_itk 
        lineItk = self.trouveLineItk(id_itk)
        self.comboItk.setCurrentIndex(int(lineItk))
        self.affichage()



#____________________Affichage____________________


    def affichage(self):
        print 'affichagePlante'
        
        largeur = 975
        firstFrame = 20
        epPlante = 20
        
        semaineAvant = 5
        semaineApres = 5
        nb_semaine = 52 + semaineAvant + semaineApres

        
        semaine = largeur / (52 + 2)

        flag = 0
        pos = 25
        

        self.listPlanning = []
        
        while flag < self.nbAffect:
            print 'flag=' + str(flag)
            print 'table affect' + str(self.tableAffect)
            id_planche = self.tableAffect[flag][1]
            
            
            pl_active = AffectPlanches()
            pl_active.lireAffect(id_planche)
            
            planningPlx = PlanningPlanche(self.scrollAreaWidgetContents)     ##self.scrollAreaWidgetContents
            planningPlx.planche_active = pl_active
            planningPlx.maj_planche()
            
            planningPlx.nb_semaine = nb_semaine
            planningPlx.semaineAvant = semaineAvant
            planningPlx.marge = self.marge
            planningPlx.largeur = largeur
            planningPlx.posyFrame = pos
            
            
            pos = planningPlx.hauteur + 30 + pos
             
            self.listPlanning.append(planningPlx)
            planningPlx.destroy()
          
            
            flag = flag +1
        
        line = 0  

        for id in self.listPlanning:
            print 'aff=' + str(self.listPlanning[line].planche_active.planche.nom)

            self.listPlanning[line].show()
            line = line + 1
        
        hauteur = self.listPlanning[line-1].hauteur
        self.scrollAreaWidgetContents.setMinimumHeight(pos + hauteur + 20)
            
        self.update()     
            

        
    def main(self):
        self.show()
         
        
        
       
if __name__ == '__main__':
    
    app = QtGui.QApplication(sys.argv)
    toto = formAssolement()
    toto.main()
    app.exec_()
        
        
        
        
        