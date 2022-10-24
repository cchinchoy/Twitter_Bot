from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


chrome_selenium_driver_path = 'C:\bin\chromedriver.exe'

PROMISED_DOWN = 300
PROMISED_UP = 20

START_TEST = "js-start-test test-mode-multi"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

