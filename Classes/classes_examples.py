#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Dr Ekaterina Abramova, 2017

Classes - example class, invisible attributes
"""
# -----------------------------------------------------------------------------
# ------------------------- example of a class --------------------------------
class exampleClass(object):
    """
    I am a docstring - a string giving specification:
        (a) Assumptions: parameters and their constraints.
        (b) Guarantees: conditions that are met by the class (its purpose).
        (c) return
    Note: the docstring gives information on the abstraction provided by class, 
    not information on how the class is implemented. """
    # Comments to give information about the implementation.
    # This info is amied at programmers who want to modify the implementation. 
    
    def __init__(self):
        # variable attributes:
        self.vals = [] # instance variable
          
    # method attributes:
    def method1(self,e):
        print('I am an method 1')
        if e not in self.vals:
            self.vals.append(e) 
        
    def method2(self):
        print('I am an method 2')
        
    def __str__(self):
        return str(self.vals)
  
print(type(exampleClass))   # <class 'type'>
myInstance = exampleClass() # creates an object myInstnce of type exampleClass  
print(type(myInstance))     # <class '__main__.exampleClass'>
print(type(myInstance.method1)) # <class 'method'>  

myInstance.method1(45)
myInstance.method1(46)
# Equivalent ways of calling __str__ method:
print(myInstance)                       # most convinient form. Ans: [45,46]
print(myInstance.__str__())             # less convinient form. Ans: [45,46]
print(exampleClass.__str__(myInstance)) # less convinient form. Ans: [45,46]


# -----------------------------------------------------------------------------
# ----------------------- insivisble attributes -------------------------------
class infoHolding(object):
    def __init__(self):
        self.visible = 'Look at me'
        self.__alsoVisible__ = 'Look at me too'
        self.__invisible = 'Don\'t look at me directly'
    
    def printVisible(self):
        print(self.visible)
        
    def printInvisible(self):
        print(self.__invisible)
        
    def __printInvisible__(self):
        print(self.__invisible)
        
    def __printInvisible(self):
        print(self.__invisible)
        
class subClass(infoHolding):
    def __init__(self):
        print(self.__invisible)

test = infoHolding()

# test variable attributes
test.visible # 'Look at me'
test.__alsoVisible__ # 'Look at me too'
test.__invisible # AttributeError: 'infoHolding' object has no attribute '__invisible'

# test method attributes
test.printVisible() # 'Look at me'
test.printInvisible() # Don't look at me directly
test.__printInvisible__() # Don't look at me directly 
test.__printInvisible() #  AttributeError: 'infoHolding' object has no attribute '__printInvisible'

# subclass can't access it either!!!
testSub = subClass() # AttributeError: 'subClass' object has no attribute '_subClass__invisible'


# ------------------------------ BAD PRACTICE 
# OVERWRITING VARIABLE ATTRIBUTES
test.visible = 'Be careful!' # allowed peration
print(test.visible) # Be careful!

# OVERWRITING METHOD ATTRIBUTES
mess = infoHolding()
print(mess.printVisible) # Be careful!
mess.printVisible = test.__printInvisible
print(mess.printVisible) # AttributeError: 'infoHolding' object has no attribute '__printInvisible'