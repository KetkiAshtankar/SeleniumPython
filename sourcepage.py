from selenium import webdriver
from selenium.webdriver.common.by import By
# Initialize Chrome WebDriver
driver = webdriver.Chrome()
# Open SauceDemo website
driver.get("https://www.saucedemo.com/")
# Perform login (assuming username and password fields have IDs "user-name" and "password")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
# Fetch title of the webpage
title = driver.title
print("Title of the webpage:", title)
# Fetch current URL of the webpage
current_url = driver.current_url
print("Current URL of the webpage:", current_url)
# Extract entire contents of the webpage
page_source = driver.page_source
# Save contents to a text file
with open("Webpage_task.txt", "w", encoding="utf-8") as file:
    file.write(page_source)
# Close the browser
driver.quit()
