# START OF NEA PROJECT

# IMPORT LIBRARIES

import customtkinter as ctk
from PageManager import PageManager
from DatabaseManager import DatabaseManager

# from FILE import CLASS

# Set up GUI

class NEAGui:
    def __init__(self):
        self.guiroot = ctk.CTk()
        self.windowheight = 480
        self.windowwidth = 720
        self.guiroot.geometry(f"{self.windowwidth}x{self.windowheight}")

        self.PageManager = PageManager(self, self.guiroot)

        # Add all pages used
        self.StartPage = self.PageManager.AddPage("StartPage",StartPage)
        self.LoginPage = self.PageManager.AddPage("LoginPage",LoginPage)
        self.RegisterPage = self.PageManager.AddPage("RegisterPage",RegisterPage)

        # Show StartPage

        self.PageManager.ShowPage("StartPage")

        self.guiroot.mainloop()

# Functions of UI #

def GoToLastPage(PageManager):
    # back button
    if PageManager == None:
        print("PageManager was not given in the function call for GoToLastPage")
        return None
    
    LastPage = PageManager.GetLastPageName() # Will give the page class name of the last page
    PageManager.ShowPage(LastPage)



# Create account and login functions #

def CreateAccount(FirstName,LastName,Email,Password):
    HighestUserID = DatabaseManager.GetHighestUserID()
    if HighestUserID == None:
        HighestUserID = 1



def CheckLogin(Email,EncryptedPassword):
    


class StartPage(ctk.CTkFrame):
    def __init__(self,rootclass,maingui):
        super().__init__(maingui)

        # Elements of GUI

        self.title = ctk.CTkLabel(self, text = "Hot Stuff", font = ('Arial', 50), anchor = "center")
        self.title.pack(anchor = "n")

        self.registerbutton = ctk.CTkButton(self, text = "Register", command = lambda: rootclass.PageManager.ShowPage("RegisterPage"))
        self.registerbutton.pack(pady = 5)

        self.loginbutton = ctk.CTkButton(self, text = "Login", command = lambda: rootclass.PageManager.ShowPage("LoginPage"))
        self.loginbutton.pack(pady = 5)

class LoginPage(ctk.CTkFrame):
    def __init__(self,rootclass,maingui):
        super().__init__(maingui)

        # Elements of GUI

        self.title = ctk.CTkLabel(self, text = "Login Page", font = ('Arial', 50), anchor = "center")
        self.title.pack(anchor = "n")

        # email entry
        
        self.emailentrylabel = ctk.CTkLabel(self, text = "Enter Email Address", font = ('Arial', 15))
        self.emailentrylabel.pack(pady = 2)
        
        self.emailentry = ctk.CTkEntry(self, font = ('Arial', 15), width = 250, corner_radius = 7)
        self.emailentry.pack(pady = 2)
        
        # password entry
        
        self.passwordentrylabel = ctk.CTkLabel(self, text = "Enter Password", font = ('Arial', 15))
        self.passwordentrylabel.pack(pady = 2)

        self.passwordentry = ctk.CTkEntry(self, font = ('Arial', 15), width = 250, show = "*", corner_radius = 7)
        self.passwordentry.pack(pady = 2)
        
        # login button
        
        self.loginbutton = ctk.CTkButton(self, font = ('Arial', 30), width = 5, text = "Login", fg_color = "red", command = lambda: CheckLogin())
        self.loginbutton.pack(pady = 10)

        self.backbutton = ctk.CTkButton(self, text = "Back", fg_color = "red", width = 3, command = lambda: GoToLastPage(rootclass.PageManager))
        self.backbutton.pack(pady = 5)

class RegisterPage(ctk.CTkFrame):
    def __init__(self,rootclass,maingui):
        super().__init__(maingui)

        # Elements of GUI

        self.title = ctk.CTkLabel(self, text = "Register Page", font = ('Arial', 50), anchor = "center")
        self.title.pack(anchor = "n")

        self.enterfirstnamelabel = ctk.CTkLabel(self, text = "Enter your first name", font = ('Arial', 15))
        self.enterfirstnamelabel.pack(pady = 2)
        
        self.enterfirstnameentry = ctk.CTkEntry(self, font = ('Arial', 15), width = 250, corner_radius = 7)
        self.enterfirstnameentry.pack(pady = 2)
        
        self.enterlastnamelabel = ctk.CTkLabel(self, text = "Enter your last name", font = ('Arial', 15))
        self.enterlastnamelabel.pack(pady = 2)
        
        self.enterlastnameentry = ctk.CTkEntry(self, font = ('Arial', 15), width = 250, corner_radius = 7)
        self.enterlastnameentry.pack(pady = 2)
        
        # email entry
        
        self.emailentrylabel = ctk.CTkLabel(self, text = "Enter Email Address", font = ('Arial', 15))
        self.emailentrylabel.pack(pady = 2)
        
        self.emailentry = ctk.CTkEntry(self, font = ('Arial', 15), width = 250, corner_radius = 7)
        self.emailentry.pack(pady = 2)
        
        # password entry
        
        self.passwordentrylabel = ctk.CTkLabel(self, text = "Enter Password", font = ('Arial', 15))
        self.passwordentrylabel.pack(pady = 2)

        self.passwordentry = ctk.CTkEntry(self, font = ('Arial', 15), width = 250, corner_radius = 7)
        self.passwordentry.pack(pady = 2)
        
        # sign up button
        
        self.createaccountbutton = ctk.CTkButton(self, font = ('Arial', 30), width = 5, text = "Create Account", fg_color = "red", command = lambda: CreateAccount())
        self.createaccountbutton.pack(pady = 10)

        self.backbutton = ctk.CTkButton(self, text = "Back", fg_color = "red", width = 3, command = lambda: GoToLastPage(rootclass.PageManager))
        self.backbutton.pack(pady = 10)



NEAGui()
