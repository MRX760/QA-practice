# main library
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

#just in case for heavy load websites, also mimicking human interaction
from selenium.webdriver.common.action_chains import ActionChains

# reporting library
import allure
from allure_commons.types import AttachmentType

class POM:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)
    
    @allure.step("Clicking button")  
    def click_btn(self, identifier: tuple) -> None:
        """Clicking button

        Args:
            identifier (tuple): For example, (By.ID, "user-name") or else.

        Raises:
            ValueError: If identifier is non exist.
        """
        try:
            if isinstance(identifier, WebElement):
                self.action.move_to_element(identifier)
                self.action.click(identifier)
            else:
                if 'option' not in identifier[1]:
                    self.action.move_to_element(self.get(identifier))
                self.action.click(self.get(identifier))
            self.action.perform()
        except Exception as e:
            raise ValueError(f"Can't find button with identifier: {identifier}, {e}")

    @allure.step("Select/click button with text {txt}")
    def select(self, identifier, txt):
        button = Select(self.get(identifier))
        button.select_by_visible_text(txt)

    @allure.step("Hovering mouse to element {identifier}")
    def hover(self, identifier: tuple) -> None:
        """Hovering mouse to an element of given identifier

        Args:
            identifier (tuple): For example, (By.ID, "user-name") or else.
        """
        try:
            self.action.move_to_element(self.get(identifier))
            self.action.perform()
        except Exception as e:
            raise(e)

    @allure.step("Navigate to {url}")
    def navigate_to(self, url:str):
        """Redirecting to given URL

        Args:
            url (str): address to redirect
        """
        self.driver.get(url)

    @allure.step("Checking if element exist ({identifier})")
    def is_exist(self, identifier:tuple) -> bool:
        """Checking if element exist, return True when exist and False if non-exist.

        Args:
            identifier (tuple): For example, (By.ID, "user-name") or else.

        Returns:
            bool: Status (boolean)
        """
        return True if self.find(identifier) else False
    
    def get(self, identfier:tuple) -> object:
        """Get element object by identifier

        Args:
            identfier (tuple): For example, (By.ID, "user-name") or else.

        Returns:
            object: Element object
        """
        return self.driver.find_element(*identfier)

    def get_list(self,identifier:tuple)  -> list:
        """Get element of object but with list

        Args:
            identifier (tuple): For example, (By.ID, "user-name") or else.

        Returns:
            list: Element object in list
        """
        return self.driver.find_elements(*identifier)
    
    def get_text(self, identifier:tuple) -> str:
        """Get text within specified container ID

        Args:
            identifier (tuple): For example, (By.ID, "user-name") or else.

        Returns:
            str: Text within container ID
        """
        if isinstance(identifier, tuple):
            return self.get(identifier).text
        elif isinstance(identifier, WebElement):
            return identifier.text
        else:
            raise ValueError("supported instance -> tuple/WebElement")
    
    def get_wait(self, identifier:tuple, time:int=10) -> object:
        """Get element object with timeout wait, can be used for checking if element is exist within particular time after actions.
        Args:
            identifier (tuple): For example, (By.ID, "user-name") or else.
            time (int, optional): Timeout wait. Defaults to 10.

        Raises:
            ValueError: Wrong/non-exist identifier

        Returns:
            object: Object with given identifier
        """
        try:
            return WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located(identifier)
            )
        except Exception as e:
            raise ValueError(f"No presence of element with identifier: {identifier} \n Please check connection or element identifier.")

    @allure.step("Take Screenshot")  
    def take_page_screenshot(self, file_name):
        """Take page screenshot

        Args:
            file_name (_type_): Filename of screenshot file
        """
        try:
            allure.attach(self.driver.get_screenshot_as_png(), name=file_name, attachment_type=AttachmentType.PNG)
        except AttributeError:
            print("Take screenshot failed. Please use the web_driver and not the POM driver. The driver you passed didn't support .get_screenshot_as_png() function")
        except Exception as e:
            print(f"Error: {e}")

    def get_child(self, identifier):
        if isinstance(identifier, tuple):
            by, address = identifier
            address+='/*'
            return self.get_list((by,address))
        elif isinstance(identifier, WebElement):
            return identifier.find_elements(By.XPATH, './*')
        

    def is_clickable(self, identifier):
        from selenium.webdriver.support import expected_conditions as EC

    def is_element_clickable(self, element):
        """Checks if an element is clickable using ActionChains."""
        try:
            # Move to the element to ensure it's visible and interactable
            element = self.get(element)
            ActionChains(self.driver).move_to_element(element).perform()

            # Check if it's clickable using Selenium's expected conditions
            WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(element))

            return True  # If no exception is raised, the element is clickable
        except Exception as e:
            print(f"Element not clickable: {e}")
            return False  # If an exception occurs, the element is not clickable
        
        