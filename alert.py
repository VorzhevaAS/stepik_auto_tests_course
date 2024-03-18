import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")
try:
    # Нажатие на кнопку
    button = browser.find_element(By. TAG_NAME, "button")
    button.click()

    # Переключение на alert и принятие его
    confirm = browser.switch_to.alert
    confirm.accept()

    # Получение значения x и вычисление y
    x_element = browser.find_element(By.ID,"input_value")
    x = x_element.text
    y = calc(x)

    # Ввод ответа в текстовое поле и отправка формы
    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)

    submit_button = browser.find_element(By.TAG_NAME,"button")
    submit_button.click()

finally:
    # Пауза для визуальной проверки результата
    time.sleep(15)
    browser.quit()
