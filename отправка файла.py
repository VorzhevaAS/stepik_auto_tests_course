import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

try:
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Anastasiia")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Vorzheva")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("nastya-odinokova@mail.ru")

    # Определение пути к файлу
    current_dir = os.path.abspath(os.path.dirname("C:/Users/vorzh/OneDrive/Рабочий стол/bio.txt"))
    file_path = os.path.join(current_dir, "bio.txt")

    input4 = browser.find_element(By.ID, "file")
    input4.send_keys(file_path)

    button = browser.find_element(By.XPATH, "/html/body/div/form/button")
    button.click()

finally:
    # Пауза, чтобы увидеть результаты
    time.sleep(30)
    browser.quit()
