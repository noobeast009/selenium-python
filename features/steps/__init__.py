import os
import time
from behave import *
from constants.config import TestData
from pages.HomePage import HomePage
from pages.ListingPage import ListingPage
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

@given(u'Launch the browser')
def launch_browser(context):
    if TestData.BROWSER == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=800,600")
        options.add_argument("--ignore-certificate-error")
        options.add_argument("--ignore-ssl-errors")
        options.add_argument("--incognito")
        options.add_argument("--disable-notifications")
        # options.add_argument("download.default_directory=C:\\Users\\786 Computers\\PycharmProjects\\E2E-Web\\TestData\\Downloaded_Files")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--disable-blink-features=AutomationControlled")
        if TestData.PLATFORM == 'local':
            context.driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
        #elif TestData.PLATFORM == 'docker':
        #    remote_url = os.getenv('SELENIUM_GRID_URL')
        #    # os.environ['DISPLAY'] = ':0'
        #    time.sleep(5)
        #    context.driver = webdriver.Remote(command_executor=f'http://{remote_url}/wd/hub',
        #    desired_capabilities = DesiredCapabilities.CHROME, options = options)
        #context.driver.maximize_window()
    elif TestData.BROWSER == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument("--disable-notifications")
        context.driver = webdriver.Firefox(service=FirefoxService(executable_path=GeckoDriverManager().install()))
        
@when(u'Open the https://www.saucedemo.com/')
def open_home_page(context):
    try:
        # url = context.config.userdata['url']
        # context.driver.get(url)
        context.driver.get(TestData.sauceDemo)
        
        context.HomePage = HomePage(context.driver)
        context.ListingPage = ListingPage(context.driver)
        time.sleep(2)
    except Exception as e:
        print(e)
        context.driver.close()
        assert False, "Test failed in SauceDemo"
