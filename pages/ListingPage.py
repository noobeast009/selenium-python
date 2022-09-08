import os

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from Elements.ListingPageElement import ListingPageElement

class ListingPage(ListingPageElement):
    
    def __init__(self, driver):
        super().__init__(driver)
        
    def verify_logo_homepage(self):
        self.assert_equal(self.verify_element_display(self.swagLabs_logo_xpath),True,"Cannot Find Logo")
        self.wait(6)
        
    def click_add_to_cart(self):
        self.wait(2)
        self.click_element(self.AddToCart)
        
    def click_cart_button(self):
        self.wait(2)
        self.click_element(self.CartButton)

    def click_checkout_button(self):
        self.wait(2)
        self.click_element(self.CheckoutButton)
        
    def verify_item_added(self):
        self.wait(2)
        self.assert_equal(self.verify_element_display(self.BagPackAdded),True,"Cannot Find Logo")
        self.wait(6)
        
    def enter_first_name(self,value):
        self.input_element(self.FirstName,value)
        
    def enter_last_name(self,value):
        self.input_element(self.LastName,value)
        
    def enter_postal_code(self,value):
        self.input_element(self.PostalCode,value)
        
    def click_continue_button(self):
        self.wait(2)
        self.click_element(self.ContinueButton)

    def click_finish_button(self):
        self.wait(2)
        self.click_element(self.FinishButton)
        