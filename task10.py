from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

class InstagramScraper:
    def __init__(self, username):
        self.username = username
        self.url = f"https://www.instagram.com/guviofficial/"
        self.driver = None

    def setup_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def get_followers_and_following(self):
        self.driver.get(self.url)
        time.sleep(5)  # Wait for the page to load

        followers = self.driver.find_element(By.XPATH, "//*[text()=' following']").text
        following = self.driver.find_element(By.XPATH, "//*[text()=' followers']").text

        # //*[text()=' following']
        # //*[text()=' followers']

        print(f"Followers: {followers}")
        print(f"Following: {following}")

    def close_driver(self):
        if self.driver:
            self.driver.quit()

    def run(self):
        self.setup_driver()
        try:
            self.get_followers_and_following()
        finally:
            self.close_driver()

if __name__ == "__main__":
    scraper = InstagramScraper("guviofficial")
    scraper.run()
