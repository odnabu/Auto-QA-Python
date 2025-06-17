import pytest
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# link where we are: https://suninjuly.github.io/math.html

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

def test_math_form(browser):
    url = "https://suninjuly.github.io/math.html"
    browser.get(url)

    #Решение
    # Расчет значения по случайно сгенерированному числу:
    value = browser.find_element(By.ID, "input_value").text
    result = calc(value)

    # Поле введения результата расчета:
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(result)

    # Проверка, что я не робот:
    robot_box = browser.find_element(By.ID, "robotCheckbox")
    robot_box.click()

    # Переключатель в robotsRule:
    robots_rule_btn = browser.find_element(By.ID, "robotsRule")
    robots_rule_btn.click()

    # Кнопка отправки ответа:
    submit_button = browser.find_element(By.CLASS_NAME, "btn-default")
    submit_button.click()

    # Запуск проверки:
    wait = WebDriverWait(browser, 10)
    alert = wait.until(EC.alert_is_present())
    alert_text = Alert(browser).text

    expected_substring = "Congrats, you've passed the task!"
    assert expected_substring in alert_text, f"Ожидаемая строка '{expected_substring}' отсутствует в alert: '{alert_text}'"

    alert.accept()
