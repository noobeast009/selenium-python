import os

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Elements.HomePageElement import HomePageElement
from selenium.webdriver.support.select import Select

class HomePage(HomePageElement):

    def __init__(self, driver):
        super().__init__(driver)
        
    def click_on_login(self):
        self.wait(2)
        self.click_element(self.Login)