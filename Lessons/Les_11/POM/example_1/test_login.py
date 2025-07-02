import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# Тесты теперь вызывают методы LoginPage, а не ищут локаторы вручную:
from pages.login_page import LoginPage


# Тесты структурированы по Page Object Model, что делает их более удобными для поддержки.
# При изменении локаторов их нужно обновить только в одном месте – в LoginPage,
# а тесты останутся неизменными.

@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_on_login_button()
    assert "inventory.html" in driver.current_url, "Не удалось войти в систему."

def test_invalid_password(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("wrong_password")
    login_page.click_on_login_button()
    assert "Epic sadface: Username and password do not match any user in this service" in login_page.error_message().text, "Неверное сообщение об ошибке."

def test_locked_out_user(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("locked_out_user")
    login_page.enter_password("secret_sauce")
    login_page.click_on_login_button()
    assert "Sorry, this user has been locked out." in login_page.error_message().text, "Неверное сообщение об ошибке."

def test_empty_username(driver):
    login_page = LoginPage(driver)
    login_page.enter_password("secret_sauce")
    login_page.click_on_login_button()
    assert "Username is required" in login_page.error_message().text, "Неверное сообщение об ошибке."

