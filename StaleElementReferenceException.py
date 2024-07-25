from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

driver = webdriver.Chrome()
driver.get("https://www.google.com")

try:
    # Find an element that might be dynamic (search input)
    search_input = driver.find_element(By.NAME, "q")

    # Simulate a dynamic change (e.g., page refresh)
    driver.refresh()  # This will cause the search input element to become stale
    
    # #Wait for the element to be clickable after the refresh
    # search_input = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.NAME, "q"))
    # )

    # Interact with the element after ensuring it's ready
    search_input.send_keys("Selenium Exceptions")

except StaleElementReferenceException as e:
    print("Stale element encountered as expected:", e)
finally:
    driver.quit()
