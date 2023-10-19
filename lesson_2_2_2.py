from selenium import webdriver
from selenium.webdriver.common.by import By
from math import log
from math import sin
import math
import time

# defining the browser
browser = webdriver.Chrome()
try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    # get input value
    value_x = browser.find_element(By.ID, "input_value")
    x = int(value_x.text)
    formula = browser.find_element(By.CSS_SELECTOR, ".form-group .nowrap")
    index_sl = formula.text.index(',')
    formula_str = formula.text[8:index_sl].replace('ln','log')
    result_value = str(eval(formula_str))
    # scroll down the page
    browser.execute_script("window.scrollBy(0, 200);")
    # looking for an input element
    input = browser.find_element(By.ID, "answer")
    input.send_keys(result_value)
    # mark the checkbox
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()
    # select radiobutton
    robotRule_radioButton = browser.find_element(By.ID, "robotsRule")
    robotRule_radioButton.click()
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

