from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class POM:
    def __init__(self, driver):
        self.driver = driver
    
    def click_btn(self, identifier: tuple) -> None:
        try:
            self.get(identifier).click()
        except Exception as e:
            raise ValueError(f"Can't find button with identifier: {identifier}")

    def navigate_to(self, url:str):
        self.driver.get(url)

    def is_exist(self, identifier:tuple) -> bool:
        return True if self.find(identifier) else False
    
    def get(self, identfier:tuple) -> object:
        return self.driver.find_element(*identfier)

    def get_list(self,identifier:tuple)  -> list:
        return self.driver.find_elements(*identifier)
    
    def get_text(self, identifier:tuple) -> str:
        return self.get(identifier).text
    
    def get_wait(self, identifier:tuple, time:int=10) -> object:
        try:
            return WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located(identifier)
            )
        except Exception as e:
            raise ValueError(f"No presence of element with identifier: {identifier} \n Please check connection or element identifier.")