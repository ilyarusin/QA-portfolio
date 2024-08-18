
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    input_name = browser.find_element(By.NAME, "firstname")
    input_name.send_keys("Ivan")
    input_last_name = browser.find_element(By.NAME, "lastname")
    input_last_name.send_keys("Petrov")
    input_email = browser.find_element(By.NAME, "email")
    input_email.send_keys("example@mail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'text.txt')

    file_loading_button = browser.find_element(By.ID, "file")
    file_loading_button.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()