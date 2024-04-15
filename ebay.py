import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

url = "https://www.ebay.com/"
driver.get(url)

# #click on shop by category
driver.find_element(By.XPATH, '//*[@id="gh-shop-a"]').click()
time.sleep(2)
# #click on shoes
driver.find_element(By.XPATH, "//a[contains(text(),'Shoes')]").click()

women_shoe_elements = driver.find_elements(By.XPATH,'//div[@class="b-visualnav__grid"]/span')
for element in women_shoe_elements:
    if "women" in element.text.lower():  # Case-insensitive check for "women"
        print(element.text)
