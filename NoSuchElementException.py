from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def search_google_with_error(search_term, invalid_locator):
  """Searches Google with a potential NoSuchElementException."""
  driver = None
  try:
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()

    # Open Google homepage
    driver.get("https://www.google.com")

    # Find search input element using By.NAME (correct)
    search_input = driver.find_element(By.NAME, "q")

    # Send keys (search term)
    search_input.send_keys(search_term)

    # Try using an invalid locator (guaranteed to cause NoSuchElementException)
    invalid_element = driver.find_element(By.ID, invalid_locator)
    print("This line will cause an error (intended for demonstration).")
    invalid_element.click()  # This line will raise the exception

    # Submit the search (will not be reached due to the exception)
    search_input.submit()
    
  except NoSuchElementException as e:
    print("Error: Element not found using the invalid locator:", e)
  finally:
    if driver:
      driver.quit()  # Close the browser window even if exceptions occur
# Example usage
search_term = "Selenium Exceptions"
invalid_locator = "non_existent_element"  # This ID is guaranteed not to exist
search_google_with_error(search_term, invalid_locator)
print("Script execution completed (or exception handled).")
