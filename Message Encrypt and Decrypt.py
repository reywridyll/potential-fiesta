""" ©owner Rey
    Created -- 11/22/17 
    Version 1.1
    Application that encrypts and decrypts a message
"""

# import
from tkinter import *
from tkinter.ttk import *
import random
import string
#import end //

class messageEncrypter():
    """Encryter class:
            window >> Tk()
    """
    def __init__(self, window):
        """Gui constructor function"""
        #GLobal Vars // 
        global userEntry, userDrop
        #Gui Constructor starts here // 
        operatorChoices = ['Encrypt', 'Decrypt'] # Choices User can make
        self.greetingsWindow = Label(window, text="Enter the message below")
        self.greetingsWindow.grid(row=0, column=0,padx=125)
        self.userEntry = Entry(window, width=85)
        self.userDrop = Combobox(window, values=operatorChoices)
        self.userDrop.set('Encrypt')
        self.userDrop.grid(row=1, column=1, padx=10)
        self.userEntry.grid(row=1, column=0, pady=10, padx=10)
        self.enterButton = Button(window, text="Continue", command=self.runFunction)
        self.enterButton.grid(row=2,column=0, pady=10)

    def runFunction(self):
        """Runs main command line from user interface"""
        #GLobal Vars // 
        global userEntry, userDrop
        #Checks if user has entered text
        if len(self.userEntry.get()) != 0:
            #User check passed << Continue Encrypt // Decrypt >> //
            if self.userDrop.get() == 'Encrypt':
                result = self.encryptFunction(self.userEntry.get()) #Runs encrypt key function
                return result
            else:
                result = self.decryptFunction(self.userEntry.get()) #Runs decrypt key function
                return result
        #Check fails //
        else:
            self.greetingsWindow['text'] = "Error: No text detected!! "

    def encryptFunction(self, currentEntry):
        """Encrypts the user message for safe sending"""
        #GLobal Vars // 
        global userEntry, userDrop
        #Main Encrypt function <<Starts>> //
        newString = ''
        for i in currentEntry:
            generatedString = i + random.choice(string.ascii_letters)
            newString += generatedString
        #Encrypt Message Display // 
        self.greetingsWindow['text'] = "Your encryted code is:"
        self.userEntry.delete(0,END)
        self.userEntry.insert(0, newString)
    
    def decryptFunction(self, currentEntry):
        """Decrypts the user message"""
        #GLobal Vars //
        global userEntry, userDrop
        #Main Decrypt function <<Starts>> //
        n = 0
        newString = ''
        while n != len(currentEntry):
            i = currentEntry[n]
            if n%2 == 0:
                n += 1
                newString += i
            else:
                pass
                n += 1
        #Decrypt Message Display
        self.greetingsWindow['text'] = "Your decryted code is:"
        self.userEntry.delete(0,END) 
        self.userEntry.insert(0, newString)
        
#Main call code starts here
if __name__ == '__main__':
    """Main Call function of the class"""
    window = Tk() # using tkinter
    gui = messageEncrypter(window)
    window.mainloop()
