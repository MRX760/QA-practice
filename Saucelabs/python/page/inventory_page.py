from selenium.webdriver.common.by import By
from .POM import POM
from allure import step
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

class Inventory_page(POM):
    def __init__(self, driver):
        super().__init__(driver)
        self.title = (By.XPATH, '//*[@id="header_container"]/div[2]/span')
        self.item_list_container = (By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div')
        self.item_name = (By.XPATH, '//*[@id="item_4_title_link"]/div')
        self.item_sort = (By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select')
        self.item_cart = (By.XPATH, '//*[@id="shopping_cart_container"]/a')
        self.burger_btn = (By.XPATH, '//*[@id="react-burger-menu-btn"]')
        self.burger_btn_menu = (By.XPATH, '//*[@id="menu_button_container"]/div/div[2]/div[1]/nav')

    @step("user logout")
    def logout(self):
        self.click_btn(self.burger_btn)
        self.click_btn(self.get(self.burger_btn_menu).find_element(By.XPATH, './a[3]'))

    def get_item_description(self, id=0) -> list:
        items = self.get_list(self.item_list_container)
        description =[]
        for item in items:
            name = self.get_text(item.find_element(By.XPATH, './div[2]/div/a/div'))
            desc = self.get_text(item.find_element(By.XPATH, './div[2]/div/div'))
            price = self.get_text(item.find_element(By.XPATH, './div[2]/div[2]/div'))
            add_cart_button = item.find_element(By.XPATH, './div[2]/div[2]/button')

            description.append({'name':name, 'description':desc, 'price':price, 'add_cart_button':add_cart_button})
        if id<=0:
            return description
        else:
            return [description[id-1]]

    @step("add item to cart")
    def add_item_cart(self, web_element_dictionary):
        self.click_btn(web_element_dictionary['add_cart_button'])
        # name = web_element_dictionary['name']
        return web_element_dictionary['name'], web_element_dictionary['price']
    
    @step("remove item to cart")
    def remove_item_cart(self, web_element_dictionary):
        self.click_btn(web_element_dictionary['add_cart_button'])
        return web_element_dictionary['name'], web_element_dictionary['price']


