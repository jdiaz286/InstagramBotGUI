from selenium import webdriver
from time import sleep

class InstaBot:
    # init method acts as login
    def __init__(self,un,pw):
        # Open new Firefox window
        self.driver=webdriver.Firefox()

        self.un = un

        # open up instagram on the firefox window
        self.driver.get("https://www.instagram.com/")
        sleep(2)

        #fill in username and password 
        self.driver.find_element("xpath", "//input[@name=\"username\"]").send_keys(un)    
        self.driver.find_element("xpath","//input[@name=\"password\"]").send_keys(pw)

        #click login button and wait 4 seconds
        self.driver.find_element("xpath",'//button[@type="submit"]').click()
        sleep(4)

        #ignore button to save password and wait 2 seconds
        self.driver.find_element("xpath","//button[contains(text(), 'Not Now')]").click()
        sleep(2)

        #ignore button to send notifications and wait 2 seconds
        self.driver.find_element("xpath","//button[contains(text(), 'Not Now')]").click()
        sleep(3)

    #Function that compares the people you follow to the people that follow you
    def getUnfollowers(self):
        sleep(3)
        #Click on your instagram image page
        self.driver.find_element("xpath","//a[contains(@href,'/{}')]".format(self.un)).click()
        sleep(3)

        #Click on the "following" section of your page
        self.driver.find_element("xpath","//a[contains(@href,'/{}/following')]".format(self.un)).click()
        sleep(3)
        
        self.driver.close()

        #Call in function _get_names() to save the names of all people you are following
        following = self._get_names()
        sleep(2)

        #Click on the "followers" section of your page
        self.driver.find_element("xpath","//a[contains(@href,'/followers')]").click()

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
        #/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]
        dialog_window = self.driver.find_element("xpath","/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", dialog_window)

        #self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

        sleep(2)
        #variable that saves the scroll bar 
        scroll_box = self.driver.find_element("xpath","/html/body/div[4]")
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
        self.driver.find_element("xpath","/html/body/div[4]/div/div/div[1]/div/div[2]/button").click()

        # return the array of names as a list
        return names



