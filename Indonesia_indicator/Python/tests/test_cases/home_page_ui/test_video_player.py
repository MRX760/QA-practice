import pytest
from selenium import webdriver
from page.home_page import Home_page
import time
from selenium.webdriver.chrome.options import Options
import allure
from allure_commons.types import AttachmentType



@pytest.fixture(scope="function")
def browser_driver():
    options = Options()
    options.add_argument("--headless") 
    options.add_argument("--disable-extensions")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    yield driver
    take_page_screenshot(driver, "rendered web at the end of the test")
    driver.quit()


def test_video_player_can_be_played(browser_driver):
    driver = browser_driver
    home = Home_page(driver)
    navigate_url(home, home.url)
    driver.fullscreen_window()
    # ytb_video_btn = get_element(home, home.ytb_play_btn, 'youtube video play button')
    ytb_video_btn = home.get(home.ytb_play_btn)
    home.click_btn(ytb_video_btn, "play")
    home.wait_and_verify(home.ytb_video)

@allure.step("check if link active")
def check(POM_driver, links):
    for link in links:
        assert POM_driver.is_link_inactive(link) == False

@allure.step("Navigate to {url}")
def navigate_url(POM_driver, url):
    POM_driver.navigate_to(url)    
    
    #wait to render
    POM_driver.wait_to_render(POM_driver.footer)
    time.sleep(5)

@allure.step("Take page screenshot")
def take_page_screenshot(browser_driver, file_name):
    """
    Should be webdriver like webdriver.Chrome()
    """
    try:
        allure.attach(browser_driver.get_screenshot_as_png(), name=file_name, attachment_type=AttachmentType.PNG)
    except AttributeError:
        print("Take screenshot failed. Please use the web_driver and not the POM driver. The driver you passed didn't support .get_screenshot_as_png() function")
    except Exception as e:
        print(f"Error: {e}")

@allure.step("Take element screenshot")
def take_element_screenshot(element_webpage_class):
    allure.attach(element_webpage_class.get_screenshot_as_png(), name='screenshots', attachment_type=AttachmentType.PNG)

@allure.step("Get element {element_name}")
def get_element(POM_driver, locator, element_name="(not specified)"):
    element = POM_driver.get_wait(locator)
    assert element != None
    assert element != []
    assert element != ""
    return element

@allure.step("Get All element {element_name}")
def get_elements(POM_driver, locator, element_name="(not specified)"):
    elements = POM_driver.get_list(locator)
    # print(elements)
    assert elements != []
    return elements

@allure.step("Check element are clickable")
def check_clickable(POM_driver, elements, idx=0, stats=True):
    elements = filter_enabled_only(elements)
    elements = filter_displayed_only(elements)
    elements = elements[idx:-1]
    for idx2, element in enumerate(elements):
        # print(f'{button.is_enabled()} {button.is_displayed()}')
        # if element.is_displayed() :
            # home.wait_to_render(*button)
            # try:
            #     element.screenshot(f'documentation/test_all_button_clickable button{str(idx+1)}.png')    
            # except:
            #     pass
            #     take_screenshots(POM_driver)
            # print(f'{element.get_attribute('class')} {element.get_attribute('id')}\n')
        # try:
        assert POM_driver.is_clickable(element) == True
        # except Exception as e:
        #     if stats == True:
        #         check_clickable(POM_driver, get_elements(POM_driver, POM_driver.CTA_button, "CTA button (recapture)"), idx=idx+idx2+1, stats=False)
        #     else:
        #         raise Exception(f"Error:::::::> {e}")
        # stats = POM_driver.is_clickable(element)
        # take_page_screenshot(POM_driver.driver, f"After action {idx+1}")

@allure.step("Check element are unclickable")
def check_unclickable(POM_driver, elements):
    # filtered_elements = [element for element in elements if not element.is_displayed or not element.is_enabled()]
    for element in elements:
        assert POM_driver.is_clickable(element) == False

@allure.step("Filter only displayed elements")
def filter_displayed_only(elements):
    return [element for element in elements if element.is_displayed()]

@allure.step("Filter only enabled elements")
def filter_enabled_only(elements):
    return [element for element in elements if element.is_displayed()]
