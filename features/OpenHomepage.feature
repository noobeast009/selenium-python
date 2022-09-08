Feature: Validate the Home Page

Background:
    Given Launch the browser
    When Open the https://www.saucedemo.com/

Scenario: Validate Login module
    Then Run the whole login procedure with "standard_user"as username and "secret_sauce" as password

Scenario: Validate HomePage logo
    Then Run the whole login procedure with "standard_user"as username and "secret_sauce" as password
    Then Verify SwagLabs homepage logo

Scenario: Verify user can add item to cart
    Then Run the whole login procedure with "standard_user"as username and "secret_sauce" as password
    Then Click on Add To Cart button for Sauce Lab Backpack
    Then Click on Cart button
    Then Verify Sauce Lab Backpack had been added to cart

Scenario: Verify user can add item to cart
    Then Run the whole login procedure with "standard_user"as username and "secret_sauce" as password
    Then Click on Add To Cart button for Sauce Lab Backpack
    Then Click on Cart button
    Then Click on Checkout
    Then Provide the First Name "QA"
    Then Provide the Last Name "Test"
    Then Provide the Postal Code "45301"
    Then Click on Continue
    Then Click on Finish