from selenium.webdriver.common.by import By
from selenium import webdriver
import time
# # Initialize Chrome WebDriver
driver = webdriver.Chrome()
# # Open the first website (https://www.saucedemo.com)
driver.get("https://www.saucedemo.com")
# # Open a new window/tab with Google
driver.execute_script("window.open('https://www.google.com')")
# # Get handles of all the open windows
window_handles = driver.window_handles
# Switch to the Google window
google_window_handle = None
for handle in window_handles:
    if handle != driver.current_window_handle:
        google_window_handle = handle
        break
driver.switch_to.window(google_window_handle)
time.sleep(5)
# # Perform actions on the Google page (optional). For example, you can perform a search: # search_input = driver.find_element_by_name("q")
search_input = driver.find_element(By.NAME, "q")
search_input.send_keys("Selenium Python")
search_input.submit()
# # Wait for demonstration purposes
time.sleep(2)
# Switch back to the original window (https://www.saucedemo.com)
driver.switch_to.window(window_handles[0])
# Perform actions on the original page (optional)# # For example, you can log in:
username_input = driver.find_element(By.ID, "user-name")
password_input = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")
username_input.send_keys("standard_user")
password_input.send_keys("secret_sauce")
login_button.click()
# # Wait for demonstration purposes
time.sleep(2)
# # Close the browser
driver.quit()
