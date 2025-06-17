import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_fill_form_and_check_alert(browser):
    url = "http://suninjuly.github.io/huge_form.html"
    browser.get(url)

    input_fields = browser.find_elements(By.TAG_NAME, "input")
    for field in input_fields:
        field.clear()
        field.send_keys("Hello")

    submit_button = browser.find_element(By.CLASS_NAME, "btn-default")
    submit_button.click()
    time.sleep(3)

    wait = WebDriverWait(browser, 10)
    time.sleep(3)

    alert = wait.until(EC.alert_is_present())
    alert_text = Alert(browser).text
    time.sleep(3)

    expected_substring = "Congrats, you've passed the task!"
    assert expected_substring in alert_text, f"Ожидаемая строка '{expected_substring}' отсутствует в alert: '{alert_text}'"

    alert.accept()