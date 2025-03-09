from selenium.webdriver.common.by import By
from .POM import POM
from allure import step
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

class Cart_page(POM):
    def __init__(self, driver):
        super().__init__(driver)
        self.cart_list = (By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]') #only 2 child when empty, more than 2 if cart exist
        self.cart_items = (By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]')
        self.item_labels = (By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]')
        # self.item_name = '//*[@id="item_4_title_link"]'
        self.checkout_btn = (By.XPATH, '//*[@id="checkout"]')
        
        
    @step("Checking if cart is empty")
    def is_cart_empty(self):
        childs = self.get_child(self.cart_list)
        if len(childs) == 2:
            return True
        for num, child in enumerate(childs):
            if num > 2:
                if child.get_attribute("class") != "removed_cart_item":
                    return False
        return True
    
    @step("Checking if item inside cart has identical price and title")
    def is_item_same(self, added_item_description_arr_dict):
    
        cart_item = self.get_item_properties()
        #checking if cart item is all same
        for num, dictionary in enumerate(cart_item):
            if dictionary['name'] == added_item_description_arr_dict[num]['name'] and dictionary['price'] == added_item_description_arr_dict[num]['price']:
                continue
            else:
                return False
        return True
    
    @step("Reading item properties in cart")
    def get_item_properties(self):
        cart_item = []
        
        #check if the child element exist
        childs = self.get_child(self.cart_list)
        if len(childs) <= 2:
            return cart_item
        
        #store all the cart item description
        for num, child in enumerate(childs):
            if num < 2 or child.get_attribute("class") == "removed_cart_item":
                continue
            name = self.get_text(child.find_element(By.XPATH, './div[2]/a'))
            desc_button = child.find_element(By.XPATH, './div[2]/a')
            price = self.get_text(child.find_element(By.XPATH, './div[2]/div[2]/div'))
            description = self.get_text(child.find_element(By.XPATH, './div[2]/div'))
            remove_btn = child.find_element(By.XPATH, './div[2]/div[2]/button')
            cart_item.append({'name':name, 'desc_button': desc_button, 'price':price, 'description':description, 'remove_btn':remove_btn})
        return cart_item

    @step("Removing item from cart")
    def remove_item(self, id = -1):
        cart_items = self.get_item_properties()
        if id == -1:
            for item in cart_items:
                self.click_btn(item['remove_btn'])
        else:
            self.click_btn(cart_items[id]['remove_btn'])









