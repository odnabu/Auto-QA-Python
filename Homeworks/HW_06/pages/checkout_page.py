from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Ожидание до 10 секунд

    # XPath полей ввода данных: 
    first_name_field = '//*[@id="first-name"]'
    last_name_field = '//*[@id="last-name"]'
    zip_postal_code_field = '//*[@id="postal-code"]'
    # XPath кнопки Continue:
    continue_button = '//*[@id="continue"]'


    def put_first_name(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, self.first_name_field)))

    def put_last_name(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, self.last_name_field)))

    def put_zip_postal_code(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, self.zip_postal_code_field)))

    def enter_first_name(self, first_name):
        first_name_field = self.put_first_name()
        first_name_field.send_keys(first_name)

    def enter_last_name(self, last_name):
        last_name_field = self.put_last_name()
        # last_name_field.clear()
        last_name_field.send_keys(last_name)

    def enter_zip_postal_code(self, zip_postal_code):
        zip_postal_code_field = self.put_zip_postal_code()
        zip_postal_code_field.send_keys(zip_postal_code)


    def fill_checkout_form(self, first_name, last_name, zip_postal_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_zip_postal_code(zip_postal_code)

    def get_continue_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    def click_on_continue_button(self):
        self.get_continue_button().click()

    def get_total_price(self):
        """ Получает итоговую стоимость выбранных товаров (в формате строки с $) """
        return self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))).text
