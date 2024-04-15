import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains


# Set the default download directory
download_dir = "C://Users//ketki.ashtankar//Desktop//Notes"
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "plugins.always_open_pdf_externally": True,
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,  # Disable prompt for download
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

# Initialize Chrome WebDriver with options
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

# Open the website
driver.get("https://labour.gov.in/")

# Click on "Monthly Progress Report" link
try:
    # Hover over "Documents" menu
    documents = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Documents']"))
    )
    ActionChains(driver).move_to_element(documents).perform()

    # Click on "Monthly Progress Report" link
    monthly_progress_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"Monthly Progress Report")]'))
    )
    monthly_progress_link.click()

    # Click on the download link for a specific report (adjust as needed)
    download_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//td[contains(text(),"December-2023")]/following::a[1]'))
    )
    download_link.click()

    # Wait for the download to complete
    time.sleep(10)  # Adjust the waiting time based on the download speed
except TimeoutException as e:
    print("Timeout occurred while waiting for element:", e)

# Close the browser window
driver.quit()
