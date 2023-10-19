from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# get file path
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

# defining the browser
browser = webdriver.Chrome()
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    # enter the values in the input fields
    input_fn = browser.find_element(By.NAME, "firstname")
    input_fn.send_keys("VALERII")
    input_ln = browser.find_element(By.NAME, "lastname")
    input_ln.send_keys("VALERII")
    input_em = browser.find_element(By.NAME, "email")
    input_em.send_keys("valerii@mail.ru")
    # get element file download
    input_file_download = browser.find_element(By.ID, "file")
    input_file_download.send_keys(file_path)

    # click on the Submit button
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    # wait 10
    time.sleep(10)
    # close browser
    browser.quit()