from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Specify the URL
url = "https://practice.expandtesting.com/dropdown"

# Initialize the WebDriver (assumes you have the appropriate driver installed, e.g., chromedriver)
driver = webdriver.Chrome()

# Navigate to the URL
driver.get(url)

# Wait for the dropdown element to be clickable
wait = WebDriverWait(driver, 10)
dropdown_element = wait.until(EC.element_to_be_clickable((By.ID, "country")))

# Select value from the dropdown
dropdown = Select(dropdown_element)
dropdown.select_by_value("DJ")  # Selects the option with value "IN" (assuming "IN" is the value for India)


# Close the browser
# driver.quit()
