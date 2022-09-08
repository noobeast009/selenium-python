### Python Selenium BDD Test Suite

### Project Setup

1. install the dependencies
   'pip install -r requirements.txt'

**To run the test with allure report**
'behave -f allure_behave.formatter:AllureFormatter -o allure/results ./features -D url=https://www.saucedemo.com/'

**To generate allure report**
'allure serve allure/results'