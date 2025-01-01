import pytest
from selenium import webdriver
from page.login_page import Login_page

@pytest.fixture(scope="module")
def browser_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_steps(browser_driver):
    driver = browser_driver
    login_page = Login_page(driver)
    
    # Navigate to login page
    login_page.navigate_to(login_page.login_url)
    
    # Perform login with incorrect credentials
    login_page.login_as("standard_user", "secret_sauc")

    # Assert if the error alert is displayed
    login_page.get_wait(login_page.login_error_alert, 5).is_displayed()

    assert login_page.get_text(login_page.login_error_msg)=='Epic sadface: Username and password do not match any user in this service', "Error message missing!"
