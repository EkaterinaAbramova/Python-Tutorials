#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Dr Ekaterina Abramova, 2017
STRUCTURED TYPES.

Sequence type: strings
"""
# -----------------------------------------------------------------------------
# ------------------------------ empty string ---------------------------------
str1 = '' # empty string ''
str2 = "" # empty string ''
a = '4.0'
type(a) # str


# -----------------------------------------------------------------------------
# --------------------------- simple operations -------------------------------
'abc'[1:3] # 'bc'  
'abc'[0:len('abc')] # 'abc'  

'abc'[:3] # 'abc'
'abc'[0:] # 'abc'


# iterate over a string   
total = 0
for ii in '12345':  
    total = total + int(ii)
# 15 
    
# -----------------------------------------------------------------------------
# ------------------------- s.split built-in function -------------------------
s = 'Ekaterina Abramova plays basketball'
# Strings are immutable, s is unchanged.
s.split(' ') # ['Ekaterina', 'Abramova', 'plays', 'basketball']
print(s) # 'Ekaterina Abramova plays basketball'
# Assign result to a different variable
d = s.split(' ') # ['Ekaterina', 'Abramova', 'plays', 'basketball']
print(d) # ['Ekaterina', 'Abramova', 'plays', 'basketball']


# -----------------------------------------------------------------------------
# ------ Return True if either string occurs anywhere inside the other. -------
def isIn(a,b):  
    if len(a) > len(b):  
        longerStr = a  
        shorterStr = b  
    else:  
        longerStr = b  
        shorterStr = a     
    lenShortStr = len(shorterStr)      
    for ii in range(len(longerStr)-lenShortStr+1):  
        if shorterStr == longerStr[ii : ii+lenShortStr]:  
            print(shorterStr)  
            return True  
    return False      

# function call:
isIn('hell abcd','cd') # True  


# -----------------------------------------------------------------------------
# ------------------------------ XXX ---------------------------------
