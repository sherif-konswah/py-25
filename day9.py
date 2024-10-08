# course link https://www.youtube.com/watch?v=H2EJuAcrZYU
#<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Start From Time 4:39:00 To 4:56:30
# #<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

print("********* Modules *********")
import math
import sys
import random as rdm # rdm as alias you can call it
from enum import Enum




print(math.pi)
print(rdm.choice("123"))

# note if you import from the calling will change 
# from math import pi
# print(pi)

print('---------------')
for item in dir(rdm):
    print(item)

print('---------------')
# you can call by module alians
print(rdm.choice("456"))


# using in functions
def randfuc():
    funahly = [
        "Ahli is biggest club in affrica",
        "Ahly Won 12 Championship league - CAF",
        "Ahly Won 44 Egyption League",
        "Ahly is a great club"
    ]
    
    index = rdm.choice("0123")
    print(funahly[int(index)])


randfuc()




