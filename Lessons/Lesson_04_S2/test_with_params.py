import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def test_open_google(driver):
    # Открытие сайта
    driver.get("https://www.google.com")

    # Проверка заголовка страницы
    assert "Google" in driver.title

def test_open_example(driver):
    # Открытие другого сайта
    driver.get("https://www.example.com")

    # Поиск заголовка
    heading = driver.find_element(By.TAG_NAME, "h1").text
    assert heading == "Example Domain"


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif request.param == "firefox":
        from selenium.webdriver.firefox.service import Service as FirefoxService
        from webdriver_manager.firefox import GeckoDriverManager
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    yield driver
    driver.quit()