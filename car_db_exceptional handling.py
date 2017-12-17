# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 21:42:06 2017

@author: user
"""

cars = {};

class carNotFound(Exception):
     def __str__(self):
        return "car Not Found"
    
class carFound(Exception):
    def __str__(self):
        return "car Found"

def addcars():
    try:
        carNumber = input ("Insert car Number: ")
        name = input("Insert Name of car: ")
        
        if carNumber not in cars:
            cars[carNumber] = name
        else:
            raise carFound( )
            
            
    except carFound as e:
        print (e)

def searchcars(): 
    try:
        carNumber = input ("Insert car Number: ")
        
        if carNumber not in cars:
            raise carNotFound
            
        else:
            print(cars[carNumber])
            
            
    except carNotFound as e:
         print(e)            