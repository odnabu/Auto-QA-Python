# Skrebnev Fedor
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
""" ################################################################################################################
 30.05.25
 Python - Auto QA 05:  Lecture 5 - Автоматизация веб-тестов с использованием Selenide часть 1.
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


"""  __ NB! __"""       # See   Les05-Auto QA_3.pdf.


""" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%__________   SELECTOR  EXAMPLE   __________%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% """

# # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
# # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
# # https://suninjuly.github.io/cats.html
# # test-data="some-data"
#
# driver = webdriver.Chrome()
# driver.get("http://example.com")
#
# element = driver.find_element(By.TAG_NAME, "h1")
# print(element.text)
#
#
# try:
#     element = driver.find_element(By.ID, "non-existent")
#     print(f"\033[33mЭлемент найден\033[0m")
# except NoSuchElementException:
#     print(f"\033[34mЭлемент не найден\033[0m")
#
#
# driver.quit()


""" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%_____________   TESTS   _____________%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% """


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

@pytest.fixture(params=["chrome"])
def driver(request):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


# Задание 1
# Написать тест, который проверяет наличия теста “Cat memesˮ в заголовке страницы.

# def test_header_text(driver):
#     #Решение
#     driver.get("https://suninjuly.github.io/cats.html")
#     get_h1 = driver.find_element(By.TAG_NAME, "h1")
#     print(get_h1.text)
#     assert get_h1.text == "Cat memes"


# Задание 2
# Написать тест, который проверяет наличия теста "9 mins" в значении времени карточки номер 1.
# body > main > div > div > div > div:nth-child(1) > div > div > div > small

# def test_time_of_first_cat_card(driver):
#     #Решение
#     driver.get("https://suninjuly.github.io/cats.html")
#     first_cat = driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > div > div > div > small")
#     print(first_cat.text)
#     assert first_cat.text == "9 mins"

# Задание 3
# Написать тест, который проверяет наличие теста "I love you so much" в названии последней карточки.

# def test_last_cat_card_name(driver):
#     #Решение
#     driver.get("https://suninjuly.github.io/cats.html")
#     find_text = driver.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div > div > p")
#     print(find_text)
#     assert find_text.text == "I love you so much"




""" ___________________________________  Review of previously covered material  ___________________________________ """

"""  HOME  WORK  """
#
""" __________ --- __________ """

""" __________ --- __________ """
#       ●
# ___ EXAMPLE __________________________________________________
# ___ END of Example __________________________________________________


""" ______  Task 1  ______________________________________________________________________________________________ """
#



