from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# defining the browser
browser = webdriver.Chrome()
try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser.get(link)
    # image search
    image_element = browser.find_element(By.ID, "treasure")
    valuex = image_element.get_attribute("valuex")
    # calculate the value by function
    calc_x = calc(valuex)
    # enter the answer in the text field
    answer_element = browser.find_element(By.ID, "answer")
    answer_element.send_keys(calc_x)
    # mark the checkbox
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()
    # select radiobutton
    robotRule_radioButton = browser.find_element(By.ID, "robotsRule")
    robotRule_radioButton.click()
    # click on the Submit button
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    # wait 10
    time.sleep(10)
    # close browser
    browser.quit()