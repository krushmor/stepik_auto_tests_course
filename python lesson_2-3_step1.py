from selenium import webdriver
import time

try:
    #link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    #browser.get(link)
    
    
    alert = browser.switch_to.alert
    alert.accept()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

