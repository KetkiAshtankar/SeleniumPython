from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")

# Initialize Chrome WebDriver in headless mode
driver = webdriver.Chrome(options=chrome_options)

# Open Google
driver.get("https://www.google.com")

# Print success message
print("Headless browser opened Google successfully.")

# Close the browser
driver.quit()


