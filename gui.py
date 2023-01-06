'''
    This file is intended to hold all code to handle the GUI
'''
import instagram_follower_bot # imports the file with the bot code

# modules below are used for the GUI
import tkinter
from tkinter import *

# module below is used to get check login info before executing bot
import requests

class GUI:
    def runGUI(self):
        # Created a class object
        myBot = None

        #this is the part of the code that initializes the GUI
        main=tkinter.Tk()
        main.geometry('400x400') # set the size of the window
        main.title("Instagram Bot") # set the title

        # create user label and input windows on the page
        userLabel=Label(main,text="Username: ")
        self.usernameInput = Entry(main)
        passwordLabel=Label(main,text="Password: ")
        self.passwordInput = Entry(main)
        
        # place the label and input windows in the correct places
        userLabel.place(relx=.3,rely=.4)
        self.usernameInput.place(relx=.5,rely=.4)
        passwordLabel.place(relx=.3,rely=.6)
        self.passwordInput.place(relx=.5,rely=.6)
        

        # create the button to run the command and place it in the correct place
        getUserInputsButton=Button(main,text="Click to find unfollowers", command=self.startBot)
        getUserInputsButton.place(relx=.4,rely=.8)

        # loop the main method
        main.mainloop()

    #method to get the password and the username
    def startBot(self):
        # get the username and password that was typed in the gui
        username=self.usernameInput.get()
        password=self.passwordInput.get()

        # loop until the login can be validated

        # as long as the above loop ends, then we can pass the valid password and username to the instagram page
        myBot=instagram_follower_bot.InstaBot(username,password)
        myBot.getUnfollowers()

# execute the gui
guiInstance = GUI()
guiInstance.runGUI()
