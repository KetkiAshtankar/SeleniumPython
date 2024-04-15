import time
from selenium import webdriver


# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the login page
driver.get("https://www.saucedemo.com")

# Simple Usage: Finding and interacting with DOM elements
username_input = driver.find_element_by_id("user-name")
password_input = driver.find_element_by_id("password")
login_button = driver.find_element_by_xpath("//input[@type='submit']")

# Input data into the username and password fields
username_input.send_keys("standard_user")
password_input.send_keys("secret_sauce")

# Click the login button
login_button.click()


# Wait for 2 seconds
time.sleep(2)

# Go back in history
driver.back()
print("Current URL after going back:", driver.current_url)

# Wait for 2 seconds
time.sleep(2)

# Go forward in history
driver.forward()
print("Current URL after going forward:", driver.current_url)

# Wait for 2 seconds
time.sleep(2)

# Refresh the page
driver.refresh()
print("Page refreshed")

# Wait for 2 seconds
time.sleep(2)

# Close the browser
driver.quit()
