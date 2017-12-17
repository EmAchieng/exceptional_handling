# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 15:54:45 2017

@author: user
"""

f = open ('fibo.txt', 'w')

try:
    f.write(error)
except NameError as e:
    print ("An Error Occurred")
finally:
    f.close()