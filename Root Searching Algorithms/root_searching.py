#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Dr Ekaterina Abramova, 2017

Root Searching Algorithms
"""
# -----------------------------------------------------------------------------
# -------------------- Bisection: find square root ----------------------------
def Bisection1(S):   
    """ Parameters: S number to be square rooted.
        Return: g - approximate sq root, 
            count - number of iterations """
    # set search range
    if S > 0:
        a = 1
        b = S
    else:
        a = S
        b = 1
    eps = 0.001
    # fog - f(g) is funciton of g
    fog = eps*2 # initialse to anything bigger than eps 
    count = 0
    while abs(fog) > eps:
        g = 0.5*(a+b) # it is faster to multiply than divide
        fog = g**2 - S 
        count += 1
        if fog > 0:
            b = g
        else:
            a = g    
    return g, count
# function call
print(Bisection1(9.5)) # (3.0821990966796875, 15)

# ---------------------- Bisection: find pwr root -----------------------------
def Bisection(S,pwr,eps):
    """ Assumes S and eps int/float, pwr is int, eps > 0, power >= 1
    Returns float 'guess' s.t. guess**pwr is within eps of x and number of 
    iterations 'count'. If such a float does not exist, it returns None """
    if (pwr%2 == 0 and S < 0):
        return None # Cannot input a negative number for an even power
    low = min(-1.0, S)
    high = max(1.0, S)
    # fog - f(g) is funciton of g
    fog = eps*2
    count = 0
    while abs(fog) > eps:
        guess = 0.5*(low+high)
        fog = guess**pwr - S # f(g)
        if fog > 0:
            high = guess
        else:
            low = guess  
        count += 1
    return guess
# function call
print(Bisection(-64, 5, 0.001)) # (-2.297393798828125, 21)
print(Bisection(0.29, 2, 0.001)) # (0.5390625, 8)

# test Bisection is working
def testFindRoot():
    epsilon = 0.0001
    for x in (0.25, -0.25, 2, -2, 8, -8):
        for power in range(1, 4):
            print('Testing x = ', str(x), ' and power = ', power)
            result = Bisection(x, power, epsilon)
            if result == None:
                print(' No root')
            else:
                print(' ', result**int(power), '~=', x)
testFindRoot()                


# -----------------------------------------------------------------------------                
# ------------------- Newton Raphson: f(x) = (x**2 - S) -----------------------
def Heron_of_Alexandria(S):
    g = 0.5*S
    eps = 0.01
    count = 0
    while abs(g*g - S) > eps:
        g = 0.5*(g + S/g)
        count += 1
    return g, count
guess, count = Heron_of_Alexandria(122) 
print(guess, count) # (3.000015360039322, 3)

# ------------------ Newton Raphson: f(x) = (x**pwr - S) ----------------------
def newtonRaphson(S, pwr, eps):
    if (pwr%2 == 0 and S < 0):
        return None # Cannot input a negative number for an even power
    guess = 0.5*S
    while abs(guess**pwr - S) >= eps:
        guess = guess - ((guess**pwr) - S) / (pwr*guess**(pwr-1)) 
    return guess

# test NR is working
def testFindRoot2():
    epsilon = 0.0001
    for x in (0.25, -0.25, 2, -2, 8, -8):
        for power in range(1, 4):
            print('Testing x = ', str(x), ' and power = ', power)
            result = newtonRaphson(x, power, epsilon)
            if result == None:
                print(' No root')
            else:
                print(' ', result**int(power), '~=', x)
testFindRoot2() 









