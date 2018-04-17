#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 19:46:15 2018

@author: cedric
"""
from PyQt4 import QtGui, QtCore
import sys

from PyQt4.QtGui import QPainter, QPen
from PyQt4.QtCore import Qt
from itk import *
from plante import *
from action import *
from planche import *
from fonctionFC import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

       
        
class PlanningPlanche(QtGui.QWidget):
    def __init__(self, parent=None):
        
        QtGui.QWidget.__init__(self, parent)
        self.setObjectName(_fromUtf8("PlanningPlanche"))
        self.planche_active = AffectPlanches()
        
        self.qp = QtGui.QPainter()
        self.marge = 10
        self.largeur = 1000
        self.posyFrame = 30
        self.nomItk = ''
        
        self.epPlante = 20
        self.nb_semaine = 60
        self.semaineAvant = 5
        self.h_plante = 500
        self.h_action = 500
        self.hauteur = self.h_action + self.h_plante + self.epPlante
        self.setGeometry(20, 20, self.largeur, 50000)
        self.zonePlanning = QtGui.QWidget(self)
        self.zonePlanning.setGeometry(self.marge, self.posyFrame, self.largeur, 5000)
        
        self.planningPlante = PlanningPlante(self.zonePlanning)
        self.planningAction = PlanningAction(self.zonePlanning)
        
        self.maj_planche()

        
    def paintEvent(self, event):
        self.maj_affichage(event)

       
    def maj_planche(self):
        
        self.planningPlante.itk_active = self.planche_active.listeItk[0]
        self.planningAction.itk_active = self.planche_active.listeItk[0]
        
        nbPlante = self.planche_active.listeItk[0].plantation.nbPlante
        self.h_plante = (nbPlante + 1 ) * self.epPlante
        nbAction = self.planche_active.listeItk[0].intervention.nbAction
        self.h_action = (nbAction + 1) * self.epPlante 
        self.hauteur = self.h_action + self.h_plante 
        
        self.nomPlanche = self.planche_active.planche.nom
        self.nomItk = self.planche_active.listeItk[0].nom

        self.planche_active.lireAffect(self.planche_active.id_affect)
        
        

        
        
    def maj_affichage(self,event):
 
                #taille du widget
        self.nomItk = self.planche_active.listeItk[0].nom
        self.hauteur = self.h_action + self.h_plante 

        self.setGeometry(20, 20, self.largeur, 50000)
        largeurFrame = self.largeur - self.marge - 10
        self.zonePlanning.setGeometry(self.marge,self.posyFrame,largeurFrame, self.hauteur)

        self.planningPlante.setGeometry(0,0, self.largeur, self.h_plante + 15)        
        self.planningPlante.hauteur= self.h_plante
        self.planningPlante.largeur = self.largeur
        self.planningPlante.epPlante = self.epPlante
        self.planningPlante.nb_semaine = self.nb_semaine
        self.planningPlante.semaineAvant = self.semaineAvant
        self.planningPlante.maj_affichage(event)

        self.planningAction.setGeometry(0,self.h_plante, self.largeur, self.h_action + self.epPlante)
        self.planningAction.hauteur= self.h_action + self.epPlante
        self.planningAction.largeur = self.largeur
        self.planningAction.epAction = self.epPlante
        self.planningAction.nb_semaine = self.nb_semaine
        self.planningAction.semaineAvant = self.semaineAvant
        self.planningAction.maj_affichage(event)
        

        
        self.qp.begin(self)
        self.qp.eraseRect(0,self.posyFrame - 20,self.largeur,1000)
        self.qp.setBrush(QtGui.QColor(150, 150, 150))
        self.qp.drawRect(self.marge, self.posyFrame, largeurFrame, self.hauteur)
        
        self.qp.setBrush(QtGui.QColor(255,0, 0))
        self.qp.setFont(QtGui.QFont('Decorative', 10))
        self.qp.drawText(self.marge + 5, self.posyFrame - 8 , self.nomPlanche )
        self.qp.end()
       

        
        
class PlanningPlante(QtGui.QWidget):
    def __init__(self, parent=None):    
        QtGui.QWidget.__init__(self, parent)
        self.setObjectName(_fromUtf8("affichagePlante"))
        self.itk_active = Itk()
        self.qp = QtGui.QPainter()
        self.largeur = 950
        self.hauteur = 300
        self.epPlante = 20
        self.semaineAvant =2
        
        self.nb_semaine = 60       
        

        self.setGeometry(0, 0, self.largeur, self.hauteur)
 

        
    def paintEvent(self, event):        
        self.maj_affichage(event)
        
        
    def maj_affichage(self, event):
        nbPlante = self.itk_active.plantation.nbPlante
        self.semaine = self.largeur / self.nb_semaine
       
        semaine = self.semaine 
        
       
        self.qp.begin(self)

        flag =0
        pen = QPen(Qt.black, 1, Qt.DotLine)
        self.qp.setPen(pen)
        
        while flag < self.nb_semaine + 1  :
            posX = flag * semaine
            posY =0
            
            self.qp.drawLine(posX, posY, posX, posY + (nbPlante +1) * self.epPlante)
            flag = flag + 1
        
        pen.setStyle(Qt.SolidLine)
        self.qp.setPen(pen)
 
        flag = 0
        self.qp.setFont(QtGui.QFont('Decorative', 10))
        
        while flag < self.nb_semaine + 1:
            posX = flag * semaine + 2
            posY =0
            
            
            if flag < 53 + self.semaineAvant :
                num_semaine = flag - self.semaineAvant
            if flag > 52 + self.semaineAvant :
                num_semaine = flag- 52 - self.semaineAvant                
            
            self.qp.drawText(posX, posY + 15, str(num_semaine)) 
            
            flag = flag + 5
             
        
        flag = 0
        
        while flag < nbPlante:
            nomPlante = self.itk_active.plantation.listePlante[flag].plante.nom

            pos_y = self.epPlante + flag *  self.epPlante
          
            debut_semis = semaine  * (self.itk_active.plantation.listePlante[flag].date_semis + self.semaineAvant)
            long_semis = semaine * self.itk_active.plantation.listePlante[flag].plante.duree_pepiniere
            
            debut_croissance = debut_semis + long_semis
            long_croissance = (semaine * self.itk_active.plantation.listePlante[flag].plante.duree_croissance) - long_semis
            
            debut_recolte = debut_croissance + long_croissance
            long_recolte = semaine * self.itk_active.plantation.listePlante[flag].plante.duree_recolte
                  
          
            self.qp.setBrush(QtGui.QColor(255, 80, 0, 160))
            self.qp.drawRect(debut_semis, pos_y, long_semis, self.epPlante)
    
            self.qp.setBrush(QtGui.QColor(0, 255, 0))
            self.qp.drawRect(debut_croissance, pos_y, long_croissance, self.epPlante)
    
            self.qp.setBrush(QtGui.QColor(255, 0, 0))
            self.qp.drawRect(debut_recolte, pos_y, long_recolte, self.epPlante)
            
            self.qp.setFont(QtGui.QFont('Decorative', 10))
            self.qp.drawText(debut_croissance + 5, pos_y + 15, nomPlante)        
       

    
            flag = flag + 1
        self.qp.end()
        


                
class PlanningAction(QtGui.QWidget):
    def __init__(self, parent=None):    
        QtGui.QWidget.__init__(self, parent)
        self.setObjectName(_fromUtf8("affichageAction"))
        self.itk_active = Itk()
        self.qp = QtGui.QPainter()
        self.largeur = 950
        self.hauteur = 300
        self.epAction = 20
        self.semaineAvant =2
        
        self.nb_semaine = 60       
       
        
        self.setGeometry(0, 0, self.largeur, self.hauteur)
 

        
    def paintEvent(self, event):
        self.maj_affichage(event)
        
        
    def maj_affichage(self,event):
        nbAction = self.itk_active.intervention.nbAction
        self.semaine = self.largeur / self.nb_semaine
        
        semaine = self.semaine 
        
        self.qp.begin(self)

        flag =0
        pen = QPen(Qt.black, 1, Qt.DotLine)
        self.qp.setPen(pen)
        
        while flag < self.nb_semaine + 1 :
            posX = flag * semaine
            posY =0
            
            self.qp.drawLine(posX, posY, posX, posY + (nbAction +1) * self.epAction)
            flag = flag + 1

            
        pen.setStyle(Qt.SolidLine)
        self.qp.setPen(pen)
        
        flag = 0
        
        while flag < nbAction:
            nomAction = self.itk_active.intervention.listeAction[flag].action.nom

            pos_y = self.epAction / 2 + flag *  self.epAction
          
            debut_action = semaine  * (self.itk_active.intervention.listeAction[flag].date + self.semaineAvant)
            long_action = semaine * self.itk_active.intervention.listeAction[flag].duree 
                  
          
            self.qp.setBrush(QtGui.QColor(255, 80, 0, 160))
            self.qp.drawRect(debut_action, pos_y, long_action, self.epAction)
                
            self.qp.setFont(QtGui.QFont('Decorative', 10))
            self.qp.drawText(debut_action + 5, pos_y + 15, nomAction)        
       

    
            flag = flag + 1
        self.qp.end()
        


def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = PlanningPlanche()
    ex.show()
    sys.exit(app.exec_())
       


if __name__ == '__main__':
    main()        