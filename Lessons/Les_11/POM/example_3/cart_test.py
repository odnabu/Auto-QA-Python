import pytest
from base_tests import BaseTest  # Импорт базового тестового класса

class TestInventory(BaseTest):

    def test_items_amount(self):
        self.login_page.success_login("standard_user", "secret_sauce")
        assert self.inventory_page.get_items_amount() == 6, "Количество товаров не совпадает."

    def test_backpack_cost(self):
        self.login_page.success_login("standard_user", "secret_sauce")

        # Запоминаем цену товара "Backpack"
        backpack_price = self.inventory_page.get_item_price("Sauce Labs Backpack")
        # Добавляем товар в корзину
        self.inventory_page.add_item_to_cart("Sauce Labs Backpack")

        # Переходим в корзину
        self.inventory_page.go_to_cart()

        # Проверяем цену в корзине
        cart_price = self.cart_page.get_cart_item_price("Sauce Labs Backpack")
        assert backpack_price == cart_price, "Цена товара в корзине не совпадает с ценой на странице инвентаря."
