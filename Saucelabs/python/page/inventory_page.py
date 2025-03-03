from selenium.webdriver.common.by import By
from .POM import POM
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

class Inventory_page(POM):
    def __init__(self, driver):
        super().__init__(driver)
        self.title = (By.XPATH, '//*[@id="header_container"]/div[2]/span')
        self.item_list = (By.XPATH, '//*[@id="inventory_container"]/div')
