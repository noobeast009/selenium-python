from selenium.webdriver.common.by import By

from pages.BasePage import BasePage

class HomePageElement(BasePage):
    UserNameField = "(//input[@placeholder='Username'])[1]"
    PasswordField = "(//input[@placeholder='Password'])[1]"
    LoginButton = ("(//input[@value='Login'])[1]")
    swagLabs_logo_xpath = (By.XPATH, "(//div[@class='app_logo'])[1]")