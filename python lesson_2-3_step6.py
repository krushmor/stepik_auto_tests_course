from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

    button = browser.find_element_by_tag_name("button")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_id("input_value").get_attribute("textContent")
    y = calc(x)

    y_answer = browser.find_element_by_id("answer")
    y_answer.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_tag_name("button")
    button.click()

    time.sleep(4)

    alert = browser.switch_to.alert
    alert.accept()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()