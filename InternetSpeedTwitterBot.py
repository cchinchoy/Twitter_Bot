from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

class InternetSpeedTwitterBot:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://speedtest.net/")
        self.start_btn = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".start-button [href]")))
        self.start_btn.click()

    def tweet_at_provider(self):
        data_dwn = WebDriverWait(self.driver,60).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,".result-container-speed .result-container-data [class]")))
        for item in data_dwn:
            print(item)

