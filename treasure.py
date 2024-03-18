import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/get_attribute.html")

try:
    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

    button = browser.find_element(By.XPATH, "/html/body/div/form/div/div/button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
