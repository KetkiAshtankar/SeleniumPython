import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
# Initialize Chrome WebDriver
driver = webdriver.Chrome()
# Open Google
driver.get("https://www.google.com")
time.sleep(3)
# Click on the first image
image = driver.find_element(By.CLASS_NAME, "lnXdpd")
ActionChains(driver).move_to_element(image).context_click().perform()
# Wait for the context menu to appear
time.sleep(3)
# Use PyAutoGUI to handle the "Save image as..." option in the context menu
pyautogui.typewrite(['down', 'down', 'enter'])  # Navigate down to "Save image as..."
time.sleep(3)
pyautogui.press('enter')  # Hit enter to select "Save image as..."
# Handle the save dialog using PyAutoGUI
time.sleep(1)
pyautogui.typewrite(['enter'])  # Confirm the save action by hitting enter
# Close the browser
driver.quit()
driver.find_element(By.XPATH)