# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

students = {};

class StudentNotFound(Exception):
    def __str__(self):
        return "StudentNotFound"
    
class StudentFound(Exception):
    def __str__(self):
        return "StudentFound"
    
def addStudents():
    try:
        admissionNumber = input ("Insert Admission Number: ")
        name = input("Insert Name: ")
        
        if admissionNumber not in students:
            students[admissionNumber] = name
        else:
            raise StudentFound( )
            
            
    except StudentFound as e:
        print (e)
        
def searchStudents(): 
    try:
        admissionNumber = input ("Insert Admission Number: ")
        
        if admissionNumber not in students:
            raise StudentNotFound
            
        else:
            print(students[admissionNumber])
        
        
    except StudentNotFound as e:
         print(e)
            
    