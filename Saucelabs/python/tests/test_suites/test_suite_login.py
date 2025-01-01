import pytest
from tests.test_cases import (incorrect_password_login, incorrect_username_login, 
                              no_username_login, no_password_login, correct_credential_login)
from selenium import webdriver

# if __name__ == "__main__":
#     suite = unittest.TestSuite()
#     suite.addTest(login_incorrect_password('steps'))

#     runner = unittest.TextTestRunner()
#     runner.run(suite)
@pytest.fixture(scope="module")
def headless_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920x1080')

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_suite_login(headless_driver):
    #browser driver 
    driver = headless_driver

    #test case 1
    incorrect_password_login(driver)

    #test case 2
    incorrect_username_login(driver)

    #test case 3
    no_password_login(driver)

    #test case 4
    no_username_login(driver)

    #test case 5
    correct_credential_login(driver)