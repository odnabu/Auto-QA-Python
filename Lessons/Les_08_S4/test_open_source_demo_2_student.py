import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def driver():
    # Устанавливаем ChromeDriver через WebDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  # Открываем страницу
    yield driver
    driver.quit()  # Закрываем браузер после теста

def test_login_and_check_url(driver):
    wait = WebDriverWait(driver, 10)  # Явное ожидание до 10 секунд
    driver.implicitly_wait(10)

    # Вводим имя пользователя:
    user_name = driver.find_element(By.NAME, "username")
    user_name.send_keys("Admin")

    # Вводим пароль:
    user_password = driver.find_element(By.NAME, "password")
    user_password.send_keys("admin123")

    # Нажимаем кнопку Login:
    click = driver.find_element(By.XPATH, "//button[@type='submit']")
    click.click()

    # Ожидаем, пока URL изменится и будет содержать "dashboard":
    wait.until(EC.url_contains("dashboard"))
    # print(current_url)

    # Проверяем, что в URL содержится "dashboard"
    assert "dashboard" in driver.current_url, f"Ожидаемый URL не содержит 'dashboard': {driver.current_url}"