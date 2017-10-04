#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Dr Ekaterina Abramova, 2017
STRUCTURED TYPES.

Sequence type: lists
"""
# -----------------------------------------------------------------------------
# ----------------------------- create a list ---------------------------------
L = []

#  List Comprehension 
L1 = [ii for ii in range(5)] # [] make it a list. New list L1 = [0,1,2,3,4,5]. 
L2 = [x**2 for x in range(1,7) ] # new list L2 = [1,4,9,16,25,36]

# typcast range (which is a generator) to a list
L2 = list(range(10)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

mixed = [1, 2, 'a', 3, 4.0]
L = [x**2 for x in mixed if type(x) == int] # [1, 4, 9]

mylist = [x*x for x in range(3)] 
for ii in mylist:
    print(ii)
# 0, 1, 4  


# -----------------------------------------------------------------------------
# ---------------------------- simple operations ------------------------------
L = ['H',"e", 'l', 1,"o"]
for ii in L:
    print(ii)
# H e l 1 o

# Looping 
L = [] 
for ii in range(10):
    L.append(ii)
print(L) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 

# extend vs append method
L1 = [1,2,3]
L2 = [4,5,6]
L3 = L1 + L2
print( 'L3 =', L3 ) # [1, 2, 3, 4, 5, 6]
L1.extend(L2) # list concatenetion 
print( 'L1 =', L1 ) # [1, 2, 3, 4, 5, 6]
L1.append(L2) # structure is maintained, get list inside a list 
print( 'L1 =', L1 ) # [1, 2, 3, 4, 5, 6, [4, 5, 6]]
  
    
# -----------------------------------------------------------------------------
# ------------------------- side effects / aliasing ----------------------------
Techs = ['MIT', 'Caltech']
Ivys = ['Harvard', 'Yale', 'Brown']
Univ = [Techs, Ivys]
Techs.append('RPI') 
# Obj to which Univ is bound still contains 2 lists, but their contents have changed.
print(Univ) # [['MIT', 'Caltech', 'RPI'], ['Harvard', 'Yale', 'Brown']]


# -----------------------------------------------------------------------------
# ------------------- build a list of integer values --------------------------
L = []   # empty list 
for ii in range(10):
    L.append(ii)
print(L) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# ------------ build a lsit of integer values raised to power n ---------------  
# via for append
def powers_forLoop(pwr, N=5):
    L = []
    for ii in range(N):
        L.append(ii**pwr)
    return L

# via comprehension
def powers_listComprehension(pwr, N=5):
    L = [ii**pwr for ii in range(N)]  
    return L

# use next 2 lines on the IPython command line   
# %timeit powers_forLoop(2,1000) # 1000 loops, best of 3: 332 µs per loop   
# %timeit powers_listComprehension(2,1000) # 1000 loops, best of 3: 253 µs per loop

# --------------- remove duplicate characters from 2 strings ------------------
def removeDups(L1,L2):
    newL = L1 # safe copy of L1
    print(id(newL)==id(L1)) # True 
    for e1 in newL:
        if e1 in L2:
            L1.remove(e1) # mutates original list L1
L1 = [1,2,3,4]
L2 = [1,2,5,6]
removeDups(L1,L2)
print(L1) # [2, 3, 4]

# ----------------- find position of an int  within a list -------------------- 
def findPos(L):
    num = 5 # number to be found  
    index = 0
    found = False
    while not found:
        if L[index] == num:
            found = True
            print(index+1)
        elif index == (len (L)-1):
            print('Number not in list')
            break # come out of current loop 
        index += 1
# function call        
L = [1,2,4,5,4,5,6]
findPos(L)