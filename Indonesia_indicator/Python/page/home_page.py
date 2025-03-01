from selenium.webdriver.common.by import By
from .POM import POM
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

class Home_page(POM):
    def __init__(self, driver):
        super().__init__(driver)
        self.header = (By.XPATH, "//*[@id='navbar']/div")
        self.menu_navbar = (By.XPATH, "//*[@id='navbar']/div/div/ul") 
        self.CTA_button = (By.TAG_NAME, 'button')
        self.CTA_link = (By.TAG_NAME, "a")
        self.footer = (By.XPATH, "//*[@id='root']/div[11]/div/section/div[1]/div/div/div")
        self.ytb_play_btn = (By.XPATH, "//*[@id='movie_player']/div[4]/button")
        self.ytb_video = (By.XPATH, "//*[@id='movie_player']/div[1]/video[contains(@src, 'blob:https://www.youtube.com')]")
        # self.home_navbar = (By.XPATH, "//*[@id='navbar']/div/a")
        self.home_navbar = (By.XPATH, "//a[@navigate='home']")
        self.about = (By.XPATH, "//*[@id='navbar']/div/div/ul/li[1]/a")
        self.strategy = (By.XPATH, "//*[@id='navbar']/div/div/ul/li[2]/a")
        self.product = (By.XPATH, "//*[@id='navbar']/div/div/ul/li[3]/a")
        self.news = (By.XPATH, "//*[@id='navbar']/div/div/ul/li[4]/a")
        self.i2academy = (By.XPATH, "//*[@id='navbar']/div/div/ul/li[5]/a")
        self.url = "https://indonesiaindicator.com/home"
        self.base_url = "https://indonesiaindicator.com"
        
        # self.img_xpath = (By.XPATH, '//*[@id="root"]/div[7]/div/section/div/div/div[2]/div[1]/div/a/img')
        self.news_update_container = (By.XPATH, '//*[@id="root"]/div[7]')
        self.news_update_button = (By.XPATH, '//*[@id="root"]/div[7]/div/section/div/div/div[2]/div[1]/div/div/a/button')
        