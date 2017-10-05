#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Dr Ekaterina Abramova, 2017

Worked through solutions to finger exercises, Guttag 2nd edition, 2016.
"""

# ----------------------------- exercise p 18 --------------------------------- 
""" Write a program that examines three variables x, y, z and prints largest 
odd number among them. If none are odd, print a message to that effect. """
def findOdd(L):
    oddNs = []
    # find odd numbers
    for ii in L:
        if ii%2 != 0: # if int is odd
            oddNs.append(ii)
    # find largers int
    if len(oddNs) != 0: # if odd numbers present
        print(max(oddNs))
    else: 
        print('No odd numbers present')
# funciton call
L = [-3,-2,-5]
findOdd(L) # -3


# ----------------------------- exercise p 24 --------------------------------- 
""" Replace the comment in the following code with a while loop """
numXs = int(input('How many times should I print the letter X?'))
toPrint = ''
# concatenate X to toPrint numXs times
while numXs > 0: 
    toPrint = toPrint + 'X'
    numXs -= 1 # decrement numXs
print(toPrint)


# ----------------------------- exercise p 24 --------------------------------- 
""" Write a program that asks user to input 10 integers, and prints largest odd 
number. If no odd number was entered, print a message to that effect.  """
# build up input from user
myInts = []
for ii in range(10):
    temp = int(input('Please input an integer.'))
    myInts.append(temp) 
# untilse a function already written for finding largest odd number in a list
findOdd(myInts)


# ----------------------------- exercise p 27 --------------------------------- 
""" Write a program that asks user to enter an integer and prints two integers
root and pwr, such that 0<pwr<6 and root**pwr is equal to the integer entered 
by user. If no such pair exists it should print a message to that extent """

def root_pwr(x):
    # x = int(input('Write int ')) # typecast input string into an int
    max_power = 6
    marker = False
    for pwr in range(2,max_power+1):
        ans = 0
        while ans**pwr < abs(x): # stop at the potential root
            ans += 1       
        # check if exact root is found
        if ans**pwr == abs(x):
            if (x < 0) and (pwr%2 != 0): # deal with negative input & odd power
                ans = -ans
                marker = True
                print('For', x, 'base:', ans, 'power:', pwr)      
            elif (x > 0):
                marker = True
                print('For', x, 'base:', ans, 'power:', pwr) 
    if not marker:    
        print('For', x, 'no such pair exists')
# Good coding: write a test function to check fn behaviour over many inputs.
def test_root_pwr():
    for ii in range(-10,11):
        root_pwr(ii)
# function call
test_root_pwr()        


# --------------------------- exercise p 30 -----------------------------------
""" s is a string with a sequenc of decimal numbers separated by commas. 
Write a program that prints the sum of numbers in s. """
def sumStr(s):
    temp_str = ''
    L = []
    for ii in s: # sum up the floats in the string
        if ii != ',':
            temp_str = temp_str + ii
        else:
            L.append(float(temp_str))    
            temp_str = ''
    L.append(float(temp_str)) 
    ans = 0
    for ii in L:
        ans = ans + ii
    print(ans) 
# funtion call
sumStr('1.23,2.4,3.123') # 6.753


# --------------------------- exercise p 34 -----------------------------------
""" What would happen if x = 25 was replaced by x = -25 in Fig 3.4? """
# The while loop condition would always be true since 25 would always be added 
# to the ans**2 value and would thus result in an infinite loop.


# --------------------------- exercise p 34 -----------------------------------
""" How would code in Fig 3.4 need to be changed for finding an approximation 
to the cube root of both negative and positive nubmers? """
# x can be positive or negative
x = -25
epsilon = 0.01
numGuesses = 0
# change low to accomodate negative numbers
low = min(-1.0, x)
high = max(1.0, x)
ans = (high + low) / 2.0
# change power to 3
while abs(ans**3 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    # change power to 3
    if ans**3 < x:
        low = ans
    else: 
        high = ans
    ans = (high + low) / 2.0
print('numGuesses =', numGuesses)
print(ans, 'is close to cube root of', x)


# --------------------------- exercise p 35 -----------------------------------
""" What is the decimal equivalent of binary number 10011? """
# (2^4 x 1) + (2^3 x 0) + (2^2 x 0) + (2^1 x 1) + (2^0 x 1) = 16 + 2 + 1 = 19


# --------------------------- exercise p 38 -----------------------------------
""" Count number of iterations of Newton-Raphson method and compare the 
efficiency to Bisecion """
# write a function for Bisection (for finding a root of f(x) = x**pwr - S)
def bisection(S, pwr):
    epsilon = 0.01
    numGuesses = 0
    low = min(-1.0, x)
    high = max(1.0, x)
    guess = (high + low) / 2.0
    while abs(guess**pwr - x) >= epsilon:
        numGuesses += 1
        if guess**pwr < x:
            low = guess
        else: 
            high = guess
        guess = (high + low) / 2.0
    return guess, numGuesses

# write a function for Newton-Raphson (for finding a root of f(x) = x**pwr - S)
def newtonRaphson(S, pwr):
    epsilon = 0.01
    guess = S/2.0
    numGuesses = 0
    while abs(guess**pwr - S) >= epsilon:
        numGuesses += 1
        guess = guess - ((guess**pwr) - S) / (pwr*guess**(pwr-1)) 
    return guess, numGuesses

# test which function is faster:
S, pwr = 27, 3
# (a) look at number of iterations
root, iters = bisection(S, pwr)     # 2.92364501953125  14
root, iters = newtonRaphson(S, pwr) # 3.000000081210202 7
# (b) look at the average speed using timeit built-in function
# exectue both lines below in the command line:
# %timeit bisection(S, pwr) # 100000 loops, best of 3: 5.83 µs per loop
# %timeit newtonRaphson(S, pwr) # 100000 loops, best of 3: 3.34 µs per loop


# ---------------------------- exercise p 42 ----------------------------------
""" Write a function isIn that accepts 2 strings as arguments and returns True 
if either string occurs anywhere in other, False otherwise."""
# Option 1: using str operation 'in'
def isIn(a,b):
    if len(a) > len(b):
        longerStr = a
        shorterStr = b
    else:
        longerStr = b
        shorterStr = a   
    if shorterStr in longerStr:
            print(shorterStr)
            return True
    return False

# Option 2: stepping over longer string, looking for a match to shorter one
def isIn2(a,b):
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

# function call     
isIn('hell abcd','abcd') # True
isIn2('hell abcd','abcd') # True


# ------------------------------ exercise p 54 --------------------------------
""" When implementation of fib in Fig 4.7 is used to compute fib(5), how many 
times doesit compute the value of fib(2) on the way to computing fib(5)? """
# fib(5) --> fib(4) +   fib(3)
#            |              |
#      fib(3)+fib(2)        fib(2)+fib(1)
#         |      |             |
#         |  fib(1)+fib(0)     fib(1)+fib(0)
#  fib(2)+fib(1)            
#   |              
# fib(1)+fib(0)

# Therefore fib(2) is called 3 times.