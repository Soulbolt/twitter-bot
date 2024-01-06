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

    def tweet_complaint(self):
        self.driver.get("https://twitter.com")
        time.sleep(3)
        login = self.driver.find_element(By.LINK_TEXT, value="Sign in")
        login.click()
        time.sleep(3)
        sign_in_with_google = self.driver.find_element(By.LINK_TEXT, value="Sign in with Google")
        sign_in_with_google.click()
        time.sleep(3)
        tweet_button = self.driver.find_element(By.LINK_TEXT, value="Tweet")
        tweet_button.click()
        active = self.driver.switch_to.active_element
        active.send_keys(f"Download speed was {self.down} Mbps and Upload was {self.up} Mbps. Fix it please")
        time.sleep(15)

    def quit(self):
        self.driver.quit()
