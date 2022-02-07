# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 16:27:08 2022

@author: yvand
"""

test = False

while test != True:

    try:
        zahl1, zahl2 = float(input("Erste Zahl = ")), float(input("Zweite Zahl = "))
        test = True
    
    except: 
        print("Ungültige Zahl")


Summe = zahl1 + zahl2;
print();
print(zahl1," + ",zahl2," = ",Summe);