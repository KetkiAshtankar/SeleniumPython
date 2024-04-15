from selenium import webdriver

# Initialize Chrome WebDriver
driver = webdriver.Chrome("C:\\Users\\ketki.ashtankar\\Documents\\chromedriver-win64 (2)\\chromedriver-win64\\chromedriver.exe")

# Navigate to Google homepage
driver.get("https://www.google.com")

# Close the browser
driver.quit()

