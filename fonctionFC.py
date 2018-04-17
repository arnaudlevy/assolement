#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 10:56:15 2018

@author: cedric
"""

#Fonction diverse


import sys
import sqlite3

#déclaration de variable globale
nomBDD = 'bdd.db'
conn = sqlite3.connect(nomBDD)
cursor = conn.cursor()
conn.close


def ouvrirBase():
        print 'ouvrirBase'
        conn = sqlite3.connect(nomBDD)
        cursor = conn.cursor()
    
def fermerBase():
        print 'fermerBase'
        conn.close

        
def BoolToInt(a):
    print 'BoolToInt'
    BtI = 0
    
    if a == True:
        BtI = 1
    else:
        BtI = 0
    
    return BtI
        
def IntToBool(a):
    print 'IntToBool'
    ItB = False
    
    if a == 1:
        ItB = True
    else:
        ItB = False
    
    return ItB 

if __name__ == "__main__":
    print "Execution de fonction.py"
    