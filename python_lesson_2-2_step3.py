from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "http://suninjuly.github.io/selects1.html"
    #link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x,y):
          return str(x+y)

    x_element = browser.find_element_by_id("num1")
    time.sleep(2)
    y_element = browser.find_element_by_id("num2")
    x = x_element.get_attribute("textContent")
    y = y_element.get_attribute("textContent")
    print(x)
    print(y)
    element_answer = (int(x) + int(y))
    print(element_answer)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(element_answer))

    # Отправляем заполненную форму
    button = browser.find_element_by_tag_name("button")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()