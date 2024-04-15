from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("https://practice.expandtesting.com/dynamic-table")

# Find all the elements in the table using XPath
table_elements = driver.find_elements(By.XPATH, "//table[@class='table table-striped']/tbody/tr/td")

# Loop through the elements and print their text content
for element in table_elements:
    print(element.text)

# Close the browser
driver.quit()
