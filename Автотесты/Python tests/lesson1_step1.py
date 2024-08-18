import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



try:
    link = 'https://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    x_element = browser.find_element(By.CSS_SELECTOR, '.form-group label span:nth-child(2)')
    x = x_element.text
    y = calc(x)

    answer_field = browser.find_element(By.ID, 'answer')
    answer_field.send_keys(y)

    checkbox1 = browser.find_element(By.ID, 'robotCheckbox')
    checkbox1.click()

    radio_button1 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    radio_button1.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()