from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    wait_for_rent_price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    x_elem = browser.find_element(By.ID, "input_value").text

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    y = calc(x_elem)

    answer_field = browser.find_element(By.ID, 'answer')
    answer_field.send_keys(y)

    new_button = browser.find_element(By.ID, "solve")
    new_button.click()

    
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()