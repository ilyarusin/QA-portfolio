import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    first_digit = int(browser.find_element(By.CSS_SELECTOR, "span#num1").text)
    second_digit = int(browser.find_element(By.CSS_SELECTOR, "span#num2").text)
    sum_of_two_digits = first_digit + second_digit

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum_of_two_digits))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()