import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = 'http://suninjuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x_elem = browser.find_element(By.ID, "input_value").text

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    y = calc(x_elem)

    answer_field = browser.find_element(By.ID, 'answer')
    answer_field.send_keys(y)

    checkbox1 = browser.find_element(By.ID, 'robotCheckbox')
    checkbox1.click()

    browser.execute_script("window.scrollBy(0, 100);")

    radio_button1 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    radio_button1.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()