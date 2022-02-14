from selenium import webdriver
import time


try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/wait1.html")
    time.sleep(2)
    button = browser.find_element_by_id("verify")
    button.click()
    time.sleep(2)

    message = browser.find_element_by_id("verify_message")
   
    assert "successful" in message.text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()