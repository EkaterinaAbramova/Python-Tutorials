#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Dr Ekaterina Abramova, 2017

DICTIONARY
"""

# -----------------------------------------------------------------------------
# -------------------------- create a dictionary ------------------------------
myDict1 = {}
myDict2 = dict()

# example dictionary (key is 'Jan', value is 1)
months = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'June':6}

# add entry 
months['July'] = None
# change entry 
months['July'] = 7

# another way of creating a dictionary functionality is with lists 
L = [ ['Jan',1], ['Feb',2], ['Mar',3], ['Apr',4], ['May',5], ['June',6] ]
def keySearch(L,key):
    for elem in L:
        if elem[0] == key:
            return elem[1]
    return None
# function call
ans = keySearch(L,'Apr') # 4