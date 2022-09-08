from selenium.webdriver.common.by import By

from pages.BasePage import BasePage

class ListingPageElement(BasePage):
    swagLabs_logo_xpath = (By.XPATH, "(//div[@class='app_logo'])[1]")
    AddToCart = (By.ID, "add-to-cart-sauce-labs-backpack")
    CartButton = (By.XPATH, "(//a[@class='shopping_cart_link'])[1]")
    BagPackAdded = (By.XPATH, "(//div[@class='inventory_item_name'])[1]")
    CheckoutButton = (By.XPATH, "(//button[normalize-space()='Checkout'])[1]")
    FirstName = (By.XPATH, "(//input[@placeholder='First Name'])[1]")
    LastName = (By.XPATH, "(//input[@placeholder='Last Name'])[1]")
    PostalCode = (By.XPATH, "(//input[@id='postal-code'])[1]")
    ContinueButton = (By.XPATH, "(//input[@id='continue'])[1]")
    FinishButton = (By.XPATH, "(//button[normalize-space()='Finish'])[1]")