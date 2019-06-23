from selenium import webdriver
import os
import time

class InstagramBot :

    def __init__(self,username,password) :
        self.username = username
        self.password = password

        self.driver = webdriver.Chrome('./chromedriver.exe')

        self.login()

    def login(self) :
        self.driver.get('https://www.instagram.com/accounts/login/')

        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)

        self.driver.find_elements_by_xpath("//div[contains(text(), 'Log In')]")[0]


if __name__ == '__main__' :
    ig_bot = InstagramBot('temp_username','temp_password')

    print(ig_bot.username)
