from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# defining the browser
browser = webdriver.Chrome()
#browser.implicitly_wait(5)
try:
    link = "http://suninjuly.github.io/wait2.html"
    browser.get(link)

    #time.sleep(1)

    # looking for a button
    #button = browser.find_element(By.ID, "verify")
    #
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

finally:
    # wait 10
    time.sleep(10)
    # close browser
    browser.quit()