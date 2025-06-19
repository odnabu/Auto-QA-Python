import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage


class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

        self.login_page = LoginPage(self.driver)
        self.inventory_page = InventoryPage(self.driver)
        self.cart_page = CartPage(self.driver)

        yield
        self.driver.quit()
