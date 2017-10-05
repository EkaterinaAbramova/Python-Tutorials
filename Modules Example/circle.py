#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Dr Ekaterina Abramova

Modules
"""
pi = 3.14159 # initialise a variable

# create some functions
def area(radius):
    return pi*(radius**2)

def circumference(radius): 
    return 2*pi*radius

def sphereSurface(radius): 
    return 4.0*area(radius)

def sphereVolume(radius):
    return (4.0/3.0)*pi*(radius**3)