import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage

@pytest.fixture(scope="class")
def driver(request):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.mark.usefixtures("driver")
class TestLogin:
    def test_successful_login(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_on_login_button()
        assert "inventory.html" in self.driver.current_url, "Не удалось войти в систему."

    def test_invalid_password(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("standard_user")
        login_page.enter_password("wrong_password")
        login_page.click_on_login_button()
        assert "Epic sadface: Username and password do not match any user in this service" in login_page.error_message().text, "Неверное сообщение об ошибке."

    def test_locked_out_user(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("locked_out_user")
        login_page.enter_password("secret_sauce")
        login_page.click_on_login_button()
        assert "Sorry, this user has been locked out." in login_page.error_message().text, "Неверное сообщение об ошибке."

    def test_empty_username(self):
        login_page = LoginPage(self.driver)
        login_page.enter_password("secret_sauce")
        login_page.click_on_login_button()
        assert "Username is required" in login_page.error_message().text, "Неверное сообщение об ошибке."
