from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open the website
driver.get("https://practice.expandtesting.com/cookie-alert")

# Wait for the cookie popup to appear (handling potential timeout)
wait = WebDriverWait(driver, 10)
cookie_popup = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='js-cookie-box']")))

# Find and click the accept button (assuming it's always present)
cookie_popup.find_element(By.XPATH, "//button[contains(text(), 'Accept')]").click()

print("Popup closed successfully.")  


driver.quit()

