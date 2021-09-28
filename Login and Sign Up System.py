### Imports ###
import sys
import time
import _json
#import mysql.connector

allowed = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", "1", "2", "3", "4", "5", 
           '6', '7', '8', '9', '0', '!', '"', '£', '%', '$', '^', '&', '*', '?', '/', '+', '=', "#", 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']  ### All characters that are allowed in the passcode
chance3 = [10, 60, 600, 3600, 36000]

### Main Code ###
def Master_Login_SignUP(chance3):  ### Uses both Login and Sign Up in a master function ###
    #account = input("Do you have an account(Y / N)? ") 
    Master_choice = input("Login or Sign Up (L / S)? ") # Will be buttons on the GUI
    
    if Master_choice == 'L':
        logingIn = Login(chance3)
        print(logingIn)
    elif Master_choice == 'S':
        SigningUp = SignUp()
        print(SigningUp)

def Login(chance3):
    correct1 = False
    correct2 = False
    chance1 = 0
    chance2 = 0
    chance = 1
    while correct1 == False and chance1 <= 3:
        Username = input("Enter your Username: ")
        ## Make Username checker using database
        
        while correct2 == False and chance2 <= 3:
            Password = input("Enter Password: ") ### Make all '*' when on GUI to remain annonymous
            ## Add Password checker using a database 

            if chance1 <=3 or chance2 <= 3:
                time.sleep(chance3[-1+chance])
                chance += 1
        

def SignUp():
    checks1 = False
    checks2 = False
    while checks1 == False:
        Username = input("Make a username: ")
        UsernameCheck = input("Are you sure you want {} as your username(Y / N): ".format(Username))
        if UsernameCheck == 'Y' or UsernameCheck == 'y':
            checks1 = True
        else:
            checks1 = False
    
    # while checks2 == False:    
    #     Password = input("Make a Password: ")  
    #     for i in range(len(Password)):
    #         if Password[i] in allowed:
    #             PasswordVerify = input("Please verify your Password: ")
    #             if PasswordVerify == Password:
    #                 time.sleep(2)    ############################ Add Username and Password to data base ##########
    #                 print("You have succesfully made a username and password ")


Maincode = Master_Login_SignUP(chance3) 
#

