import pytest
# from tests.test_cases import (incorrect_password_login, incorrect_username_login, 
#                               no_username_login, no_password_login, correct_credential_login)
from selenium import webdriver
from selenium.webdriver.common.by import By

from page.item_desc_page import desc_page
from page.cart_page import Cart_page
from page.inventory_page import Inventory_page
from page.address_info_page import Address_info_page
from page.checkout_detail import Checkout_page

from allure import (severity, severity_level, 
                    feature, story,
                    title, step)
import allure

#precondition steps
from .test_login import test_login_correct_credentials as login
from .test_item_cart import test_add_item as add_item

@pytest.fixture(autouse=True)
def set_allure_labels():
    allure.dynamic.feature("item-checkout")
    # allure.dynamic.severity(allure.severity_level.BLOCKER)
    allure.dynamic.suite("Validate item checkout functionality")
    allure.dynamic.story("User can checkout item on cart")

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

@pytest.fixture(scope="function")
def user_add_item(user_login):
    add_item(user_login)
    yield user_login


@step("User checkout empty cart")
@title("[Negative] Verify user can't checkout item when no item inside cart")
@severity(allure.severity_level.BLOCKER)
def test_checkout_none(user_login):
    driver = user_login
    item_page = Inventory_page(driver)
    cart_page = Cart_page(driver)

    item_page.click_btn(item_page.item_cart)
    cart_page.take_page_screenshot("Cart")

    assert cart_page.is_element_clickable(cart_page.checkout_btn) == False, "Might be logical fault, element not clickable"

@step("User checkout cart")
@title("[Positive] Verify user can checkout when there's item inside cart")
@severity(allure.severity_level.BLOCKER)
def test_checkout_item(user_add_item):
    driver = user_add_item
    cart_page = Cart_page(driver)
    address_page = Address_info_page(driver)
    
    cart_page.take_page_screenshot("Cart page")

    cart_page.click_btn(cart_page.checkout_btn)
    
    address_page.take_page_screenshot("address page")

    assert address_page.get_text(address_page.title) == "Checkout: Your Information"


@step("User checkout cart")
@title("[Positive] Verify user can continue to payment after filling address detail")
@severity(allure.severity_level.BLOCKER)
def test_checkout_payment(user_add_item):
    driver = user_add_item
    cart_page = Cart_page(driver)
    address_page = Address_info_page(driver)
    checkout_page = Checkout_page(driver)

    cart_page.take_page_screenshot("Cart page")

    cart_page.click_btn(cart_page.checkout_btn)
    
    address_page.take_page_screenshot("address page")

    address_page.insert_detail("joan", "arc", "1234")

    address_page.click_btn(address_page.continue_btn)
    
    assert checkout_page.get_text(checkout_page.title) == "Checkout: Overview"


@step("User checkout cart")
@title("[Positive] Verify user can complete checkout if item is inside cart")
@severity(allure.severity_level.BLOCKER)
def test_checkout_complete(user_add_item):
    driver = user_add_item
    cart_page = Cart_page(driver)
    address_page = Address_info_page(driver)
    checkout_page = Checkout_page(driver)

    cart_page.take_page_screenshot("Cart page")

    cart_page.click_btn(cart_page.checkout_btn)
    
    address_page.take_page_screenshot("address page")

    address_page.insert_detail("joan", "arc", "1234")

    address_page.click_btn(address_page.continue_btn)
    
    # assert checkout_page.get_text(checkout_page.title) == "Checkout: Overview"
    checkout_page.click_btn(checkout_page.finish)

    assert checkout_page.get_text(checkout_page.completed_text) == "Thank you for your order!"


@step("User checkout cart")
@title("[Negative] Verify user can't access payment without filling address detail")
@severity(allure.severity_level.BLOCKER)
def test_checkout_incomplete_address(user_add_item):
    driver = user_add_item
    cart_page = Cart_page(driver)
    address_page = Address_info_page(driver)
    checkout_page = Checkout_page(driver)

    cart_page.take_page_screenshot("Cart page")

    cart_page.click_btn(cart_page.checkout_btn)
    
    address_page.take_page_screenshot("address page")

    address_page.click_btn(address_page.continue_btn)

    assert address_page.get_text(address_page.fail_alert) == "Error: First Name is required"


@title("[Negative] Verify user can't  continue to payment when last name on address detail form didn't filled")
@severity(allure.severity_level.BLOCKER)
def test_checkout_incomplete_lastname(user_add_item):
    driver = user_add_item
    cart_page = Cart_page(driver)
    address_page = Address_info_page(driver)

    cart_page.take_page_screenshot("Cart page")

    cart_page.click_btn(cart_page.checkout_btn)
    
    address_page.take_page_screenshot("address page")

    address_page.insert_detail("Joan", "", "1234")
    address_page.click_btn(address_page.continue_btn)

    assert address_page.get_text(address_page.fail_alert) == "Error: Last Name is required"

@title("[Negative] Verify user can't  continue to payment when first name on address detail form didn't filled")
@severity(allure.severity_level.BLOCKER)
def test_checkout_incomplete_firstname(user_add_item):
    driver = user_add_item
    cart_page = Cart_page(driver)
    address_page = Address_info_page(driver)

    cart_page.take_page_screenshot("Cart page")

    cart_page.click_btn(cart_page.checkout_btn)
    
    address_page.take_page_screenshot("address page")

    address_page.insert_detail("", "Arc", "1234")
    address_page.click_btn(address_page.continue_btn)

    assert address_page.get_text(address_page.fail_alert) == "Error: First Name is required"

@title("[Negative] Verify user can't  continue to payment when postal code on address detail form didn't filled ")
@severity(allure.severity_level.BLOCKER)
def test_checkout_incomplete_zip(user_add_item):
    driver = user_add_item
    cart_page = Cart_page(driver)
    address_page = Address_info_page(driver)

    cart_page.take_page_screenshot("Cart page")

    cart_page.click_btn(cart_page.checkout_btn)
    
    address_page.take_page_screenshot("address page")

    address_page.insert_detail("Joan", "Arc", "")
    address_page.click_btn(address_page.continue_btn)

    assert address_page.get_text(address_page.fail_alert) == "Error: Postal Code is required"

# @step("User checkout cart")
@title("[Positive] Verify the cart will be emptied once the checkout completed")
@severity(allure.severity_level.CRITICAL)
def test_checkout_complete(user_add_item):
    driver = user_add_item
    item_page = Inventory_page(driver)
    cart_page = Cart_page(driver)
    address_page = Address_info_page(driver)
    checkout_page = Checkout_page(driver)

    cart_page.take_page_screenshot("Cart page")

    cart_page.click_btn(cart_page.checkout_btn)
    
    address_page.take_page_screenshot("address page")

    address_page.insert_detail("joan", "arc", "1234")

    address_page.click_btn(address_page.continue_btn)
    
    # assert checkout_page.get_text(checkout_page.title) == "Checkout: Overview"
    checkout_page.click_btn(checkout_page.finish)
    checkout_page.take_page_screenshot("Order completed")
    checkout_page.click_btn(checkout_page.go_back_home)
    
    item_page.click_btn(item_page.item_cart)
    checkout_page.take_page_screenshot("Order completed")
    assert cart_page.is_cart_empty() == True

    # assert checkout_page.get_text(checkout_page.completed_text) == "Thank you for your order!"