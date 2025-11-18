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

        self.PageManager = PageManager(self.guiroot)

        self.TestPage = self.PageManager.AddPage("TestPage",TestPage)
        self.TestPage.pack(fill="both", expand=True)

        self.guiroot.mainloop()

class TestPage(ctk.CTkFrame):
    def __init__(self, maingui):
        super().__init__(maingui)

        # Put elements of GUI here
        
        self.text = ctk.CTkLabel(self, text = "Test text", font = ('Arial', 40))
        self.text.pack(fill="both", expand=True)


NEAGui()