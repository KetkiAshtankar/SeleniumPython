from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Specify the URL
url = "https://practice.expandtesting.com/radio-buttons"

# Initialize the WebDriver 
driver = webdriver.Chrome()

# Navigate to the URL
driver.get(url)

# Wait for the radio buttons to be clickable
wait = WebDriverWait(driver, 10)
radio_button1 = wait.until(EC.element_to_be_clickable((By.ID, "blue")))
radio_button2 = wait.until(EC.element_to_be_clickable((By.ID, "red")))

# Click on the radio buttons
radio_button1.click()
radio_button2.click()

# Close the browser
driver.quit()
