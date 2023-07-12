from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# Шаг 1: Открыть страницу
browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/math.html")

try:
    # Шаг 2: Считать значение для переменной x
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = int(x_element.text)

    # Шаг 3: Вычислить математическую функцию от x
    result = math.log(abs(12*math.sin(x)))

    # Шаг 4: Ввести ответ в текстовое поле
    answer_input = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_input.send_keys(str(result))

    # Шаг 5: Отметить checkbox "I'm the robot"
    robot_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    robot_checkbox.click()

    # Шаг 6: Выбрать radiobutton "Robots rule!"
    robots_rule_radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    robots_rule_radiobutton.click()

    # Шаг 7: Нажать на кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit_button.click()

finally:
    # Закрыть браузер после выполнения всех шагов
    time.sleep(10)
    browser.quit()
