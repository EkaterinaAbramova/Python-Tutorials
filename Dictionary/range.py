#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Dr Ekaterina Abramova, 2017

RANGE
"""

# -------------------------------------- range
range(4)   # stop = 4.            Default start = 0, step = 1
range(0,4) # start = 0, stop = 4. Default step = 1   
 
   
print(range(10)[2:6])    # sliced to give range(2, 6)
print(range(10)[2:6][2]) # indexed to give 4 

range(0,7,2) == range(0,8,2)   # True,  (0,2,4,6) (0,2,4,6)
range(0,7,2) == range(6,-1,-2) # False, (0,2,4,6) (6,4,2,0)
print( list(range(6,-1,-2)) )
