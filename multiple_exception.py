from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

try:
    # Initialize WebDriver
    driver = webdriver.Chrome()

    # Navigate to the webpage
    driver.get("https://practice.expandtesting.com/dynamic-table")

    try:
        # Find all the elements in the table using XPath
        table_elements = driver.find_elements(By.XPATH, "//table[@class='table table-striped']/tbody/tr/td")

        # Loop through the elements and print their text content
        for element in table_elements:
            print(element.text)

    except NoSuchElementException as e:
        print("Element not found:", e)

    except TimeoutException as e:
        print("Timeout occurred:", e)

finally:
    # Close the browser
    driver.quit()
