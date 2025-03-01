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
    # options.add_argument("--headless") 
    options.add_argument("--disable-extensions")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_rendering_news(browser_driver):
    driver = browser_driver
    home = Home_page(driver)
    home.navigate_to(home.url)
    home.get_wait(home.news_update_button, time=60)
    home.hover_mouse(home.news_update_button)
    # element = driver.find_element(By.ID, "element_id")
    # driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", home.get(home.img_xpath))
    home.take_page_screenshot("rendered image on screenshot")
