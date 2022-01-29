from atexit import register
from tkinter import *
from tkinter import font
from turtle import color
import string
from numpy import column_stack
import solver

# import Login_and_Sign_Up_System

# class Login_Sign_UP:
#     def __init__(self) -> None:
#         self.application = Tk()
#         self.application.title("Login or Register")
#         self.application.geometry("400x320")
#         self.Label = Label(self.application, text="Choose Login or Register", color="white", bg="black", width=400, height=2, font=("Ariel", 13)).pack()
#         self.Button = Button(self.application, text="Login", command=Login())

#     def run(self):
#         self.application.mainloop()
   
#     def login():
#         login = Login_and_Sign_Up_System.Master_Login_SignUp.Login()
#         login.run()
    
#     def register(self):
#         register = Login_and_Sign_Up_System.Master_Login_SignUp.SignUp()
#         register.run()
# # def choice_screen():

# def main_screen():
#     global screen

#     screen = Tk()
#     screen.geometry("300x250")
#     screen.title("Notes")
#     Label(text = "Notes", bg = "grey", width="300", font = ("Calabri", 13)).pack()
#     Button(text="Login", width="30", height=2, command=login).pack()
#     Label(text="").pack()
#     Button(text="Register", width="30", height=2, command = register).pack()
#     screen.mainloop()

# main_screen() 

#     choice_screen = Tk()   # create a GUI window 
#     choice_screen.geometry("300x250") # set the configuration of GUI window 
#     choice_screen.title("Account Login") # set the title of GUI window
 
#     # create a Form label 
#     Label(text="Choose Login Or Register", bg="blue", width="300", height="2", font=("Ariel", 13)).pack() 
#     Label(text="").pack() 
    
#     # create Login Button 
#     Button(text="Login", height="2", width="30").pack() 
#     Label(text="").pack() 
    
#     # create a register button
#     Button(text="Register", height="2", width="30").pack()
    
#     choice_screen.mainloop() # start the GUI
    
# choice_screen() # call the main_account_screen() function




def solving():
    if __name__ == "__main__":
        window = Tk()
        window.title("Rubik Cube Solver")
        #window.geometry("1366x768")
        solver.main(window)
    
def validateinput():
    Usercharacters = string.ascii_letters + string.digits + '!#£$%&=?@'
    Passcharacters = string.ascii_letters + string.digits + '!"#$%&()*+/<=>?@'
    allowed_characters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                        '1','2','3','4','5','6','7','8','9','0','(',')','$','%','_','/']
    usernameStr = str(username.get())
    passwordStr = str(password.get())
    if len(usernameStr) > 3 and len(usernameStr) < 15 and any(x not in Usercharacters for x in usernameStr):
        if len(passwordStr) > 5 and len(passwordStr) < 24 and any(x not in Passcharacters for x in passwordStr):
            ###
            """Put into a json file"""
            ###
            solving()
        else:
            pass
    else:
        pass

def register():
    global username, password
    register = Toplevel(root)
    register.title("Register")
    register.geometry("400x320")

    username = StringVar()
    password = StringVar()

    Userlabel1 = Label(register, text="Enter a Username")
    UserEntry1 = Entry(register, textvariable = username)
    PassLabel1 = Label(register, text = "Enter Password")
    PassEntry1 = Entry(register, textvariable = password, show="*")
    SubBtn = Button(register, text="Submit", command=solving)

    Userlabel1.grid(row = 0, column = 0)
    UserEntry1.grid(row = 0, column = 1)
    PassLabel1.grid(row = 1, column = 0)
    PassEntry1.grid(row = 1, column = 1)
    SubBtn.grid(row = 2, column = 1)

def login():
    global username, password, login
    root.destroy()
    login = Toplevel(root)
    login.title("login")
    login.geometry("400x320")

    username = StringVar()
    password = StringVar()

    Userlabel1 = Label(login, text="Enter a Username")
    UserEntry1 = Entry(login, textvariable = username)
    PassLabel1 = Label(login, text = "Enter Password")
    PassEntry1 = Entry(login, textvariable = password, show="*")
    SubBtn = Button(login, text="Submit", command=solving)

    Userlabel1.grid(row = 0, column = 0)
    UserEntry1.grid(row = 0, column = 1)
    PassLabel1.grid(row = 1, column = 0)
    PassEntry1.grid(row = 1, column = 1)
    SubBtn.grid(row = 2, column = 1)

def main_screen():
    global root, login, register
    root = Tk()
    root.geometry("300x250")
    root.title("Choose")
    Label(root, text = "Chose Login or Register", bg = "grey", width="300", font = ("Calabri", 13)).pack()
    Button(root, text="Login", width="30", height=2, command = login).pack()
    Label(root, text="").pack()
    Button(root, text="Register", width="30", height=2, command = register).pack()
    root.mainloop()
main_screen()