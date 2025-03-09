from selenium.webdriver.common.by import By
from .POM import POM
from allure import step
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

class desc_page(POM):
    def __init__(self, driver):
        super().__init__(driver)
        self.img_container = (By.XPATH, '//*[@id="inventory_item_container"]/div/div/div')
        self.desc_container = (By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]')
        self.name = (By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div')
        self.description = (By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[2]')
        self.price = (By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[3]')
        self.button = (By. XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/button')
        
    # @step("Checking if cart is empty")
    