import pytest
from selenium import webdriver
from page.login_page import Login_page
from page.inventory_page import Inventory_page

@pytest.fixture(scope="module")
def browser_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_steps(browser_driver):
    #instance initialization
    driver = browser_driver
    login_page = Login_page(driver)
    inventory_page = Inventory_page(driver)
    
    # Navigate to login page
    login_page.navigate_to(login_page.login_url)
    
    # Perform login with correct credentials
    login_page.login_as("standard_user", "secret_sauce")
    
    assert inventory_page.get_wait(inventory_page.title, 5).is_displayed(), "Login Failed!"
