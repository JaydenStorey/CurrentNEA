# IMPORT LIBRARIES

import customtkinter as ctk

class PageManager:
    def __init__(self, rootclass, maingui, rootframe):
        self.currentpage = 0 # placeholder
        self.lastpage = 0 # placeholder
        self.pages = {}
        self.rootclass = rootclass
        self.maingui = maingui
        self.rootframe = rootframe

    
    def GetPage(self,pagename):
        try:
            return self.pages.get(pagename)
        except:
            print(pagename,"page was not found in pages")
            return None

    def AddPage(self, pagename, pageclass):
        # defines a page as the page class (each page will be a class)
        page = pageclass(self.rootclass, self.maingui, self.rootframe) ## added passing the rootframe
        self.pages[pagename] = page # adds the page in the dictionary under index of the page name
        return page

    def GetLastPage(self):
        try:
            return self.pages[self.lastpage]
        except:
            print("Last page was not found.")
            return None

    def ShowPage(self, pagename):
        page = self.GetPage(pagename)

        # Remove all pages on screen
        for storedpage in self.pages.values():
            if hasattr(self, 'startframe'):
                storedpage.startframe.pack_forget()
                print("Hid",storedpage)

        if page:
            page.pack(fill="both", expand=True)
        else:
            print("Page was not found")
            
