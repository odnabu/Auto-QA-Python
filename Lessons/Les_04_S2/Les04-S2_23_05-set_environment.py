# Skrebnev Fedor
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
""" ################################################################################################################
 23.05.25
 Python - Auto QA 04:  Summary 2 - Настройка окружения.
 ################################################################################################################### """

# ------------------------ SHORTCUTS ------------------------
# Ctrl + W - выделить текущий блок. если нажимать это сочетание дальше, то будут выделяться родительские блоки.
# Ctrl+Y - Удаление всей строки. Кстати, команда копирования Ctrl+C без выделения также работает для всей строки.
# Ctrl+Akt+L / Alt+Enter - Привести код к принятым стандартам (для Python - PEP8).
# Ctrl+R — Изменить название класса/функции и т. п. по всему проекту.
# Ctrl+Shift + F - Найти по всем файлам.
# Shift + F6 - заменить имя элемента во всех частях во всех файлах.
# -----------------------------------------------------------

print('.' * 80)




""" ___________________________________  Review of previously covered material  ___________________________________ """


""" ______ Открытие браузера: ______ """

# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# # Инициализация драйвера
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#
# # Открытие страниц
# driver.get("https://itcareerhub.de/ru/")  # Открывается первая страница
# driver.get("https://www.berlin.de/")      # Переход на вторую страницу
#
# # Изменение размера окна
# driver.set_window_size(640, 460)
#
# # Задержка перед скриншотом ________ NB! __________
# sleep(10)
#
# # Сохранение скриншота
# driver.save_screenshot("./berlin_screenshot.png")  # Сохранение скриншота в текущую папку
#
# # Закрытие драйвера
# driver.quit()


""" ______ Открытие НЕСКОЛЬКИХ браузеров: ______ """






""" ______ Открытие НЕСКОЛЬКИХ страниц: ______ """

# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
#
# def test_open_google(driver):
#     # Открытие сайта
#     driver.get("https://www.google.com")
#
#     # Проверка заголовка страницы
#     assert "Google" in driver.title
#
# def test_open_example(driver):
#     # Открытие другого сайта
#     driver.get("https://www.example.com")
#
#     # Поиск заголовка
#     heading = driver.find_element(By.TAG_NAME, "h1").text
#     assert heading == "Example Domain"
#
#
# @pytest.fixture(params=["chrome", "firefox"])
# def driver(request):
#     if request.param == "chrome":
#         driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     elif request.param == "firefox":
#         from selenium.webdriver.firefox.service import Service as FirefoxService
#         from webdriver_manager.firefox import GeckoDriverManager
#         driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
#     yield driver
#     driver.quit()



""" ______ Скриншот ______ """

# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# # Инициализация драйвера
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#
# # Открытие страниц
# driver.get("https://itcareerhub.de/ru/")  # Открывается первая страница
# driver.get("https://www.berlin.de/")      # Переход на вторую страницу
#
# # Изменение размера окна
# driver.set_window_size(640, 460)
#
# # Задержка перед скриншотом
# sleep(10)
#
# # Сохранение скриншота
# driver.save_screenshot("./berlin_screenshot.png")  # Сохранение скриншота в текущую папку
#
# # Закрытие драйвера
# driver.quit()


""" ______ Метод click() ______ """

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# # Настройка драйвера
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#
# try:
#     # Открытие страницы
#     driver.get("https://itcareerhub.de/ru")
#
#     # Задержка для загрузки страницы
#     sleep(3)
#
#     # Поиск ссылки "О нас" и клик
#     about_link = driver.find_element(By.LINK_TEXT, "О нас")
#     about_link.click()
#
#     # Задержка для проверки перехода
#     sleep(5)
# finally:
#     # Закрытие браузера
#     driver.quit()







""" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%___________   ---   __________%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% """

""" __________ --- __________ """

""" __________ --- __________ """
#       ●
# ___ EXAMPLE __________________________________________________
# ___ END of Example __________________________________________________


""" ______  Task 1  ______________________________________________________________________________________________ """
#



