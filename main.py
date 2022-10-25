from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://speedtest.net/")

start_btn = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".start-button [href]")))
start_btn.click()

data_dwn = WebDriverWait(driver,60).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,".result-data-large [class]")))
for item in data_dwn:
    print(item.text)