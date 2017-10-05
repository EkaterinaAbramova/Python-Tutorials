#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Dr Ekaterina Abramova, 2017

Classes - inheritence, overriding attributes, polymorphism.
"""
# -----------------------------------------------------------------------------
# ----------------------- __lt__() function -----------------------------------
class Person(object): # superclass inherits all properties of 'object'
    # __lt__ is a special function that overlaods < operator
    def __init__(self,name):
        """Create a person"""
        self.lastName = name
    
    def __lt__(self,otherName):
        """Returns True if self preceds otherName in althabetical order. 
        False otherwise"""
        return self.lastName < otherName.lastName


# -----------------------------------------------------------------------------
# ---------------- override attributes of superclass --------------------------
# 1. __init__
# 2. __lt__
class MITPerson(Person): # subclass inherits all properties of class Person.
    nextIdnum = 0  # class variable 
    
    def __init__(self,name):
        Person.__init__(self,name) # overrides superclass Person's __init__
        self.idNum = MITPerson.nextIdnum
        MITPerson.nextIdnum += 1
    
    def getIdNum(self):
        return self.idNum
    
    def __lt__(self,otherName): # overrides superclass Person's __lt__
        return self.idNum < otherName.idNum
    
p1 = MITPerson('Smith') 
p2 = MITPerson('Jones') 
p4 = Person('Grant') 
print(p1.idNum) # 0
print(p2.idNum) # 1
print(p1<p2)    # uses method __lt__ from MITPerson subclass. True
print(p4<p1)    # shorthand for p4.__lt__(p1), ie uses superclass __lt__ method. True
# print(p1<p4)  # AttributeError: 'Person' object has no attribute 'idNum'. Since object p4 has no idNum.


# -----------------------------------------------------------------------------
# ----------------------- mulitple levels of inheritence ----------------------
class Student(MITPerson): 
    pass
class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear 
    def getClass(self):
        return self.year
class Grad(Student): 
    pass

p5 = Grad('Buzz Aldrin')
p6 = UG('Billy Beaver', 1984)
print(type(p5)) # <class '__main__.Grad'>
print(type(p6)) # <class '__main__.UG'>
print(p5, 'is a graduate student is', type(p5) == Grad)     # True
print(p5, 'is an undergraduate student is', type(p5) == UG) # False

print(p5.isStudent()) # True
print(p2.isStudent()) # False


# -----------------------------------------------------------------------------
# ---------------------------- polymorphism -----------------------------------
# Polymorphism with a function
class Bear(object):
    def sound(self):
        print("Groarrr")
 
class Dog(object):
    def sound(self):
        print("Woof woof!")

def makeSound(animalType):
    animalType.sound()
 
bearObj = Bear()
dogObj = Dog()
makeSound(bearObj)
makeSound(dogObj)

# ----- Polymorphism with a class
class Animal:
    def __init__(self,name):
        self.name = name
    def sound(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Bear(Animal): # inheritance
    def sound(self):
        return "Groarrr"
 
class Dog(Animal): # inheritance
    def sound(self):
        return "Woof woof!"

# names are initialised in the constructor of type Animal
animals = [ Bear('myBare1'), Dog('myDog'), Bear('myBare2') ] 
for animal in animals:
    print (animal.name + ': ' + animal.sound())