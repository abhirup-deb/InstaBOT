from selenium import webdriver
import os
import time

class InstagramBot :

    def __init__(self,username,password) :
        """
        Initializes an instance of the InstagramBot class,
        Calls the Log in method to authenticate a user with IG.abs(x)
        Args:
            username:str: The Instagram username for a user
            password:str: The Instagram password  for a username

        Attributes:
            driver:Selenium.webdriver.Chrome: The Chromedriver that is used to automate browser actions
        """

        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'
        self.driver = webdriver.Chrome('./chromedriver.exe')

        self.login()


    def login(self) :
        self.driver.get('{}/accounts/login/'.format(self.base_url))

        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_elements_by_xpath("//div[contains(text(), 'Log In')]")[0]


    def nav_user(self,user):
        self.driver.get('{}/{}/'.format(self.base_url,user))



if __name__ == '__main__' :
    ig_bot = InstagramBot('temp_username','temp_password')
    ig_bot.nav_user('abhirup_deb')
    
