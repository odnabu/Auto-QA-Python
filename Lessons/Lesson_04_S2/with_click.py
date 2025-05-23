from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Настройка драйвера
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
try:
    # Открытие страницы
    driver.get("https://itcareerhub.de/ru")

    # Задержка для загрузки страницы
    sleep(3)

    # Поиск ссылки "О нас" и клик
    about_link = driver.find_element(By.LINK_TEXT, "О нас")
    about_link.click()

    # Задержка для проверки перехода
    sleep(5)
finally:

    # Закрытие браузера
    driver.quit()