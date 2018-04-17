#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 09:51:58 2018

@author: cedric
"""
from PyQt4 import QtGui, QtCore
import sys
from fonctionFC import *

import planteUI

import sqlite3



class Plante():
    def __init__(self,numId):
        self.numId = numId
        self.nom = 'New Plante'
        self.designation = ''
        self.duree_pepiniere = 1
        self.duree_croissance = 2
        self.duree_recolte = 3
        self.rendement = 4.5
        self.graineparg = 10.2
        self.dist_x = 1.1
        self.dist_y = 1.1        
        self.annuelle = True
        self.gelive = True
        self.tallage = False
        self.vernalisation = False
        self.info = ''
        self.semis = '0,1,2'
        self.retour = 1
        self.NoC = 10
        self.floraison = 1
        

        self.dataPlante ={}
        
        if numId > 0:
            self.lirePlante(numId)
            
            

    def data(self):
        #ecrire les données de l'objet dans un dictionnaire pour la bdd
        print 'data'
        self.dataPlante['id_plante']= self.numId
        self.dataPlante['nom']= str(self.nom)
        self.dataPlante['designation']= str(self.designation)
        self.dataPlante['duree_pepiniere']= self.duree_pepiniere 
        self.dataPlante['duree_croissance']= self.duree_croissance
        self.dataPlante['duree_recolte']= self.duree_recolte
        self.dataPlante['rendement']= self.rendement
        self.dataPlante['graineparg']= self.graineparg        
        self.dataPlante['dist_x']= self.dist_x
        self.dataPlante['dist_y']= self.dist_y
        self.dataPlante['annuelle']= BoolToInt(self.annuelle)
        self.dataPlante['gelive']= BoolToInt(self.gelive)
        self.dataPlante['tallage']= BoolToInt(self.tallage)
        self.dataPlante['vernalisation']= BoolToInt(self.vernalisation)
        self.dataPlante['info']= str(self.info)
        self.dataPlante['semis']= str(self.semis)
        self.dataPlante['retour']= self.retour
        self.dataPlante['NoC']= self.NoC
        self.dataPlante['floraison']= self.floraison
        
        

    def lirePlante(self,numId):
        print 'lireData'
        self.numId = numId
        ouvrirBase()
        print 'numId=' + str(numId)
        cursor.execute("""
        SELECT 
            nom, designation, duree_pepiniere, duree_croissance,
            duree_recolte, rendement, graineparg, dist_x, dist_y,
            annuelle, gelive, tallage, vernalisation, info, semis,
            retour, NoC, floraison
        FROM plante WHERE id_plante=?
        """, (numId,))
        response = cursor.fetchone()
        fermerBase()
        
        self.nom = response[0]
        self.designation = response[1]
        self.duree_pepiniere = response[2]
        self.duree_croissance = response[3]
        self.duree_recolte = response[4]
        self.rendement = response[5]
        self.graineparg = response[6]
        self.dist_x = response[7]
        self.dist_y = response[8]
        self.annuelle = IntToBool(response[9])
        self.gelive = IntToBool(response[10])
        self.tallage = IntToBool(response[11])
        self.vernalisation = IntToBool(response[12])
        self.info = response[13]
        self.semis = response[14]
        self.retour = response[15]
        self.NoC = response[16]
        self.floraison = response[17]
        

        
    def ecrirePlante(self):
        print 'ecrireData'        
        self.data()
                
        ouvrirBase()
        cursor.execute("""
        UPDATE 
            plante 
        SET 
        nom = :nom, designation = :designation, duree_pepiniere = :duree_pepiniere ,
        duree_croissance = :duree_croissance, duree_recolte = :duree_recolte,
        rendement = :rendement, graineparg = :graineparg,
        dist_x = :dist_x, dist_y = :dist_y,
        annuelle = :annuelle, gelive = :gelive, tallage = :tallage,
        vernalisation = :vernalisation, info = :info, semis = :semis,
        retour = :retour, NoC = :NoC, floraison =:floraison
        WHERE id_plante = :id_plante
        """, self.dataPlante)
        conn.commit()
        
        fermerBase() 
        
    def supPlante(self):
        print 'supPlante'
        numId =int(self.numId)
        ouvrirBase()
        cursor.execute("""DELETE FROM plante WHERE (((plante.id_plante)=?))""", (numId,))
        conn.commit()
        fermerBase()


    def newPlante(self):
        print 'newPlante'
        self.nom = 'New Plante'
        self.designation = ''
        self.duree_pepiniere = 0
        self.duree_croissance = 1
        self.duree_recolte = 1
        self.rendement = 1
        self.graineparg = 1
        self.dist_x = 1
        self.dist_y = 1        
        self.annuelle = True 
        self.gelive = True
        self.tallage = False
        self.vernalisation = False
        self.info = ''
        self.semis = '0,1,2'
        self.retour = 1
        self.NoC = 10
        self.floraison = 1

        
        self.data()
       
        ouvrirBase()
        cursor.execute("""
        INSERT INTO plante (nom, designation, duree_pepiniere,
        duree_croissance, duree_recolte, rendement, graineparg,
        dist_x, dist_y, annuelle, gelive, tallage, vernalisation,
        info, semis, retour, NoC, floraison)
        VALUES 
        (:nom, :designation, :duree_pepiniere,
        :duree_croissance, :duree_recolte, :rendement, :graineparg,
        :dist_x, :dist_y, :annuelle, :gelive, :tallage, :vernalisation,
        :info, :semis, :retour, :NoC, :floraison)
        """, self.dataPlante)
        conn.commit()
        fermerBase()

        return(cursor.lastrowid)
        
        
        
        
class formPlante(QtGui.QWidget, planteUI.Ui_Form):
    def __init__(self, parent = None):
        super(formPlante, self).__init__(parent)
        self.setupUi(self)
        self.connectActions()
        self.positionList = 0
        self.plante_active = Plante(self.positionList)
        self.idPlante = ''
        self.nbPlante = 0
        self.dataPlante ={}
        self.tablePlante = []
        
        self.parcoursList()
        self.lirePlante()

        #self.ecritureChamps()
        
        
    def parcoursList(self):
        print 'parcoursList'
        ouvrirBase()
        
        cursor.execute("""SELECT id_plante, nom FROM plante ORDER BY nom""")
        self.tablePlante = cursor.fetchall()
               
        cursor.execute("""SELECT COUNT(id_plante) FROM plante""")
        self.nbPlante = cursor.fetchone()[0]
            
        fermerBase()
        
        
        
    def connectActions(self):
        self.bp_lastPlante.clicked.connect(self.prevPlante)
        self.bp_nextPlante.clicked.connect(self.nextPlante)
        self.bp_newPlante.clicked.connect(self.newPlante)
        self.bp_supPlante.clicked.connect(self.supPlante)
        self.bp_SavePlante.clicked.connect(self.savePlante)
        
              
    def savePlante(self):
        print 'savePlante'
        self.lectureChamps()

        self.plante_active.ecrirePlante()
        
        
    def prevPlante(self):
        print'prevPlante'
        self.parcoursList()
       
        if self.positionList == 0 :
            print "on est au début"
            return
        
        self.positionList = self.positionList - 1                
        self.lirePlante()
     
        
        
    def nextPlante(self):
        print 'nextPlante'
        self.parcoursList()
        
        if self.positionList > self.nbPlante-2:
            print "c'est la derniere plante"
            self.positionList = self.nbPlante - 1
            return
        
        self.positionList = self.positionList + 1
        self.lirePlante()

    
    def lirePlante(self):
        numId = self.tablePlante[self.positionList][0]
    
        self.plante_active.lirePlante(numId)
        self.ecritureChamps()
        

        
    def newPlante(self):
        print 'New plante'
        newPlante = self.plante_active.newPlante()
        self.plante_active = Plante(newPlante)
        self.plante_active.numId = newPlante
        self.positionList = newPlante
        
        self.parcoursList()
        self.ecritureChamps()
        

        
    def supPlante(self):       
        self.plante_active.supPlante()
               
        self.parcoursList()
        self.prevPlante()
        

     
    
    def ecritureChamps(self):
        print 'ecriture champs'
        self.line_nomPlante.setText(self.plante_active.nom)
        self.line_nom2.setText(self.plante_active.designation)
        self.line_ageRecolte.setText(str(self.plante_active.duree_croissance))
        self.line_duree_recolte.setText(str(self.plante_active.duree_recolte))
        self.line_ageFleur.setText(str(self.plante_active.floraison))
        self.line_duree_pepiniere.setText(str(self.plante_active.duree_pepiniere))
        self.check_annuelle.setChecked(self.plante_active.annuelle)
        self.check_gelive.setChecked(self.plante_active.gelive)
        self.check_tallage.setChecked(self.plante_active.tallage)
        self.check_vernalisation.setChecked(self.plante_active.vernalisation)
        self.lineSemis.setText(str(self.plante_active.semis))
        self.textInfo.setPlainText(str(self.plante_active.info))
        self.line_dist_x.setText(str(self.plante_active.dist_x))
        self.line_dist_y.setText(str(self.plante_active.dist_y))
        self.line_rendement.setText(str(self.plante_active.rendement))
        self.line_graineparg.setText(str(self.plante_active.graineparg))
        self.lineRetour.setText(str(self.plante_active.retour))
        self.lineNoC.setText(str(self.plante_active.NoC))
        print 'tit'
        
    


    def lectureChamps(self):
        print 'lecture champs'
        self.plante_active.nom = str(self.line_nomPlante.text())
        self.plante_active.designation = str(self.line_nom2.text())
        self.plante_active.duree_croissance = str(self.line_ageRecolte.text())
        self.plante_active.duree_recolte = str(self.line_duree_recolte.text())
        self.plante_active.floraison = str(self.line_ageFleur.text())
        self.plante_active.duree_pepiniere = str(self.line_duree_pepiniere.text())
        self.plante_active.annuelle = bool(self.check_annuelle.checkState())
        self.plante_active.gelive = bool(self.check_gelive.checkState())
        self.plante_active.tallage = bool(self.check_tallage.checkState())
        self.plante_active.vernalisation = bool(self.check_vernalisation.checkState())
        self.plante_active.semis = str(self.lineSemis.text())
        self.plante_active.info = str(self.textInfo.toPlainText())
        self.plante_active.dist_x = float(self.line_dist_x.text())
        self.plante_active.dist_y = float(self.line_dist_y.text())
        self.plante_active.rendement = float(self.line_rendement.text())
        self.plante_active.graineparg = float(self.line_graineparg.text())
        self.plante_active.retour = float(self.lineRetour.text())
        self.plante_active.NoC = float(self.lineNoC.text())
        print 'tit'
              
        
        
    def main(self):
        
        self.show()

       
if __name__ == '__main__':
    
    app = QtGui.QApplication(sys.argv)
    toto = formPlante()
    toto.main()
    app.exec_()
