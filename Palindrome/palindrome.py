#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Dr Ekaterina Abramova, 2017

Palindromes: via recursive function
"""
# -----------------------------------------------------------------------------
# ----------------------- Check if string is a palindrome ---------------------
def isPalindrome(s): 
    print('Raw string is: ', s)
    """Parameters: s - str
       Returns: True if letters in s form a palindrome; False otherwise. 
       Non-letters and capitalization are ignored."""
    # remove non-letters and capitalisation
    def toChars(s): 
        s = s.lower() # make all letters lower case
        letters = '' 
        for c in s:   # remove non-letters
            if c in 'abcdefghijklmnopqrstuvwxyz': 
                letters = letters + c
        return letters
    # recursive part
    def isPal(s):
        print(s)
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1]) # called recursively
    return isPal(toChars(s)) # the first line executed in isPalindrome()

# function call
isPalindrome('dogGod')