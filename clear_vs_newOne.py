'''
Created on Jul 2, 2014

@author: viejoemer

Difference between dict.clear() and assigning {} in Python?

¿Diferencia entre dict.clear () y asignar {} en Python?

'''

#Creating a dict with data
d = {
     "red":100,
     "yellow":200,
     "blue" : 300
     }

#Reference to the same dict 
d_clone = d
print(d_clone)
print(d)

#Cleaning the dict
d.clear()

#This clean both of them.
print(d_clone)
print(d)

d = {
     "red":100,
     "yellow":200,
     "blue" : 300
     }

#if you use {} to "clean" a dict, this gonna create a new one.
#and the other keep the values.
d_clone = d
d = {}
print(d_clone)
print(d)