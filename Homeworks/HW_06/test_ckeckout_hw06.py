# import pytest
# from pages.login_page import LoginPage
# from pages.inventory_page import InventoryPage
# from pages.cart_page import CartPage
# from pages.checkout_page import CheckoutPage

import time

from base_tests import BaseTest  # Импорт базового тестового класса


class TestCheckout(BaseTest):

    # @pytest.fixture(scope="class", autouse=True)
    # def setup(self, driver):
    #     self.driver = driver
    #     self.login_page = LoginPage(driver)
    #     self.inventory_page = InventoryPage(driver)
    #     self.cart_page = CartPage(driver)
    #     self.checkout_page = CheckoutPage(driver)


    def test_checkout_total_price(self):

        # 1. Открытие сайта и авторизация
        self.login_page.open()
        self.login_page.success_login("standard_user", "secret_sauce")

        # ---------------------------------------------------------------------
        # Чтобы проверить, что это за сервисное окно в Хром и отключить его:
        # time.sleep(10)
        # Этого окна нет в DOM!!!!!
        # ---------------------------------------------------------------------

        # 2. Добавление товаров в корзину
        self.inventory_page.add_item_to_cart("Sauce Labs Backpack")
        self.inventory_page.add_item_to_cart("Sauce Labs Bolt T-Shirt")
        self.inventory_page.add_item_to_cart("Sauce Labs Onesie")

        # 3. Переход в корзину
        self.inventory_page.go_to_cart()

        # 4. Оформление заказа
        # Для ОТЛАДКИ: проверка, что произошел переход в корзину должным образом (клик сработал):
        # print(f"\n\033[31m\tТекущий URL:\033[m", self.driver.current_url)

        self.cart_page.proceed_to_checkout()
        self.checkout_page.fill_checkout_form("John", "Doe", "12345")
        self.checkout_page.click_on_continue_button()

        # 5. Проверка итоговой стоимости
        # total_price = self.checkout_page.get_total_price()            # Так не достаточно. Нужно уточнять
        # print(f"\n\tВывод Итоговой суммы по примеру решения в Саммари 6: \033[31m{total_price}\033[m")
        # assert total_price == "$58.29", f"Итоговая сумма неверна: {total_price}"

        total_text = self.checkout_page.get_total_price()  # 'Total: $58.29'
        total_amount = total_text.split(":")[-1].strip()  # → '$58.29'
        print(f"\n\tResult of Home Work: Total = \033[31m{total_amount}\033[m")
        assert total_amount == "$58.29", f"Итоговая сумма неверна: {total_text}"

        print(f"\tHome Work successfully done.", '\n', '=' * 50)


