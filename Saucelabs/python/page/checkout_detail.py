from selenium.webdriver.common.by import By
from .POM import POM
from allure import step
from selenium.webdriver.common.keys import Keys

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

class Checkout_page(POM):
    def __init__(self, driver):
        super().__init__(driver)
        self.title = (By.XPATH, '//*[@id="header_container"]/div[2]/span')
        self.finish = (By.XPATH, '//*[@id="finish"]')
        self.completed_text = (By.XPATH, '//*[@id="checkout_complete_container"]/h2')
        self.go_back_home = (By.XPATH, '//*[@id="back-to-products"]')
        