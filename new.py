from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver with implicit wait
driver = webdriver.Chrome()
driver.implicitly_wait(10)  # Implicit wait set to 10 seconds

# Maximize the window
driver.maximize_window()

# Navigate to SauceDemo website
driver.get("https://www.saucedemo.com")

try:
    # Login
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button.click()

    print("Successfully logged in!")

    # Add an item to the cart
    add_to_cart_button = driver.find_element(By.XPATH, "//button[text()='Add to cart']")
    add_to_cart_button.click()

    # Wait for the cart icon to update with the item count
    cart_badge = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//span[@class='shopping_cart_badge']"), "1"))

    # Proceed to checkout
    checkout_button = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
    checkout_button.click()

    print("Successfully added item to cart and proceeded to checkout!")

finally:
    # Close the browser
    driver.quit()
