'''imports'''
# import matplotlib
# import numpy as np
# import pandas as pd
# from collections import namedtuple
# from matplotlib import pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
'''Sub Code '''

"""
joeOrder = "UUUUUUUUDRLRLRRFRFRFBFFBLBLDDDDDDDDULRFRLLRLBBBBFBBLFF"#U + R + F + D + L + B
for i in ["U", "R", "L", "D", "B", "F"]:
    print(i,"=",joeOrder.count(i))
print(kociemba.solve(joeOrder))
"""

import kociemba
from random import randint
num = 6
U = "LUBBUDRDU"
R = "BBRFRBLDU"
F = "DLRBFRUFD"
D = "RUFRDFFFB"
L = "DRFULLUDF"
B = "DRBUBLLLL"

class QB:   #Every individual QB has 6 sides with 26 (27 with the centre never seen) cubes
    sides = dict(white="U", green="F", red="R", orange="L", blue="B", yellow="D")  
    def __init__(self, colour, current_face, number):
        self.colour = colour
        self.real_face = QB.sides[colour]
        self.current_face = QB.sides[colour]
        self.cubi_number = number
    
    def __repr__(self):
        return str((self.colour, self.real_face, self.current_face, self.cubi_number))

class Cube:
    #all9 = []
    def __init__(self):
        self.cube = []#URFDLB
    
    def create_cube(self):
        valids = ["U", "R", "L", "D", "B", "F"]*9
        for c in ["white", "red", "green","yellow", "orange", "blue"]:
            for i in range(9):
                face = valids.pop(randint(0, len(valids)-1))
                self.cube.append(QB(c, face, i+1))
    
    def solve(self):
        order = input("Enter the Rubik's cube orientation: ") #"".join(qb.current_face for qb in self.cube)
        print(order)
        for i in ["U", "R", "L", "D", "B", "F"]:
            correct = (i,"=",order.count(i))
            print(correct)
            #Cube.all9.append()
        return kociemba.solve(order)

''' Unneeded due to to being used in main code'''
# wqer = U + R + F + D + L + B
c = Cube()
##print(Cube.all9)
print(c.solve())
# ''' Sam certified '''