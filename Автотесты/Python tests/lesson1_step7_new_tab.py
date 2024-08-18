
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_elem = browser.find_element(By.ID, "input_value").text

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    y = calc(x_elem)

    answer_field = browser.find_element(By.ID, 'answer')
    answer_field.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    
    

finally:
    time.sleep(3)
    confirm = browser.switch_to.alert
    confirm.accept()
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()