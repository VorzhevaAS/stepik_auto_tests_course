import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
try:
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    # Нажатие на кнопку
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()

    # Получение значения x и вычисление y
    x_element = browser.find_element(By.ID,"input_value")
    x = x_element.text
    y = calc(x)

    # Ввод ответа в текстовое поле и отправка формы
    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)

    submit_button = browser.find_element(By.XPATH, "//*[@id='solve']")
    submit_button.click()

finally:
    # Пауза для визуальной проверки результата
    time.sleep(15)
    browser.quit()