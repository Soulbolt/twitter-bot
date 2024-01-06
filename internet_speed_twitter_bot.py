from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_SPEED = 150
PROMISED_UP = 10
CHROME_OPTIONS = webdriver.ChromeOptions()
TWITTER_EMIAL = "email_here"
TWITTER_PASSWORD = "password_here"
OPTIONS = CHROME_OPTIONS.add_experimental_option("detach", True)

class InternetSpeedTwitterBot:
    
    def __init__(self):
        self.driver = webdriver.Chrome(options=OPTIONS)
        self.down = 0
        self.up = 0

    def test_speed(self):
        self.driver.get("https://www.speedtest.net")
        time.sleep(5)
        go_button = self.driver.find_element(By.CLASS_NAME, value="start-text")
        go_button.click()
        time.sleep(50)
        down_speed = self.driver.find_element(By.CLASS_NAME, value="download-speed")
        self.down = print(f"Download speed: {down_speed.text} Mbps")
        up_speed = self.driver.find_element(By.CLASS_NAME, value="upload-speed")
        self.up = print(f"Upload speed: {up_speed.text} Mbps")