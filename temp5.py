# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 21:24:50 2017

@author: user
"""

from car import *;

 

carList = [];

 

def initDb():

    infile = open("c:\\workspace\\car.txt", "r");

for line in infile:

    line = line.rstrip();

words = line.split(",");

print(line)

if words[0] == 'normal':

    carList.append(Car(int(words[1]), int(words[1]), int(words[1]), int(words[1])));

elif words[0] == 'sport':

    carList.append(SportsCar(int(words[1]), int(words[1]), int(words[1]), int(words[1])));

infile.close();

 



def addCar(carType, capa, wheels, seats, tank):

    if carType == 'normal':

        carList.append(Car(capa, wheels, seats, tank));

print("new normal car added")


    elif carType == 'sport':

        carList.append(SportsCar(capa, wheels, seats, tank));

print("new sport car added")

outfile = open("c:\\workspace\\car.txt", "a");

outfile.write(carType+","+str(capa)+","+str(wheels)+","+str(tank));

outfile.close();

 

def searchCar(carType):

    temp = [];

for c in carList:

    if c.type == carType:

temp.append(c);

for c in temp:

print(c);

return temp;

 

def delCar(car):

    for c in carList:

if c == car:

    carList.remove(c);

print("car deleted");

break;