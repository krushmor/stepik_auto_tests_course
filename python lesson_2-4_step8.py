from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time, math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    def calc(x):
          return str(math.log(abs(12*math.sin(int(x)))))

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    button = browser.find_element_by_id("book")
    button.click()

    x = browser.find_element_by_id("input_value").get_attribute("textContent")
    y = calc(x)

    y_answer = browser.find_element_by_id("answer")
    y_answer.send_keys(y)

    # Отправляем заполненную форму
    button1 = browser.find_element_by_id("solve")
    button1.click()
    

finally:
    time.sleep(10)

    browser.quit()