from selenium.webdriver.common.by import By
from .POM import POM
from selenium.webdriver.common.action_chains import ActionChains

# reporting library
import allure
from allure_commons.types import AttachmentType
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class Login_page(POM):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_col = (By.ID, "user-name")
        self.password_col = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.login_error_alert = (By.CLASS_NAME, "error-message-container.error")
        self.login_error_msg = (By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
        self.login_error_alert_close_btn = (By.CLASS_NAME, "error-button")
        self.login_url = "https://www.saucedemo.com/"

    @allure.step("Insert username as {username}")
    def insert_username(self, username:str) -> None:
        self.action.double_click(self.get(self.username_col))
        if username != "":
            self.action.send_keys(username)
        else:
            self.action.send_keys("a")
            self.action.send_keys(Keys.BACKSPACE)
        self.action.perform()
    
    @allure.step("Insert password to be {password}")
    def insert_password(self, password:str) -> None:
        self.action.double_click(self.get(self.password_col))
        if password != "":
            self.action.send_keys(password)
        else:
            self.action.send_keys("a")
            self.action.send_keys(Keys.BACKSPACE)
        self.action.perform()
    
    # @allure.step("Insert username as {username}, and with {password} as the password")
    def insert_credentials(self, username:str, password:str) -> None:
        self.insert_username(username)
        self.insert_password(password)
    
    @allure.step("Login as {username} with password '{password}'")
    def login_as(self,username:str, password:str) -> None:
        self.insert_credentials(username, password)
        self.click_btn(self.login_button)
    
    @allure.step("Execute script to make password field visible")
    def make_pass_visible(self) -> None:
        self.driver.execute_script("arguments[0].type = 'text';" , self.get(self.password_col))