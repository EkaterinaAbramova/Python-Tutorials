#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Dr Ekaterina Abramova, 2017


INTENDED USE:
Tutorial on different ways of calculating a Fibonacci sequence and returning 
n-th element of this sequence.
Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21 etc
n-th element index: 1, 2, 3, 4 ,5, 6, 7, 8,  9  etc


PARAMETERS:
n - the position of an element in a sequence, assumes n >= 2
e.g: for n = 1, the answer is 0
     for n = 2, the answer is 1
     for n = 7, the answer is 8.


RETURN:
fib_iterative: Fibonacci seq up to element n and the last element of this seq.
fib_recursive: Value of the Fibonacci sequence at the n-th element.
"""

# ------------ Simple iterative implementation using a for loop ---------------
def fib_iterative(n):
    """Calcualte n-th element of Fibonacci sequence. Assumes n >= 2
    Returns: Fibonacci sequence up to element n, and n-th element of the seq.
    """        
    fibSeq = [0, 1] # base case
    for ii in range(2,n): # note: list(range(2,2)) is an empty list []
        fibSeq.append(fibSeq[ii-2]+fibSeq[ii-1])
    nthElem = fibSeq[-1] # last element of the list  
    return fibSeq, nthElem 
n = 8 # find n-th element of Fib seq.
seq, elem = fib_iterative(n)
print(seq, elem) # [0, 1, 1, 2, 3, 5, 8, 13] 13  

# ------------------ Fibonacci: calculate i^th element ------------------------
def fib_recursive(n):
    """Calcualte n-th element of Fibonacci sequence.
    Returns: Fibonacci n-the element.
    """
    if n == 0:   # base cases
        return 0
    elif n == 1:
        return 1
    else:        # general case
        return (fib_recursive(n-1) + fib_recursive(n-2)) # use recursion
n = 6 # find n-th element of Fib seq.
elem = fib_recursive(n-1) # decrement by 1, since Python indexes elems from 0.
print(elem) # 5