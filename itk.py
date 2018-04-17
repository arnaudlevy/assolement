#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 09:51:58 2018

@author: cedric
"""

from plante import *
from action import *
from fonctionFC import *

import sqlite3

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class Itk():
    def __init__(self):
        self.id_itk = 1
        self.nom = 'New Itk'
        self.dataItk = {}
        self.plantation = Plantation(self.id_itk)
        self.intervention = Intervention(self.id_itk)
        
        self.lireItk(self.id_itk)
     
    def lireItk(self,id_itk):
        print 'lireItk'        
        ouvrirBase()
        id_itk = int(id_itk)
        cursor.execute("""SELECT nom FROM itk WHERE id_itk=?""", (id_itk,))
        response = cursor.fetchone()
        
        self.id_itk = id_itk        
        self.nom = response[0]
        fermerBase()
        self.plantation = Plantation(id_itk)
        self.intervention = Intervention(id_itk)
        
    def ecrireItk(self):
        print 'ecrire itk'
        self.data()
        ouvrirBase()
        cursor.execute("""UPDATE itk SET nom = :nom  WHERE id_itk = :id_itk""", self.dataItk)
        conn.commit()
        
        fermerBase() 
        
    def supItk(self):
        print 'supItk'
        ouvrirBase()
        id_itk = int(self.id_itk)
        cursor.execute("""DELETE FROM itk WHERE (((itk.id_itk)=?))""", (id_itk,))
        conn.commit()
        
        fermerBase()

    def newItk(self):
        print 'newItk'
        self.nom = 'newItk'
        self.data()
        
        ouvrirBase()
        cursor.execute("""INSERT INTO itk (nom) VALUES (:nom)""", self.dataItk)
        conn.commit()
        fermerBase()
        
        return(cursor.lastrowid)
       
        
    def data(self):
        #ecrire les données de l'objet dans un dictionnaire pour la bdd
        print 'data'
        self.dataItk['id_itk']= self.id_itk
        self.dataItk['nom']= str(self.nom)
        
        
    def lirePlante(self):
        self.plantation.lirePlantes(self.id_itk)
        


        

class Plantation():
    def __init__(self,itk):
        print 'init plantation'
        self.itk = itk 
        self.dataPlantation = {}
                
        self.listePlante = []
        self.tablePlantation = []
        self.nbPlante = 0
        
        self.lirePlantes(itk)

        
    def lirePlantes(self,itk):
        print 'lirePlantes'
        numId = int(itk)
        ouvrirBase()
        cursor.execute("""SELECT id_plantation, fk_id_itk, fk_id_plante, date_semis FROM plantation WHERE fk_id_itk = ?""",(numId,) )
        self.tablePlantation = cursor.fetchall()
        fermerBase()
        
        if self.tablePlantation == []:
            print 'pas de plantation'
            return
            
        line = 0
        print 'table plantes=' + str(self.tablePlantation)
        for id in self.tablePlantation:
            pl = Plante(id[2])
            newPlante = PlantePlantee(id[1], pl, id[3])
            
            self.listePlante.append(newPlante)
            line = line + 1
        
            self.nbPlante = line
    
        
    def addPlante(self,itk):
        print 'addPlante'
        self.dataPlantation = {}
        self.dataPlantation['fk_id_itk'] = int(itk)
        self.dataPlantation['fk_id_plante'] = int(1)
        self.dataPlantation['date_semis'] = int(1)
        
        print 'dataplantation=' + str(self.dataPlantation)
       
        ouvrirBase()
        cursor.execute("""INSERT INTO plantation (fk_id_itk, fk_id_plante, date_semis) VALUES(:fk_id_itk, :fk_id_plante, :date_semis)""", self.dataPlantation)
        conn.commit()
        fermerBase()

    def supPlante(self,id_plante):
        print 'supPlante'
        self.dataPlantation = {}
        self.dataPlantation['fk_id_itk'] = int(self.itk)
        self.dataPlantation['fk_id_plante'] = int(id_plante)
        ouvrirBase()
        cursor.execute("""DELETE FROM plantation WHERE (fk_id_itk = :fk_id_itk AND fk_id_plante = :fk_id_plante)""", self.dataPlantation)
        fermerBase()


        
class PlantePlantee():
    def __init__(self,id_itk, plante, date):
        self.plante = plante
        self.id_itk = int(id_itk)
        self.date_semis = int(date)
        self.dataPlantation = {}
        
    def save(self,id_plantation):
        self.data()
        self.dataPlantation['id_plantation'] = int(id_plantation)
        ouvrirBase()
        cursor.execute("""UPDATE plantation SET fk_id_plante = :fk_id_plante, date_semis = :date_semis WHERE id_plantation = :id_plantation""", self.dataPlantation)
        
        conn.commit()        
        fermerBase()
        
        
    def data(self):
        self.dataPlantation['fk_id_itk'] = self.id_itk
        self.dataPlantation['fk_id_plante'] = self.plante.numId
        self.dataPlantation['date_semis'] = self.date_semis



class Intervention():
    def __init__(self,itk):
        self.itk = itk 
        self.dataIntervention = {}
                
        self.listeAction = []
        self.tableAction = []
        self.nbAction = 0
        
        self.lireActions(itk)

        
    def lireActions(self,itk):
        print 'lireActions'
        id_itk = int(itk)
        ouvrirBase()
        cursor.execute("""SELECT id_intervention, fk_id_itk, fk_id_action, date, duree FROM intervention WHERE fk_id_itk = ?""",(id_itk,) )
        self.tableAction = cursor.fetchall()
        fermerBase()
        
        if self.tableAction == []:
            print 'No action'
            return
            
        line = 0

        for id in self.tableAction:
            act = Action(id[2])
            newAction = ActionProgrammee(id[1], act, id[3], id[4])
            
            self.listeAction.append(newAction)
            line = line + 1
        
            self.nbAction = line
    
        
    def addAction(self,itk):
        print 'class addaction'
        self.dataIntervention = {}
        self.dataIntervention['fk_id_itk'] = int(itk)
        self.dataIntervention['fk_id_action'] = int(1)
        self.dataIntervention['date_interv'] = int(1)
        self.dataIntervention['duree'] = int(1)
        
        print str(self.dataIntervention)
        ouvrirBase()
        cursor.execute("""INSERT INTO intervention (fk_id_itk, fk_id_action, date, duree) VALUES(:fk_id_itk, :fk_id_action, :date_interv, :duree)""", self.dataIntervention)
        conn.commit()
        fermerBase() 

    def supAction(self,id_action):
        print 'supAction'
        self.dataIntervention = {}
        self.dataIntervention['fk_id_itk'] = int(self.itk)
        self.dataIntervention['fk_id_action'] = int(id_action)
        ouvrirBase()
        cursor.execute("""DELETE FROM intervention WHERE (fk_id_itk = :fk_id_itk AND fk_id_action = :fk_id_action)""", self.dataIntervention)
        fermerBase()
        
        
class ActionProgrammee():
    def __init__(self,id_itk, action, date, duree):
        self.action = action
        self.id_itk = int(id_itk)
        self.date = int(date)
        self.duree = int(duree)
        self.dataIntervention ={}
        
    def save(self,id_intervention):
        print 'save'
        self.data()
        self.dataIntervention['id_intervention'] = int(id_intervention)
        print str(self.dataIntervention)
        ouvrirBase()
        cursor.execute("""UPDATE intervention SET fk_id_action = :fk_id_action, date = :date, duree = :duree WHERE id_intervention = :id_intervention""", self.dataIntervention)
        
        conn.commit()        
        fermerBase()
                
    def data(self):
        print 'data'
        self.dataIntervention['fk_id_itk'] = self.id_itk
        self.dataIntervention['fk_id_action'] = int(self.action.id_action)
        self.dataIntervention['date'] = self.date
        self.dataIntervention['duree'] = self.duree

        