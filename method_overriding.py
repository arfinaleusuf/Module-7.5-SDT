# method overriding
"""
Parent class এর method কে child class এ redefine (override) করা
"""

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):  # overriding
        print("Dog barks")

d = Dog()
d.sound()   # Dog barks