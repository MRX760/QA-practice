import pytest
# from tests.test_cases import (incorrect_password_login, incorrect_username_login, 
#                               no_username_login, no_password_login, correct_credential_login)
from selenium import webdriver
from selenium.webdriver.common.by import By

from page.item_desc_page import desc_page
from page.cart_page import Cart_page
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
    allure.dynamic.suite("Validate item cart functionality")
    allure.dynamic.story("User can add, remove, and see item details on cart")

@pytest.fixture(scope="function")
def browser_driver():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920x1080')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def redirect(browser_driver):
    """Precondition."""
    #redirect to login
    base_url = 'https://www.saucedemo.com/'
    browser_driver.get(base_url)
    yield browser_driver

@pytest.fixture(scope="function")
def user_login(redirect):
    """Precondition."""
    #login
    login(redirect)
    yield redirect

@step("User add item to cart")
@title("[Positive] Verify user can add item to cart")
@severity(allure.severity_level.BLOCKER)
def test_add_item(user_login):
    driver = user_login
    item_page = Inventory_page(driver)
    cart_page = Cart_page(driver)

    #get item properties
    item_properties = item_page.get_item_description()

    #add the first item
    added_item_arr = []
    name, price = item_page.add_item_cart(item_properties[0])
    added_item_arr.append({'name':name, 'price':price})

    item_page.take_page_screenshot("After adding item")

    #click cart icon
    item_page.click_btn(item_page.item_cart)
    
    cart_page.take_page_screenshot("Cart page")
    #check if item inside cart is same
    assert cart_page.is_item_same(added_item_arr) == True, "Item is not same"

@step("User remove item from cart")
@title("[Positive] Verify user can remove item from cart")
@severity(allure.severity_level.BLOCKER)
def test_remove_item(user_login):
    driver = user_login
    item_page = Inventory_page(driver)
    cart_page = Cart_page(driver)

    #get item properties
    item_properties = item_page.get_item_description()

    #add the first item
    added_item_arr = []
    name, price = item_page.add_item_cart(item_properties[0])
    added_item_arr.append({'name':name, 'price':price})
    item_page.take_page_screenshot("After adding item")

    #click cart icon
    item_page.click_btn(item_page.item_cart)
    cart_page.take_page_screenshot("Cart page")
    
    #click remove item
    cart_page.remove_item()

    #check if cart empty
    assert cart_page.is_cart_empty() == True, "Might be logical fault, cart is not empty!"
    cart_page.take_page_screenshot("After removing item")


@step("Check cart icon bubble number")
@title("[Positive] Verify cart icon will show number of item inside cart")
@severity(allure.severity_level.MINOR)
def test_cart_icon(user_login):
    driver = user_login
    item_page = Inventory_page(driver)

    #adding one item
    for i in range (6):
        item_properties = item_page.get_item_description()
        name, price = item_page.add_item_cart(item_properties[i])
        assert item_page.get_text(item_page.item_cart) == f"{i+1}"
    
    item_page.take_page_screenshot("Added all item")
    
    #removing one item
    for i in range(5, -1, -1):
        item_properties = item_page.get_item_description()
        name, price = item_page.remove_item_cart(item_properties[i])
        if i != 0:
            assert item_page.get_text(item_page.item_cart) == f"{i}"
        else:
            # child = item_page.item_cart[1] 
            # child 
            # assert len(item_page.get_child(item_page.item_cart)) == 0
            assert len(item_page.get_child(item_page.get(item_page.item_cart))) == 0
    
    item_page.take_page_screenshot("Removed all item")

# @step("")
@title("[Positive] Verify user can see item details when clicking on item title inside cart")
@severity(allure.severity_level.CRITICAL)
def test_item_title_cart(user_login):
    driver = user_login
    item_page = Inventory_page(driver)
    cart_page = Cart_page(driver)
    item_desc_page = desc_page(driver)

    #get item properties
    item_properties = item_page.get_item_description()

    #add the first item
    added_item_arr = []
    name, price = item_page.add_item_cart(item_properties[0])
    added_item_arr.append({'name':name, 'price':price})

    item_page.take_page_screenshot("After adding item")

    #click cart icon
    item_page.click_btn(item_page.item_cart)
    
    cart_page.take_page_screenshot("Cart page")
    
    item_properties = cart_page.get_item_properties()
    cart_page.click_btn(item_properties[0]['desc_button'])
    
    item_desc_page.take_page_screenshot("Item description page")
    
    #check if item inside cart is same
    assert item_desc_page.get_text(item_desc_page.name) == item_properties[0]['name'] 
    assert item_desc_page.get_text(item_desc_page.description) == item_properties[0]['description']
    assert item_desc_page.get_text(item_desc_page.price) == item_properties[0]['price']


# @step("")
@title("[Positive] Verify user can see item details when clicking on item title inside cart")
@severity(allure.severity_level.BLOCKER)
def test_item_title_cart(user_login):
    driver = user_login
    item_page = Inventory_page(driver)
    cart_page = Cart_page(driver)

    #get item properties
    item_properties = item_page.get_item_description()

    #add the first item
    added_item_arr = []
    name, price = item_page.add_item_cart(item_properties[0])
    added_item_arr.append({'name':name, 'price':price})

    item_page.take_page_screenshot("After adding item")

    #user logout
    item_page.logout()
    item_page.take_page_screenshot("user logout")

    login(driver)

    item_page.take_page_screenshot("user login")

    #click cart icon
    item_page.click_btn(item_page.item_cart)

    assert cart_page.get_item_properties()[0]['name'] == name
    assert cart_page.get_item_properties()[0]['price'] == price
