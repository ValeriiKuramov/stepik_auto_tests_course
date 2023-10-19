from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# defining the browser
browser = webdriver.Chrome()
try:
    link = "https://suninjuly.github.io/selects1.html"
    browser.get(link)

    # calculate the sum of the numbers
    span_element_1 = browser.find_element(By.ID, "num1")
    span_element_2 = browser.find_element(By.ID, "num2")
    sum_element = 0
    try:
        sum_element = int(span_element_1.text) + int(span_element_2.text)
    except:
        pass

    # select search
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum_element))

    #for option in select.options:
    #    try:
    #        value_option = int(option.get_attribute('innerHTML'))
    #    except:
    #        continue
    #    sum_element = sum_element + value_option

    # click on the Submit button
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    # wait 10
    time.sleep(10)
    # close browser
    browser.quit()