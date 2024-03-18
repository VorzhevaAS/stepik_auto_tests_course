import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


def sum(x, y):
    return str(int(x) + int(y))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")

try:
    x_element = browser.find_element(By.ID, "num1")
    y_element = browser.find_element(By.ID, "num2")
    x = x_element.text
    y = y_element.text

    result = sum(x, y)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(result)

    button = browser.find_element(By.XPATH, "/html/body/div/form/button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
