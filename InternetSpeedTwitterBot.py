import time
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
        self.results_visible = False
        self.twitter_acc = "CCC-WatchDog"
        self.twitter_username = "colinchinchoy@gmail.com"
        self.twitter_password = "C0l1nC41nC40y"
        self.flow_handle = "@Flowtt"

    def get_internet_speed(self):
        self.driver.get("https://speedtest.net/")
        self.start_btn = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".start-button [href]")))
        self.start_btn.click()
        time.sleep(80)
        self.down = self.driver.find_element(By.XPATH,"/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span").text
        self.up = self.driver.find_element(By.XPATH,"/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text  
        print(f"Down Speed = {self.down} / Up Speed = {self.up}")
    
    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")
        time.sleep(10)
        signin_btn = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a")
        signin_btn.click()
        time.sleep(5)
        username_input = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label/div")
        username_input.send_keys(self.twitter_username)
        next_button = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div/div[6]")
        next_button.click()
        time.sleep(5)
        password_input = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        password_input.send_keys(self.twitter_password)
        login_btn = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div")
        login_btn.click()
