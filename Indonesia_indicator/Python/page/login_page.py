from selenium.webdriver.common.by import By
from .POM import POM
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

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

    def insert_username(self, username:str) -> None:
        self.get(self.username_col).send_keys(username)
    
    def insert_password(self, password:str) -> None:
        self.get(self.password_col).send_keys(password)
    
    def insert_credentials(self, username:str, password:str) -> None:
        self.insert_username(username)
        self.insert_password(password)
    
    def login_as(self,username:str, password:str) -> None:
        self.insert_credentials(username, password)
        self.click_btn(self.login_button)