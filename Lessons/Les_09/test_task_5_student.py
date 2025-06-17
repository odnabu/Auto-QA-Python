import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Фикстура для WebDriver
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# Тест загрузки файла
def test_file_upload(browser):
    url = "http://suninjuly.github.io/file_input.html"
    browser.get(url)

    # Заполняем форму
    browser.find_element(By.NAME, "firstname").send_keys("John")
    browser.find_element(By.NAME, "lastname").send_keys("Doe")
    browser.find_element(By.NAME, "email").send_keys("test@example.com")

    # Создаем временный текстовый файл
    file_path = os.path.abspath("test_file.txt")
    with open(file_path, "w") as f:
        f.write("Hello, this is a test file.")

    #Решение
    # Загрузка файла
    file_download = browser.find_element(By.ID, "file")
    file_download.send_keys(file_path)


    # Нажимаем Submit
    browser.find_element(By.CLASS_NAME, "btn-primary").click()

    # Ожидаем появление Alert
    wait = WebDriverWait(browser, 10 )
    alert = wait.until(EC.alert_is_present())

    # Проверяем текст в Alert
    alert_text = Alert(browser).text
    expected_text = "Congrats, you've passed the task!"
    assert expected_text in alert_text, f"Ожидаемая строка '{expected_text}' отсутствует в alert: '{alert_text}'"

    # Закрываем Alert
    alert.accept()

    # Удаляем тестовый файл
    os.remove(file_path)
