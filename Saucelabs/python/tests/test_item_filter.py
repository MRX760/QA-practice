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

#precondition steps
from .test_login import test_login_correct_credentials as login

@pytest.fixture(autouse=True)
def set_allure_labels():
    allure.dynamic.feature("item-filter")
    allure.dynamic.severity(allure.severity_level.MINOR)
    allure.dynamic.suite("Validate item filter functionality")
    allure.dynamic.story("User can sort item based on alphabet sequence or price")

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
def redirect(browser_driver):
    """Precondition."""
    #redirect to login
    base_url = 'https://www.saucedemo.com/'
    browser_driver.get(base_url)
    yield browser_driver

@pytest.fixture(scope="session")
def user_login(redirect):
    """Precondition."""
    #login
    login(redirect)
    yield redirect

@step("User sort item from A to Z (item title)")
@title("[Positive] Verify user can sort item from A to Z")
def test_alpha_ascending(user_login):
    driver = user_login
    item_page = Inventory_page(driver)
    
    item_page.click_btn(item_page.item_sort)
    item_page.take_page_screenshot("clicking sort button")

    item_page.select(item_page.item_sort, "Name (A to Z)")
    item_page.take_page_screenshot("clicking sort alphabet ascending")
    
    descriptions = item_page.get_item_description()

    item_names = [item['name'] for item in descriptions]

    assert item_names == sorted(item_names)

step("User sort item from Z to A (item title)")
@title("[Positive] Verify user can sort item from Z to A")
def test_alpha_descending(user_login):
    driver = user_login
    item_page = Inventory_page(driver)
    
    item_page.click_btn(item_page.item_sort)
    item_page.take_page_screenshot("clicking sort button")

    item_page.select(item_page.item_sort, "Name (Z to A)")
    item_page.take_page_screenshot("clicking sort alphabet descending")
    
    descriptions = item_page.get_item_description()

    item_names = [item['name'] for item in descriptions]

    assert item_names == sorted(item_names, reverse=True)

step("User sort item from lowest to biggest price")
@title("[Positive] Verify user can sort item from lowest to highest price")
def test_price_descending(user_login):
    driver = user_login
    item_page = Inventory_page(driver)
    
    item_page.click_btn(item_page.item_sort)
    item_page.take_page_screenshot("clicking sort button")

    item_page.select(item_page.item_sort, "Price (low to high)")
    item_page.take_page_screenshot("clicking sort price ascending")
    
    descriptions = item_page.get_item_description()

    item_prices = [item['price'] for item in descriptions]
    sorted_prices = sorted(item_prices, key=lambda x: float(x[1:]))

    assert item_prices == sorted_prices, sorted_prices

step("User sort item from biggest to lowest price")
@title("[Positive] Verify user can sort item from highest to lowest price")
def test_price_ascending(user_login):
    driver = user_login
    item_page = Inventory_page(driver)
    
    item_page.click_btn(item_page.item_sort)
    item_page.take_page_screenshot("clicking sort button")

    item_page.select(item_page.item_sort, "Price (high to low)")
    item_page.take_page_screenshot("clicking sort price descending")
    
    descriptions = item_page.get_item_description()

    item_prices = [item['price'] for item in descriptions]
    sorted_prices = sorted(item_prices, key=lambda x: float(x[1:]), reverse=True)

    assert item_prices == sorted_prices, sorted_prices

    