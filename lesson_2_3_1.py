from selenium import webdriver
from selenium.webdriver.common.by import By
from math import log
from math import sin
import time

# defining the browser
browser = webdriver.Chrome()
try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    # looking for a button
    button_alert = browser.find_element(By.XPATH, "//button[text()='I want to go on a magical journey!']")
    button_alert.click()
    # accept confirm
    confirm = browser.switch_to.alert
    confirm.accept()
    # get input value
    value_x = browser.find_element(By.ID, "input_value")
    x = int(value_x.text)

    print(x)

    formula = browser.find_element(By.CSS_SELECTOR, ".container .form-group .nowrap")

    print(formula.text)

    index_sl = formula.text.index(',')
    formula_str = formula.text[8:index_sl].replace('ln', 'log')

    result_value = str(eval(formula_str))
    # looking for an input element
    input = browser.find_element(By.ID, "answer")
    input.send_keys(result_value)

    # click on the Submit button
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    # wait 10
    time.sleep(10)
    # close browser
    browser.quit()