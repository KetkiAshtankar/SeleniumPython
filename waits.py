from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome WebDriver with implicit wait
driver = webdriver.Chrome()
driver.implicitly_wait(10)  # Set implicit wait to 10 seconds

# Navigate to the saucedemo website
driver.get("https://www.saucedemo.com/")

# Find the username and password fields, and login button
username_input = driver.find_element(By.ID, "user-name")
password_input = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

# Enter username and password, then click login
username_input.send_keys("standard_user")
password_input.send_keys("secret_sauce")
login_button.click()

# Add an item to the cart
add_to_cart_button = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
add_to_cart_button.click()

# Click on the shopping cart icon
shopping_cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
shopping_cart_icon.click()

# Wait for the checkout button to be clickable
checkout_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Checkout']"))
)
checkout_button.click()

# Wait for the name input field to be visible
name_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "first-name"))
)
# Wait for the last name input field to be visible
last_name_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "last-name"))
)
# Wait for the postal code input field to be visible
postal_code_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "postal-code"))
)

# Enter name, last name, and postal code
name_input.send_keys("John")
last_name_input.send_keys("Doe")
postal_code_input.send_keys("12345")

# Click on the continue button
continue_button = driver.find_element(By.XPATH, "//input[@value='Continue']")
continue_button.click()

# Fluent wait to verify the item in the cart
# fluent_wait = WebDriverWait(driver, 10)
# item_in_cart = fluent_wait.until(
#     lambda driver: driver.find_element(By.CLASS_NAME, "inventory_item_name").text
# )
# assert item_in_cart == "Sauce Labs Backpack"



# Define FluentWait object with maximum timeout of 10 seconds and polling interval of 1 second
fluent_wait = WebDriverWait(driver, 10, poll_frequency=1)

# Define the condition to wait for the element with class name "inventory_item_name" to be visible
item_in_cart = fluent_wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))
)

# Once the element is visible, get its text
item_text = item_in_cart.text

# Perform assertion
assert item_text == "Sauce Labs Backpack"


# Click on the finish button
finish_button = driver.find_element(By.XPATH, "//button[text()='Finish']")
finish_button.click()

# Click on the back to home button
back_to_home_button = driver.find_element(By.XPATH, "//button[text()='Back Home']")
back_to_home_button.click()

# Close the browser
driver.quit()
