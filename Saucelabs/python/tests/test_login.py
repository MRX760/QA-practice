import pytest
# from tests.test_cases import (incorrect_password_login, incorrect_username_login, 
#                               no_username_login, no_password_login, correct_credential_login)
from selenium import webdriver
from page.login_page import Login_page
from page.inventory_page import Inventory_page
from allure import (severity, severity_level, 
                    feature, story,
                    title, step)
import allure

@pytest.fixture(autouse=True)
def set_allure_labels():
    allure.dynamic.feature("Login")
    allure.dynamic.severity(allure.severity_level.BLOCKER)
    allure.dynamic.suite("Validate Login Functionality")

@pytest.fixture(scope="session")
def browser_driver():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920x1080')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def set_up(browser_driver):
    """Precondition."""
    base_url = 'https://www.saucedemo.com/'
    browser_driver.get(base_url)
    yield browser_driver


@step("user try login with incorrect password")
@story("User will failed login to website if credentials are incorrect")
@title("[Negative] Verify user can't login using wrong password")
def test_login_incorrect_password(set_up):
    driver = set_up
    login_page = Login_page(driver)
        
    # Perform login with incorrect credentials
    login_page.login_as("standard_user", "secret_sauc")

    # Assert if the error alert is displayed
    login_page.get_wait(login_page.login_error_alert, 5).is_displayed()

    assert login_page.get_text(login_page.login_error_msg)=='Epic sadface: Username and password do not match any user in this service', "Error message missing!"
    login_page.make_pass_visible()
    login_page.take_page_screenshot("Error message")

@step("user try login with non-existing usernmae")
@story("User will failed login to website if credentials are incorrect")
@title("[Negative] Verify user can't login using non-exist username")
def test_login_incorrect_username(set_up):
    driver = set_up
    login_page = Login_page(driver)

    # Perform login with incorrect credentials
    login_page.login_as("std", "secret_sauce")

    # Assert if the error alert is displayed
    login_page.get_wait(login_page.login_error_alert, 5).is_displayed()

    assert login_page.get_text(login_page.login_error_msg)=='Epic sadface: Username and password do not match any user in this service', "Error message missing!"
    login_page.make_pass_visible()
    login_page.take_page_screenshot("Error message")

@step("user try login with no password")
@story("User will failed login to website if credentials are incorrect")
@title("[Negative] Verify user can't login when password is empty")
def test_login_no_password(set_up):
    driver = set_up
    login_page = Login_page(driver)
        
    # Perform login with incorrect credentials
    login_page.login_as("standard_user", "")

    # Assert if the error alert is displayed
    login_page.get_wait(login_page.login_error_alert, 5).is_displayed()

    assert login_page.get_text(login_page.login_error_msg)=='Epic sadface: Password is required', "Error message missing!"
    login_page.make_pass_visible()
    login_page.take_page_screenshot("Credentials")

@step("user try login with no username")
@story("User will failed login to website if credentials are incorrect")
@title("[Negative] Verify user can't login when username is empty")
def test_login_no_username(set_up):
    driver = set_up
    login_page = Login_page(driver)
    
    # Perform login with incorrect credentials
    login_page.login_as("", "secret_sauce")

    # Assert if the error alert is displayed
    login_page.get_wait(login_page.login_error_alert, 5).is_displayed()

    assert login_page.get_text(login_page.login_error_msg)=='Epic sadface: Username is required', "Error message missing!"
    login_page.make_pass_visible()
    login_page.take_page_screenshot("Credentials")

@step("user try login without credentials")
@story("User will failed login to website if credentials are incorrect")
@title("[Negative] Verify user can't login when credentials is empty")
def test_login_no_credentials(set_up):
    driver = set_up
    login_page = Login_page(driver)
   
    # Perform login with incorrect credentials
    login_page.login_as("", "")

    # Assert if the error alert is displayed
    login_page.get_wait(login_page.login_error_alert, 5).is_displayed()

    assert login_page.get_text(login_page.login_error_msg)=='Epic sadface: Username is required', "Error message missing!"
    login_page.take_page_screenshot("Credentials")

@step("user try login with correct credentials")
@story("User can login to website using correct credentials")
@title("[Positive] Verify user can login on saucelabs using correct credentials")
def test_login_correct_credentials(set_up):
    #instance initialization
    driver = set_up
    login_page = Login_page(driver)
    inventory_page = Inventory_page(driver)
        
    # Perform login with correct credentials
    # login_page.login_as("standard_user", "secret_sauce")
    login_page.insert_credentials("standard_user", "secret_sauce")
    
    login_page.make_pass_visible()
    login_page.take_page_screenshot("Credentials")
    
    login_page.click_btn(login_page.login_button)

    assert inventory_page.get_wait(inventory_page.title, 5).is_displayed(), inventory_page.take_page_screenshot("failed to locate element")
    inventory_page.take_page_screenshot("dashboard/item list")
