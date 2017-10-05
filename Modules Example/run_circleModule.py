#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 18:07:36 2017

@author: bondgirl007
"""
# -------------------------------------- first way to use module 
import circle
pi = 3
print(pi) # 3
print(circle.pi) # 3.14159
print(circle.area(pi)) # 28.27431
print(circle.circumference(pi)) # 18.849539999999998
print(circle.sphereSurface(pi)) # 113.09724

# -------------------------------------- rename imported module 
import circle as cr
pi = 3
print(pi) # 3
print(cr.pi) # 3.14159

# -------------------------------------- second way to use module
from circle import *
print(pi) # 3.14159
print(circle.pi) # NameError: name 'circle' is not defined

nameHandle = open('kids', 'w')