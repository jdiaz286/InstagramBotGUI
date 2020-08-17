from selenium import webdriver
from time import sleep
import tkinter
from tkinter import *
#FIGURE OUT WHY IT SAVES PEOPLE AND HASHTAGS!!!!

class InstaBot:
    #execute program here
    def __init__(self,un,pw):
        #Open chrome webpage
        self.driver=webdriver.Chrome()
        #save username 
        self.un=un
        #open up instagram
        self.driver.get("https://www.instagram.com/")
        sleep(2)
        #fill in username
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(un) 
        #fill in password
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        #click login button
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)
        #ignore button to save password
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(2)
        #ignore button to send notifications
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(2)

    #Function that compares the people you follow to the people that follow you
    def getUnfollowers(self):
        #Click on your instagram image page
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.un))\
            .click()
        sleep(2)
        #Click on the "following" section of your page
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        #Call in function _get_names() to save the names of all people you are following
        following = self._get_names()
        #Click on the "followers" section of your page
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()
        #Call in function _get_names() to save the names of all people you have as followers
        followers = self._get_names()
        #only saves the usernames of people that you are following but that don't follow you back
        not_following_back = [user for user in following if user not in followers]
        #print out the names of the people not following you
        print(not_following_back)

    #Function to get the names of a list
    def _get_names(self):
        sleep(2)
        #scroll down to the bottom of the page on the browser
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        sleep(2)
        #variable that saves the scroll bar 
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]")
        #variables to track the current height of the 
        last_ht, ht = 0, 1
        #loop that occurs until the scroll bar has reached the bottom
        while last_ht != ht:
            last_ht = ht
            sleep(1)
        #gets the links of each person/box   
        links = scroll_box.find_elements_by_tag_name('a')
        #variable to save each name in each box
        names = [name.text for name in links if name.text != '']
        # close button
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button")\
            .click()
        return names

#method to get the password and the username
def startBot():
    username=usernameInput.get()
    password=passwordInput.get()
    myBot=InstaBot(username,password)
    myBot.getUnfollowers()

#this is the part of the code that initializes the GUI
main=tkinter.Tk()
main.title("Instagram Bot")
main.geometry('400x400')
userLabel=Label(main,text="Username: ")
userLabel.place(relx=.3,rely=.4)
usernameInput = Entry(main)
usernameInput.place(relx=.5,rely=.4)
passwordLabel=Label(main,text="Password: ")
passwordLabel.place(relx=.3,rely=.6)
passwordInput = Entry(main)
passwordInput.place(relx=.5,rely=.6)
getUserInputsButton=Button(main,text="Click to find unfollowers", command=startBot)
getUserInputsButton.place(relx=.4,rely=.8)
main.mainloop()

