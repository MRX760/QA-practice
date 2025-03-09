from selenium.webdriver.common.by import By
from .POM import POM
from allure import step
from selenium.webdriver.common.keys import Keys

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

class Address_info_page(POM):
    def __init__(self, driver):
        super().__init__(driver)
        self.title = (By.XPATH, '//*[@id="header_container"]/div[2]/span')
        self.first_name = (By.XPATH, '//*[@id="first-name"]')
        self.last_name = (By.XPATH, '//*[@id="last-name"]')
        self.zip_code = (By.XPATH, '//*[@id="postal-code"]')
        self.continue_btn = (By.XPATH, '//*[@id="continue"]')
        self.fail_alert = (By.XPATH, '//*[@id="checkout_info_container"]/div/form/div[1]/div[4]/h3')
        
    
    @step("Insert first name as {username}")
    def insert_first_name(self, username:str) -> None:
        self.action.double_click(self.get(self.first_name))
        if username != "":
            self.action.send_keys(username)
        else:
            self.action.send_keys("a")
            self.action.send_keys(Keys.BACKSPACE)
        self.action.perform()

    @step("Insert last name as {username}")
    def insert_last_name(self, username:str) -> None:
        self.action.double_click(self.get(self.last_name))
        if username != "":
            self.action.send_keys(username)
        else:
            self.action.send_keys("a")
            self.action.send_keys(Keys.BACKSPACE)
        self.action.perform()
    
    @step("Insert zip as {username}")
    def insert_zip(self, username:str) -> None:
        self.action.double_click(self.get(self.zip_code))
        if username != "":
            self.action.send_keys(username)
        else:
            self.action.send_keys("a")
            self.action.send_keys(Keys.BACKSPACE)
        self.action.perform()
    
    def insert_detail(self, first, last, zip):
        self.insert_first_name(first)
        self.insert_last_name(last)
        self.insert_zip(zip)
