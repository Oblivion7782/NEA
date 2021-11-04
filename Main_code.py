###
"""The Main Code is going to be used to connect the other pieces of code together and paste it into a visual workplace"""
###
'''imports'''
import itertools
import json
#import matplotlib
#import numpy    
import random
from sys import exit
#from tkinter import * 
#from tkinter.ttk import *
import Cube_Solving_Algorithm
import Login_and_Sign_Up_System

cube = True
'''Main Code '''
# window = Tk()

# greeting = Label(text="ok")
# greeting.pack()
# window.mainloop()

# master = Tk()
# master.geometry("1000x750 + 300 + 300")

# #wqer = U + R + F + D + L + B
# Cube_Solving_Alg = Cube_Solving_Algorithm.Cube()
# Cube_Solving_Alg.create_cube()
# #checkCube()
# print(Cube_Solving_Alg.cube)
# print(Cube_Solving_Alg.solve())

Cube_Solving_Alg = Cube_Solving_Algorithm.Cube()
#checkCube()
while cube == True:
    print(Cube_Solving_Alg.cube)
    print(Cube_Solving_Alg.solve())
    if Cube_Solving_Alg.solve() == """U = 9, R = 9, L = 9, D = 9, B = 9, F = 9""":


#Login_and_SignUp_System = Login_and_Sign_Up_System.Master_Login_SignUp()
#Login = Login_and_SignUp_System.Login()
#SignUp = Login_and_SignUp_System.SignUp()
#print(Login)
#print(SignUp)







