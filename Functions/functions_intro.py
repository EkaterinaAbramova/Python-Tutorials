#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Dr Ekaterina Abramova, 2017

Functions -  simple functions coded explicitly
"""
# -----------------------------------------------------------------------------
# ----------------------- max, min for floats and lists -----------------------
def max_float(a,b):
    if(a >= b):
        return a
    else:
        return b
ans = max_float(2.3, 5.5)
print(ans) # 5.5


def max_list(L):
    maxVal = L[0] # current max value
    for ii in L[1:]: # compare to each element of list from 1 to end
        # OPTION 1
#        if ii > maxval:
#            maxval = ii
        # OPTION 2
        maxVal = max_float(maxVal, ii)
    return maxVal
L = [1, 2, 3, 4, 5]
ans = max_list(L)
print(ans) # 5


def min_float(a, b):
    return -max_float(-a, -b)
ans = min_float(2, 5)
print(ans) # 2


def min_list(L):
    minVal = L[0]
    for ii in L[1:]:
        minVal = min_float(minVal, ii)
    return minVal
L = [1, 2, 3, 4, 5]
ans = min_list(L)
print(ans) # 1


# -----------------------------------------------------------------------------
# ------------------ absolute value of an int / float -------------------------
def abs_val(a): 
    if a < 0:
        return -a
    else:
        return a
ans = abs_val(-10)
print(ans)


# -----------------------------------------------------------------------------
# ------ golden ratio / Newton Euler pi / Wallis pi approximations ------------
import math
golden_ratio = 0.5 * (1 + math.sqrt(5))
print(golden_ratio) # 1.618033988749895

def fact(n): # declare factorial function before using (in Newton-Euler below)
    acc = 1
    for ii in range(1,n+1):
        acc *= ii
    return acc
# test
for jj in range(0,6): # i.e. (0,1,2,3,4,5)
    print(fact(jj)) # 1 1 2 6 24 120

def Newton_Euler_pi(tol):
    k = 0
    diff = 10 # arbitrarily large
    pi_new = 0
    pi_old = 10
    while diff > tol:
        pi_new += ( 2**k * fact(k)**2 ) / fact(2*k + 1)
        diff = abs_val(pi_new - pi_old)
        pi_old = pi_new
        k += 1
    return 2*pi_new, k    
print(Newton_Euler_pi(0.00001)) # (3.1415797881375944, 16)   
    
def Wallis_pi(tol):
    k = 1
    diff = 10 # arbitrarily large
    pi_new = 2
    pi_old = 10
    while diff > tol:
        pi_new *= (4 * k**2) / (4 * k**2 - 1)
        diff = abs_val(pi_new - pi_old)
        pi_old = pi_new
        k += 1
    return pi_new, k    
print(Wallis_pi(0.00001)) # (3.138803846846745, 282)