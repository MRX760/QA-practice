# main library
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
            self.action.move_to_element(self.get(identifier))
            self.action.click(self.get(identifier))
            self.action.perform()
        except Exception as e:
            raise ValueError(f"Can't find button with identifier: {identifier}")

    @allure.step("Hovering mouse to element {identifier}")
    def hover_mouse(self, identifier: tuple) -> None:
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
        return self.get(identifier).text
    
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