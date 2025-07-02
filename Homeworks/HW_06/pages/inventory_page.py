from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_items(self):
        return self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))

    def get_items_amount(self):
        return len(self.get_items())

    def all_items_are_displayed(self):
        return all(item.is_displayed() for item in self.get_items())

    def get_item_names(self):
        return [item.text for item in self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name")))]

    def all_items_names_are_displayed(self):
        return all(name.strip() != "" for name in self.get_item_names())

    def all_item_names_are_not_empty(self):
        return all(bool(name.strip()) for name in self.get_item_names())

    def all_item_names_contains_sauce_labs(self):
        return all(name.startswith("Sauce Labs") for name in self.get_item_names())

    def add_item_to_cart(self, item_name):
        """ Добавляет товар в корзину по названию """
        button_xpath = f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button"
        self.wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath))).click()

    def go_to_cart(self):
        """ Переход в корзину """

        # Проверка, что точно на inventory-странице:
        # print(f"\n\033[31m\tТекущий URL перед переходом в корзину:\033[m", self.driver.current_url)

        # self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()

        # Лучше реализовать так:
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        # Ожидание, пока URL станет адресом корзины:
        WebDriverWait(self.driver, 10).until(EC.url_contains("/cart.html"))

