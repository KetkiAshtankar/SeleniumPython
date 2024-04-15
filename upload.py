import os
from selenium import webdriver
from selenium.webdriver.common.by import By

image_path = "C:\\Users\\ketki.ashtankar\\Downloads\\abc.jpeg"
driver = webdriver.Chrome()


driver.get("https://practice.expandtesting.com/upload")

# Find the file input element
element = driver.find_element(By.ID, "fileInput")
element.send_keys(image_path)

upload_button= driver.find_element(By.ID, "fileSubmit").click()

uploaded_file_element = driver.find_element_by_xpath("//*[@id='uploaded-files']/p")
uploaded_file_element_text = uploaded_file_element.text

# Assert if 'abc' file is uploaded and displayed
assert "abc" in uploaded_file_element_text, "File 'abc' not uploaded and displayed"

# If assertion passes, print success message
print("File 'abc' uploaded and displayed successfully.")
driver.quit()