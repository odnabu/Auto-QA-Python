# НЕЯВНОЕ ОЖИДАНИЕ - глобальное ожидание.

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # Устанавливаем неявное ожидание
    yield driver
    driver.quit()

def test_example(driver):
    driver.get("https://example.com")

    wait = WebDriverWait(driver, 2)
    element = wait.until(EC.visibility_of_element_located((By.ID, "some_id")))
