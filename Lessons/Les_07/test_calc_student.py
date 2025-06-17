# Les07-Auto QA_LfS4.pdf, slide. 99 |-->
# Создайте файл test_calc.py и добавьте в  него автотест с шагами:
# 1. Откройте страницу Slow Calculator.
# 2. В поле ввода по локатору #delay введите значение 45.
# 3. Нажмите на кнопки (в указанном порядке):
# ● 7
# ● +
# ● 8
# ● =
# 4. Проверьте (assert), что в окне отображается результат 15 через 45 секунд.


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v135.debugger import resume
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()

def test_slow_calculator(driver):
    wait = WebDriverWait(driver, 30)  # Ожидание результата

    # решение:
    value = "10"
    delay_input = driver.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys(value)

    assert delay_input, value
    # assert delay_input.text == value      # ---> НЕ работает.
    # time.sleep(4)

    # Теперь тестирование кнопок на калкуляторе:
    #     /html/body/main/div/div[4]/div/div/div[2]/span[1]
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    result = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

    assert result, "failed"



