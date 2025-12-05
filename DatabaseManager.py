# IMPORT LIBRARIES

import sqlite3

class DatabaseManager:
    def __init__(self):
        self.databaseName = "NEADatabase.db"

    def CreateAccount(self, firstName, lastName, email, password):
        error = False
        patternForEmail = r'[^@]+@[^@]+\.[^@]+'






























def CreateAccount(self,firstname,lastname,email,password):
        
        erroroccured = False
        patternforemail = r'[^@]+@[^@]+\.[^@]+'
        if re.match(patternforemail,email) == None:
            self.MakeErrorMessage("Email is not valid")
            erroroccured = True
        
        
        highestuserid = self.controller.GetHighestUserID()
        if highestuserid == None:
            highestuserid = 1
        
        # encrypt password
        encryptedpass = self.controller.EncryptData(password)
        
        # final checks
        
        if erroroccured == False:
            database = sqlite3.connect("NEADatabase.db")
            cursor = database.cursor()
            cursor.execute("INSERT INTO AccountInformation (EmailAddress, FirstName, LastName, Password) VALUES (?, ?, ?, ?)", (f"{email}", f"{firstname}",f"{lastname}",f"{encryptedpass}"))
            database.commit()
            database.close()
            if hasattr(self,"errormessage"):
                self.errormessage.destroy()
            
            self.successmessage = ctk.CTkLabel(self, text = "Account was created!", font = ('Arial',15), text_color = "green")
            self.successmessage.pack(pady = 5)
            
            self.after(3000, self.successmessage.destroy)




    def CheckLoginConditions(self,email,password):
        database = sqlite3.connect("NEADatabase.db")
        cursor = database.cursor()
        cursor.execute("SELECT * FROM AccountInformation WHERE EmailAddress=?", (email,))
        if cursor.fetchone() == None:
            self.MakeErrorMessage("Email is not found.")
        else:
            cursor.execute("SELECT Password FROM AccountInformation where EmailAddress = ?", (email,))
            dbpass = cursor.fetchone()[0]
            issamepass = self.controller.CheckEncryptedData(dbpass,password)
            if issamepass == True:
                if hasattr(self,"errormessage"):
                    self.errormessage.destroy()
                
                self.controller.ShowPage(MainMenu)
                self.controller.HidePage(LoginPage)
                # probably add more stuff later
            else:
                self.MakeErrorMessage("Password is incorrect.")
                
        database.close()