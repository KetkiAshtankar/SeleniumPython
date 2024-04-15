from selenium import webdriver
import time

from selenium.webdriver.common.by import By

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open the download page
driver.get("https://practice.expandtesting.com/download")

# Find and click the download button
download_button = driver.find_element(By.LINK_TEXT,"1710148878589_12345.jpeg")
# download_button = driver.find_element_by_xpath("//a[@href='/download']")
download_button.click()

# Wait for the download to complete
time.sleep(5)  # Adjust the sleep time as needed

# Close the browser
driver.quit()
