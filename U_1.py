# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 16:27:08 2022

@author: yvand
"""
def summe(a,b):
    
    summ = zahl1 + zahl2
    
    return summ
    
def differenz(a,b):
    
    diff = zahl1 - zahl2
    
    return diff

def produkt(a,b):
    
    pro = zahl1*zahl2
    
    return pro

def division(a,b):
    
    try:
        divi = zahl1/zahl2
        return divi
    except:
        print("Division durch Null")
        return 
    
test = False

while test != True:

    try:
        zahl1, zahl2 = float(input("Erste Zahl = ")), float(input("Zweite Zahl = "))
        test = True
    
    except: 
        print("Ungültige Zahl")

operation_liste = ["add", "sub", "mult", "div"]


test = False
while test != True:
    
    operation = input("Wählen Sie ihre Opeation: ""add"" ""sub"" ""mult"" ""div"" :  ")
    
    if operation == "add" :
        print(summe(zahl1,zahl2));
        test = True
    elif operation == "sub" :
        print(differenz(zahl1,zahl2)); 
        test = True
    elif operation == "mult" :
        print(produkt(zahl1,zahl2));
        test = True
    elif operation == "div" :
        print(division(zahl1,zahl2));
        test = True
    else: 
        print("falsche Eingabe");
        
