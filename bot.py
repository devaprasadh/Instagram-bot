from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import time

class InstagramBot:

    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'
        self.driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
        self.login()

    def login(self):
        self.driver.get('https://www.instagram.com')
        time.sleep(3)
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_elements_by_xpath("//div[contains(text(),'Log In')]")[0].click()

    def nav_user(self,user):
        
        self.driver.get('{}/{}/'.format(self.base_url,user))

    def follow_user(self,user):
        self.nav_user(user)
        follow_button = self.driver.find_elements_by_xpath("//button[contains(text(),'Follow')]")[0]
        follow_button.click()


    def like_posts(self, user, n_posts, like=True):
        """
        Likes a number of a users latest posts, specified by n_posts.
        Args:
            user:str: User whose posts to like or unlike
            n_posts:int: Number of most recent posts to like or unlike
            like:bool: If True, likes recent posts, else if False, unlikes recent posts
        TODO: Currently maxes out around 15.
        """

        action = 'Like' if like else 'Unlike'

        self.nav_user(user)

        imgs = []
        imgs.extend(self.driver.find_elements_by_class_name('_9AhH0'))
        time.sleep(1)
        for img in imgs[:n_posts]:
            img.click() 
            time.sleep(2) 
            try:
                self.driver.find_element_by_xpath("//*[@aria-label='{}']".format(action)).click()
            except Exception as e:
                print(e)

            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@aria-label='Close']").click()
            time.sleep(4)
    

    def comment_posts(self,text,n_posts,user):

        self.nav_user(user)

        imgs = []
        imgs.extend(self.driver.find_elements_by_class_name('_9AhH0'))
        time.sleep(2)

        for img in imgs[:n_posts]:
            img.click()
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'Ypffh')))
            comment_input = self.driver.find_element_by_class_name('Ypffh')
            comment_input.click()
            comment_button = self.driver.find_element_by_xpath("//*[@aria-label='Add a comment…']")
            time.sleep(2)
            comment_button.send_keys(text)
            comment_button.send_keys(Keys.RETURN)
            print('commented successfully')
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@aria-label='Close']").click()
            time.sleep(4)

    def quit_browser(self):

        self.driver.quit()
                       
    
        

if __name__ == '__main__':
    #ig_bot = InstagramBot()
    #time.sleep(4)
    
    #ig_bot.like_posts()
    
    

