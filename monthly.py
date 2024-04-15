import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://labour.gov.in/")
time.sleep(5)
driver.find_element(By.XPATH,'//a[contains(text(),"Monthly Progress Report")]').click
time.sleep(2)