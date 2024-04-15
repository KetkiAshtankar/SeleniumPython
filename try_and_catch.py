from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    # Initialize WebDriver
    driver = webdriver.Chrome()
    # Navigate to the webpage
    driver.get("https://practice.expandtesting.com/dynamic-table")

    # Find and store the CPU load value for Chrome from the table
    # chrome_cpu_table_element = driver.find_element(By.XPATH, "//td[text()='Chrome']/following-sibling::td[1]")
    chrome_cpu_table_element = driver.find_element(By.XPATH, "//td[text()='Chrome']/following-sibling::td[1]")
    chrome_cpu_table_text = chrome_cpu_table_element.text

    # Find and store the value in the yellow label
    yellow_label_element = driver.find_element(By.XPATH, "//p[contains(text(), 'Chrome CPU')]")
    yellow_label_text = yellow_label_element.text.split(":")[1].strip()

    # Compare CPU load value from table with value in the yellow label
    if chrome_cpu_table_text == yellow_label_text:
        print("Test Passed: CPU load value from table matches the value in the yellow label.")
    else:
        print("Test Failed: CPU load value from table does not match the value in the yellow label. Table value:", chrome_cpu_table_text, "Yellow label value:", yellow_label_text)

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the browser
    driver.quit()
