from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# Инициализация драйвера
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Открытие страниц
driver.get("https://itcareerhub.de/ru/")  # Открывается первая страница
driver.get("https://www.berlin.de/")      # Переход на вторую страницу

# Изменение размера окна
driver.set_window_size(640, 460)

# Задержка перед скриншотом
sleep(10)

# Сохранение скриншота
driver.save_screenshot("./berlin_screenshot.png")  # Сохранение скриншота в текущую папку

# Закрытие драйвера
driver.quit()