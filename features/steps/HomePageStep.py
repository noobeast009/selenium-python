import time

from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from behave import *
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from Elements.HomePageElement import HomePageElement
from selenium.webdriver.common.by import By

@then(u'Run the whole login procedure with "{userName}"as username and "{pwd}" as password')
def step_impl(context, userName, pwd):
    try:
        time.sleep(10)
        context.HomePage = HomePageElement
        context.driver.find_element(By.XPATH, context.HomePage.UserNameField).send_keys(userName)
        context.driver.find_element(By.XPATH, context.HomePage.PasswordField).send_keys(pwd)
        context.driver.find_element(By.XPATH, context.HomePage.LoginButton).click()
        time.sleep(5)
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=(str(e) + "Test Failed Login module"),attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'Verify SwagLabs homepage logo')    
def logo_homepage(context):
        time.sleep(2)
        context.ListingPage.verify_logo_homepage()
        
@then(u'Click on Add To Cart button for Sauce Lab Backpack')    
def add_to_cart(context):
        time.sleep(2)
        context.ListingPage.click_add_to_cart()
        
@then(u'Click on Cart button')    
def cart_button(context):
        time.sleep(2)
        context.ListingPage.click_cart_button()
        
@then(u'Verify Sauce Lab Backpack had been added to cart')    
def item_added(context):
        time.sleep(2)
        context.ListingPage.verify_item_added()

@then(u'Click on Checkout')    
def checkout_button(context):
        time.sleep(2)
        context.ListingPage.click_checkout_button()
                
@then(u'Provide the First Name "{name}"')
def first_name(context, name):
    context.ListingPage.enter_first_name(name)
    
@then(u'Provide the Last Name "{name}"')
def last_name(context, name):
    context.ListingPage.enter_last_name(name)
    
@then(u'Provide the Postal Code "{name}"')
def postal_code(context, name):
    context.ListingPage.enter_postal_code(name)
    
@then(u'Click on Continue')    
def continue_button(context):
        time.sleep(2)
        context.ListingPage.click_continue_button()
    
@then(u'Click on Finish')    
def finish_button(context):
        time.sleep(2)
        context.ListingPage.click_finish_button()