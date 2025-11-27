# START OF NEA PROJECT

# IMPORT LIBRARIES

import customtkinter as ctk
from PageManager import PageManager

# from FILE import CLASS

# Set up GUI

class NEAGui:
    def __init__(self):
        self.guiroot = ctk.CTk()
        self.windowheight = 480
        self.windowwidth = 720
        self.guiroot.geometry(f"{self.windowwidth}x{self.windowheight}")

        self.frame = ctk.CTkFrame(self.guiroot)
        self.frame.pack(fill="both", expand=True)

        self.PageManager = PageManager(self, self.guiroot, self.frame)

        # Add all pages used
        self.StartPage = self.PageManager.AddPage("StartPage",StartPage)
        self.LoginPage = self.PageManager.AddPage("LoginPage",LoginPage)

        # Show StartPage

        self.PageManager.ShowPage("StartPage")

        self.guiroot.mainloop()


class StartPage(ctk.CTkFrame):
    def __init__(self,rootclass,maingui,rootframe):
        super().__init__(maingui)

        # Elements of GUI
        self.startframe = ctk.CTkFrame(rootframe)
        self.startframe.pack(fill="both", expand=True)

        self.title = ctk.CTkLabel(self.startframe, text = "Hot Stuff", font = ('Arial', 50), anchor = "center")
        self.title.pack(anchor = "n")

        self.loginbutton = ctk.CTkButton(self.startframe, text = "Login", command = lambda: rootclass.PageManager.ShowPage("LoginPage"))
        self.loginbutton.pack(pady = 5)

class LoginPage(ctk.CTkFrame):
    def __init__(self,rootclass,maingui,rootframe):
        super().__init__(maingui)

        # Elements of GUI
        self.startframe = ctk.CTkFrame(rootframe)
        self.startframe.pack(fill="both", expand=True)

        self.title = ctk.CTkLabel(self.startframe, text = "Login Page", font = ('Arial', 50), anchor = "center")
        self.title.pack(anchor = "n")



NEAGui()
