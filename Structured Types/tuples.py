#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Dr Ekaterina Abramova, 2017
STRUCTURED TYPES.

Sequence type: tuples
"""
# -----------------------------------------------------------------------------
# ---------------------------- Simple Operations ------------------------------
for ii in (1, 'two', 3):
    print(ii)
# 1, 'two', 3
    
t1 = ()   # empty tuple
type(t1)  # tuple
print(t1) # ()

t2 = (1) 
type(t2)  # int
print(t2) # 1

t3 = (1,) # MUST INLCUDE COMMA FOR SINGLE ELEMENT TUPLE
type(t3)  # tuple
print(t3) # (1,)

t =  ('I did it all', 4, 'Love')
     
t = 3*('a',2) # ('a', 2, 'a', 2, 'a', 2)   
    
t1 = (1, 'two', 3)   
t2 = (t1, 3.25) 
print(t2) # ((1, 'two', 3), 3.25)
    
print(t1 + t2) # 1, 'two', 3, (1, 'two', 3), 3.25)    
print( (t1 + t2)[3] )  # (1, 'two', 3)   
print( (t1 + t2)[2:5] ) # (3, (1, 'two', 3), 3.25) 

# -----------------------------------------------------------------------------
# --------------------- Find identical items in 2 tuples ----------------------
def intersect(t1, t2):      
    result = () # empty tuple  
    for e in t1: # iterate over tuple using for loop 
        if e in t2:  
            result += (e,)  
    return result 

# function call:   
t1 = (1, 'two', 3)     
t2 = ('two', 3)       
intersect(t1, t2) # ('two', 3) 













