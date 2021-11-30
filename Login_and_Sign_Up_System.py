### Imports ###
import sys
import time
import _json
from tkinter.constants import FALSE
import string
#import mysql.connector

### Main Code ###
class Master_Login_SignUp:  ### Uses both Login and Sign Up in a master function ###
    times = dict(first = 10, second = 60, third = 600, fourth = 3600)
    characters = string.ascii_letters + string.digits + string.punctuation     ### All characters that are allowed in the passcode
    def __init__(self):
        self.correct = False
        self.chance1 = 0

    def Login(self):
        while self.correct == False and self.chance1 <= 3:
            Username = input("Enter your Username: ")
            ## Make Username checker using database
             
            while self.correct == False and self.chance1 <= 3:
                Password = input("Enter Password: ") ### Make all '*' when on GUI to remain annonymous
                ## Add Password checker using a database 
 
                if self.chance1 <=3:
                    time.sleep(self.times[0+self.chance1])
                    self.chance1 += 1
            
    def SignUp(self):
        username_check = False
        while username_check == False:
            Username = input("Make a username: ")
            UsernameCheck = input("Are you sure you want {} as your username(Y / N): ".format(Username))
            if UsernameCheck.upper() == 'Y' or UsernameCheck.upper() == 'YES':
                username_check = True
         
        password_check = False
        while password_check == False:
            password_check = True
            Password = input("Make a Password: ")  
            for i in range(len(Password)):
                if Password[i] not in self.characters:
                    password_check = False
                    break
            if password_check:
                PasswordVerify = input("Please verify your Password: ")
                if PasswordVerify == Password:
                    time.sleep(2)    ############################ Add Username and Password to data base ##########
                    print("You have succesfully made a username and password ")
 
#
#  '''
# if Master_choice == 'L':
#     logingIn = Login(chance3)
#     print(logingIn)
# elif Master_choice == 'S':
#     SigningUp = SignUp()
#    print(SigningUp)'''

# Maincode = Master_Login_SignUp() 

