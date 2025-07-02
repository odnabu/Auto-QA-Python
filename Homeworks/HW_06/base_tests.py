# import time

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Для устранения проблемы системного всплывающего окна Google Chrome:
from selenium.webdriver.chrome.options import Options

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage



class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self):

        # ----------------------------------------------------------------------
        # К сожалению, этот метод НЕ ВСЕГДА срабатывает. Почему - я так и не поняла.
        # Для устранения проблемы системного всплывающего окна Google Chrome:
        chrome_options = Options()

        # Отключение предложения сохранить пароль и предупреждение о взломе:
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
        chrome_options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=chrome_options
        )
        # ----------------------------------------------------------------------

        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

        self.login_page = LoginPage(self.driver)
        self.inventory_page = InventoryPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)

        yield
        self.driver.quit()

        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver.maximize_window()
        # self.driver.get("https://www.saucedemo.com/")
        #
        # self.login_page = LoginPage(self.driver)
        # self.inventory_page = InventoryPage(self.driver)
        # self.cart_page = CartPage(self.driver)
        # self.checkout_page = CheckoutPage(self.driver)
        #
        # yield
        # self.driver.quit()
