from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import log
from math import sin
import time

# defining the browser
browser = webdriver.Chrome()
#browser.implicitly_wait(5)
try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
    # waiting for the value of $100
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element ((By.ID, "price"), '$100')
    )
    # click on the button "book"
    button_book = browser.find_element(By.ID, "book")
    button_book.click()
    #
    # get input value
    value_x = browser.find_element(By.ID, "input_value")
    x = int(value_x.text)
    formula = browser.find_element(By.CSS_SELECTOR, ".container .form-group .nowrap")
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