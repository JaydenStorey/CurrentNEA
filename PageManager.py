# IMPORT LIBRARIES

import customtkinter as ctk

class PageManager:
    def __init__(self, maingui):
        self.currentpage = 0 # placeholder
        self.pages = {}
        self.maingui = maingui

    
    def GetPage(self,pagename):
        try:
            return self.pages.get(pagename)
        except:
            print(pagename,"page was not found in pages")
            return None

    def AddPage(self, pagename, pageclass):
        # defines a page as the page class (each page will be a class)
        page = pageclass(self.maingui)
        self.pages[pagename] = page # adds the page in the dictionary under index of the page name
        return page
    