#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 10:36:25 2018

@author: cedric
"""

from PyQt4 import QtGui, QtCore
import sys

from itk import *
from fonctionFC import *

import plancheUI

import sqlite3



class AffectPlanches():
    def __init__(self):
        self.id_affect = 1
        self.planche = Planche()
        self.itk = Itk()
        self.dataAffect = {}
        
        self.listeItk = []
       
        self.lireAffect(self.id_affect)

        
        
    def data(self):
        #ecrire les données de l'objet dans un dictionnaire pour la bdd
        print 'data'
        self.dataAffect['id_affect']= self.id_affect
        self.dataAffect['fk_id_planche']= int(self.planche.id_planche)
        self.dataAffect['fk_id_itk']= int(self.itk.id_itk)


        
        
    def lireAffect(self, id_planche):
        print 'lireAffect'
        id_planche = int(id_planche)
        print 'id_planche=' + str(id_planche)
        self.planche = Planche()
        self.planche.lirePlanche(id_planche)
        
        ouvrirBase()
        cursor.execute("""SELECT id_affect, fk_id_planche, fk_id_itk FROM affectPlanche WHERE fk_id_planche = ?""",(id_planche,) )
        self.tableAffect = cursor.fetchall()
        fermerBase()

        if self.tableAffect == []:
            print 'pas de planche'
            return
        
        line = 0
        self.listeItk = []
        
        for id in self.tableAffect:
            itk = Itk()
            itk.lireItk(id[2])
            
            self.listeItk.append(itk)
            line = line + 1
        
            self.nbItk = line        
        
        
    def addAffect(self):
        print 'addAffect'
        self.dataAffect = {}
        self.dataAffect['fk_id_planche'] = int(self.planche.id_planche)
        self.dataAffect['fk_id_itk'] = int(1)
        
        print 'dataAffect' + str(self.dataAffect)

        ouvrirBase()
        cursor.execute("""INSERT INTO affectPlanche (fk_id_planche, fk_id_itk) VALUES(:fk_id_planche, :fk_id_itk)""", self.dataAffect)
        conn.commit()
        fermerBase()
        
        return(cursor.lastrowid)

        
    def saveAffect(self):
        print 'saveAffect'
        
        self.data()
        ouvrirBase()
        cursor.execute("""UPDATE affectPlanche SET fk_id_itk = :fk_id_itk  WHERE id_affect = :id_affect""", self.dataAffect)
        conn.commit()
        
        fermerBase() 
          
        
        
       
    def supAffect(self):
        print 'supAffect'
        id_affect =int(self.id_affect)

        ouvrirBase()
        cursor.execute("""DELETE FROM affectPlanche WHERE (((affectPlanche.id_affect)=?))""", (id_affect,))
        conn.commit()
        fermerBase()
        
        



class Planche():
    def __init__(self):
        self.id_planche = 1
        self.nom = 'New planche'
        self.longueur = 0.1
        self.largeur = 0.1
        self.surface = self.longueur * self.largeur
        
        self.dataPlanche = {}

        
    def data(self):
        #ecrire les données de l'objet dans un dictionnaire pour la bdd
        print 'data'
        self.dataPlanche['id_planche'] = int(self.id_planche)
        self.dataPlanche['nom']= str(self.nom)
        self.dataPlanche['longueur'] = self.longueur
        self.dataPlanche['largeur'] = self.largeur
        
        
    def lirePlanche(self,id_planche):
        print 'lirePlanche'
        self.id_planche = id_planche
        
        ouvrirBase()
        print 'id_planche=' + str(self.id_planche)
        cursor.execute("""SELECT nom, longueur, largeur FROM planche WHERE id_planche=?""", (id_planche,))
        response = cursor.fetchone()
        fermerBase()
        
        self.nom = response[0]
        self.longueur = response[1]
        self.largeur = response[2]
        

    def ecrirePlanche(self):
        print 'ecrirePlanche'        
        self.data()
        
        print str(self.dataPlanche)
                
        ouvrirBase()
        cursor.execute("""UPDATE planche SET nom = :nom, longueur = :longueur, largeur = :largeur WHERE id_planche = :id_planche""", self.dataPlanche)
        conn.commit()
        
        fermerBase() 
        
 
    def supPlanche(self):
        print 'supPlanche'
        id_planche =int(self.id_planche)
        print 'id_planche'
        ouvrirBase()
        cursor.execute("""DELETE FROM planche WHERE (((planche.id_planche)=?))""", (id_planche,))
        conn.commit()
        fermerBase()

        
    def newPlanche(self):
        print 'newPlanche'
        self.nom = 'New Planche'
        self.longueur = 0.1
        self.largeur = 0.1
        
        self.data()
        print 'dataPlanche=' + str(self.dataPlanche)
        ouvrirBase()
        cursor.execute("""INSERT INTO planche (nom, longueur, largeur) VALUES(:nom, :longueur, :largeur)""", self.dataPlanche)
        conn.commit()
        fermerBase()

        return(cursor.lastrowid)
        
         
        
        
        

        
class formPlanche(QtGui.QMainWindow, plancheUI.Ui_MainWindow):
    def __init__(self, parent = None):
        super(formPlanche,self).__init__(parent)
        self.setupUi(self)
        self.connectActions()
        self.positionList = 0

        self.planche_active = Planche()
        self.planche_active.id_planche = int(self.positionList)

        self.dataPlanche ={}
        self.tablePlanche = []
           
        self.parcoursList()
        self.lirePlanche()
        

    def parcoursList(self):
        print 'parcoursList'
        ouvrirBase()
        
        cursor.execute("""SELECT id_planche, nom FROM planche ORDER BY nom""")
        self.tablePlanche = cursor.fetchall()
               
        cursor.execute("""SELECT COUNT(id_planche) FROM planche""")
        self.nbPlanche = cursor.fetchone()[0]
            
        fermerBase()
        print str(self.tablePlanche)
              
        
    def connectActions(self):
        self.bp_last.clicked.connect(self.prevPlanche)
        self.bp_next.clicked.connect(self.nextPlanche)
        self.bp_new.clicked.connect(self.newPlanche)
        self.bp_sup.clicked.connect(self.supPlanche)
        self.bp_save.clicked.connect(self.savePlanche) 
        
        
    def lirePlanche(self):
        print 'lirePlanche'
        id_planche = self.tablePlanche[self.positionList][0]
        print id_planche
    
        self.planche_active.lirePlanche(id_planche)
        self.ecritureChamps()
    
        
    def savePlanche(self):
        print 'savePlanche'
        self.lectureChamps()

        self.planche_active.ecrirePlanche()

        
    def prevPlanche(self):
        print'prevPlanche'
        self.parcoursList()
        print str(self.positionList)

       
        if self.positionList == 0 :
            print "on est au début"
            return
        
        self.positionList = self.positionList - 1                
        self.lirePlanche()
 
        
    def nextPlanche(self):
        print 'nextPlante'
        self.parcoursList()
        print str(self.positionList)
        
        if self.positionList > self.nbPlanche - 2:
            print "c'est la derniere plante"
            self.positionList = self.nbPlanche - 1
            return
        
        self.positionList = self.positionList + 1
        self.lirePlanche()
       

    def newPlanche(self):
        print 'New planche'
        idNewPlanche = self.planche_active.newPlanche() #renvoie l'id de la nouvelle ligne
        print 'idNewPlanche=' + str(idNewPlanche)
        self.planche_active = Planche()
        self.planche_active.lirePlanche(idNewPlanche)
        self.planche_active.id_planche = idNewPlanche
        self.positionList = idNewPlanche
        
        self.parcoursList()
        self.ecritureChamps()
        

    def supPlanche(self):       
        self.planche_active.supPlanche()
               
        self.parcoursList()
        self.prevPlanche()
        
    
    def ecritureChamps(self):
        print 'ecriture champs'
        self.line_nom.setText(self.planche_active.nom)
        self.line_longueur.setText(str(self.planche_active.longueur))
        self.line_largeur.setText(str(self.planche_active.largeur))
        

    def lectureChamps(self):
        print 'lecture champs'
        self.planche_active.nom = str(self.line_nom.text())
        self.planche_active.longueur = float(self.line_longueur.text())
        self.planche_active.largeur = float(self.line_largeur.text())
        
        
        
    def main(self):
        
        self.show()
        
        
        
        
        
if __name__ == '__main__':
    
    app = QtGui.QApplication(sys.argv)
    ApPlanche = formPlanche()
    ApPlanche.main()
    app.exec_()
    
            