#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Dr Ekaterina Abramova, 2017

Factorials
"""
# -----------------------------------------------------------------------------
# --------------------- Calculate factorial via for loop  ---------------------
def fact_iter_for(n):
    acc = 1
    for ii in range(1,n+1):
        acc *= ii
    return acc
# test function is working correctly
for jj in range(0,6): # i.e. (0,1,2,3,4,5)
    print(fact_iter_for(jj)) # 1 1 2 6 24 120

# ------------------- Calculate factorial via while loop  ---------------------
def factorial_iter_while(n):
    ans = 1
    while n > 0:
        ans = ans*n
        n -= 1
    return ans
# function call
print(factorial_iter_while(4)) # 24

# -------------------- Calculate factorial via recursion  ---------------------
def factorial_recursive(n):
    # Base case
    if n == 1:
        return n
    # General case
    return n*factorial_recursive(n-1) # General case moves towards Base case
# function call
print(factorial_recursive(4)) # 24