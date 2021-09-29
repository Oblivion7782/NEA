### Imports ###
import sys
import time
import _json
from tkinter.constants import FALSE
#import mysql.connector

### Main Code ###
class Master_Login_SignUp:  ### Uses both Login and Sign Up in a master function ###
    timeing = dict(first = 10, second = 60, third = 600, fourth = 3600, fith = 36000)
    allowed = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", "1", "2", "3", "4", "5", 
           '6', '7', '8', '9', '0', '!', '"', '£', '%', '$', '^', '&', '*', '?', '/', '+', '=', "#", '+', '¬', '`', '<', '>', 'A', 'B', 'C', 'D',
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']  
           ### All characters that are allowed in the passcode

    def __init__(self):
        self.correct = False
        self.chance1 = 0
        self.times = Master_Login_SignUp.timeing
        self.characters = Master_Login_SignUp.allowed
        
    def Login(self, chance1, correct, timeing):
        while correct == False and chance1 <= 3:
            Username = input("Enter your Username: ")
            ## Make Username checker using database
            
            while correct == False and chance1 <= 3:
                Password = input("Enter Password: ") ### Make all '*' when on GUI to remain annonymous
                ## Add Password checker using a database 

                if chance1 <=3:
                    time.sleep(timeing[0+chance1])
                    chance1 += 1
           
    def SignUp(self, characters, correct):
        checks = correct #checks = False
        while checks1 == False:
            Username = input("Make a username: ")
            UsernameCheck = input("Are you sure you want {} as your username(Y / N): ".format(Username))
            if UsernameCheck == 'Y' or UsernameCheck == 'Yes':
                checks1 = True
        
        while checks == False:    
            Password = input("Make a Password: ")  
            for i in range(len(Password)):
                if Password[i] not in characters:
                    PasswordVerify = input("Please verify your Password: ")
                if PasswordVerify == Password:
                    time.sleep(2)    ############################ Add Username and Password to data base ##########
                    print("You have succesfully made a username and password ")

# '''
# if Master_choice == 'L':
#     logingIn = Login(chance3)
#     print(logingIn)
# elif Master_choice == 'S':
#     SigningUp = SignUp()
#    print(SigningUp)'''

# Maincode = Master_Login_SignUp() 

