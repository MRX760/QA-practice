from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time 
import allure

class POM:
    def __init__(self, driver):
        self.driver = driver
        self.url = None
        self.footer_tag = (By.TAG_NAME, "footer")
        self.header_tag = (By.TAG_NAME, "header")
        self.not_found = (By.XPATH, "//*[text()='404']")
        self.not_found2 = (By.XPATH, "//*[text()='tidak ditemukan']")
        self.not_found3= (By.XPATH, "//*[text()='Not found']")
    
    def is_link_inactive(self, identifier) -> bool:
        self.click_btn(identifier)
        self.wait_to_render(self.footer_tag)
        result = self.is_exist(self.not_found) or self.is_exist(self.not_found2) or self.is_exist(self.not_found3)
        self.driver.back()
        return result

    @allure.step("click {button_name} button")
    def click_btn(self, identifier: tuple, button_name:str="") -> None:
        try:
            self.get(identifier).click()
        except Exception as e:
            try: 
                identifier.click()
            except:
                raise ValueError(f"Can't find button with identifier: {identifier}")

    def navigate_to(self, url:str):
        self.driver.get(url)

    def is_exist(self, identifier:tuple) -> bool:
        return True if self.find(identifier) else False
    
    def get(self, identfier:tuple) -> object:
        return self.driver.find_element(*identfier)

    def get_list(self,identifier:tuple)  -> list:
        return self.driver.find_elements(*identifier)
        # elements = WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located(identifier))
        # return elements
    
    def get_text(self, identifier:tuple) -> str:
        return self.get(identifier).text
    
    def get_wait(self, identifier:tuple, time:int=10) -> object:
        try:
            return WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located(identifier)
            )
        except Exception as e:
            raise ValueError(f"No presence of element with identifier: {identifier} \n Please check connection or element identifier. {e}")
    
    @allure.step("check the availability of an element")
    def wait_to_render(self, identifier:tuple, time:int=60) -> None:
        """
        Wait page to render by waiting for certain element "footer is recommended"
        Args:
            identifier (tuple): _description_
            time (int, optional): _description_. Defaults to 60.
        """
        WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located(identifier)
            )

    def wait_and_verify(self, identifier:tuple, time:int = 20) -> bool:
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(identifier))
            if element == None or element == [] or element == "":
                return False
            return True
        except TimeoutError:
            print("Can't find element with identifier")
            return False

    def is_clickable(self, identifier) -> bool:
        try:
            element = self.get(identifier) #if not webpage object
        except:
            element = identifier #if webpage object
        finally:
            try:
                element.click()
                return True
            except Exception as e:
                time.sleep(2)
                if self.driver.current_url != self.url:
                    
                    self.navigate_to(self.url)
                    self.driver.fullscreen_window()
                    self.wait_to_render(self.footer)
                    time.sleep(5)

                    return self.is_clickable(identifier)
                print(f'error (currently on {self.driver.current_url})::::> {e}')
                return False
            # return (element.is_enabled() and element.is_displayed())
            # return element.is_enabled()