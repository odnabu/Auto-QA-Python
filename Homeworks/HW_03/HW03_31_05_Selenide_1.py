# Skrebnev Fedor
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
""" ################################################################################################################
 31.05.25
 Python - Auto QA 05:  5 - Автоматизация веб-тестов с использованием Selenide часть 1.
 ################################################################################################################### """
from rich.jupyter import display

# ------------------------ SHORTCUTS ---------------------------------------------------------------------------
# Ctrl+W - выделить текущий блок. Если нажимать это сочетание дальше, то будут выделяться родительские блоки.
# Ctrl+Y - Удаление всей строки. Кстати, команда копирования Ctrl+C без выделения также работает для всей строки.
# Ctrl+Akt+L / Alt+Enter - Привести код к принятым стандартам (для Python - PEP8).
# Ctrl+R — Изменить название класса/функции и т. п. по всему проекту.
# Ctrl+Shift + F - Найти по всем файлам.
# Shift + F6 - заменить имя элемента во всех частях во всех файлах.
# Shift+F10 - выполнить код Current файла.
# Double Shift - to search everywhere for classes, files, tool windows, actions, and settings.
#  Ctrl+F8 to toggle the breakpoint.  ???????????
# --------------------------------------------------------------------------------------------------------------

print('.' * 70)


""" ______  Task 1  ______________________________________________________________________________________________ """
# Написать автотест с использованием Python и Pytest, который:
# 1. Открывает https://itcareerhub.de/ru.

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from selenium import webdriver
# ______ Для тестирования __________________________________________________________
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import pytest
import time             # Для установки большей задержки перед закрытием окна браузера.
import os
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

l = 70            # Длина заполнителя.
# Для сокращения ширины всей консоли (чтобы не очень широким выводился блок с
# результатами теста):
os.environ['COLUMNS'] = str(l+1)
pytest.main(["Homeworks/HW_03/HW03_31_05_Selenide_1.py"])

# Адрес веб-страницы для тестирования:
web_page = "https://itcareerhub.de/ru"

# ___ Простое открытие веб-страницы _________________________________________
# driver = webdriver.Chrome()
# driver.get(web_page)
# time.sleep(5)       # Задержка в 5 сек перед закрытием окна со страницей.
# driver.quit()       # Закрытие окна браузера с открытой веб-страницей.
# print(f"\033[33m{'':=<{l}}\033[0m")
# print(f"\033[33mВы посетили Web-страницу:\033[0m\t{web_page}")
# print(f"\033[33m{'':=<{l}}\033[0m")

# ___ Через декоратор для последующих обращений к вызову драйвера ____________
@pytest.fixture(params=["chrome"])
def driver(request):
    """ Открывает https://itcareerhub.de/ru """
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    time.sleep(3)
    print(f"\033[32m\n{'  Тест завершен  ':=^{l}}\033[0m")
    driver.quit()           # Закрытие драйвера браузера.


# CSS-селектор кнопки "Принять" COOKIE:
button_accept_cookie = "#rec630011311 > div > div.t972__banner > div.t972__actions > button.t972__btn.t972__btn-primary.t972__accept-btn.t-btn.t-btn_md"

# Нажатие не кнопку подтверждения куков.
def test_click_cookie(driver):
    """  Подтверждает cookies по клику на кнопку.  """
    driver.get(web_page)
    cookie_click = driver.find_element(By.CSS_SELECTOR, button_accept_cookie)
    cookie_click.click()
    # Проверка, что клик сработал:
    assert "Подтвердить" in driver.page_source


""" ______  Task 2  ______________________________________________________________________________________________ """
# 2. Проверяет, что на странице отображаются:
#       ● Логитип ITCareerHub
#       ● Ссылка “Программыˮ
#       ● Ссылка “Способы оплатыˮ
#       ● Ссылка “Новостиˮ
#       ● Ссылка “О насˮ
#       ● Ссылка “Отзывыˮ
#       ● Кнопки переключения языка (ru и de)

""" _ NB! _  ВОПРОС """   # Почему в терминале при запуске по команде __python Homeworks/HW_03/HW03_31_05_Selenide_1.py__
# ТЕСТИРОВАНИЕ не выполняется так как при нажатии кнопки RUN?

# Соответствие Ключей -- Условиям в задании:
elements_key_to_task = {
    "logo": "Логитип ITCareerHub",
    "link_curriculums": "Ссылка 'Программы'",
    "link_payment": "Ссылка 'Способы оплаты'",
    "link_news": "Новости",
    "link_about_us": "О нас",
    "link_reviews": "Отзывы",
    "button_ru": "Кнопка переключения языка - ru",  # ru
    "button_de": "Кнопка переключения языка - de"
}

# Соответствие Ключей -- CSS-селекторам элементов на странице:
elements_css_selector = {
    "logo": "#rec717843722",
    "link_curriculums": "#rec717847765",
    "link_payment": "div.t396__elem.tn-elem.tn-elem__7178437221709552445907 > a",  # #rec860584261
    "link_news": "#rec725283886",
    "link_about_us": "#rec717852887",
    "link_reviews": "div.t396__elem.tn-elem.tn-elem__7178437221709552523895 > a",
    "button_ru": "div.t396__elem.tn-elem.tn-elem__7178437221710152827519 > a",  # ru
    "button_de": "div.t396__elem.tn-elem.tn-elem__7178437221710153064158 > div > a"  # de
}


def test_display_element(driver):
    """ Проверяет, что на странице отображаются элементы из словаря elements_key_to_task. """
    # Запуск драйвера браузера:
    driver.get(web_page)

    # Клик по "Принять" куки:
    cookie_click = driver.find_element(By.CSS_SELECTOR, button_accept_cookie)
    cookie_click.click()

    """ __ NB! __  --> Здесь проверки лучше делать через CSS_SELECTOR, -->  """
    # --> если нужно каждый элемент тестировать по отдельности, тк ВСЕ элементы
    # из одного класса "tn-atom", и отличаются только хешами, те ID.

    for k, v in elements_css_selector.items():
        try:
            # display_elem = driver.find_element(By.ID, "1710153310155")  # _____ Проверять по ID здесь НЕ получается!
            display_elem = driver.find_element(By.CSS_SELECTOR, elements_css_selector.get(k))
            display_elem.is_displayed()
            print(f"\tЭлемент \"{elements_key_to_task.get(k)}\"\033[33m отображается\033[0m на странице.")
            print(f"{'':-<{l}}")
        except NoSuchElementException as e:
            error_text = str(e)
            # Обрезка сообщения об ошибке до слова "Stacktrace":
            trimmed_text = error_text.split("Stacktrace")[0].strip()
            print(f"\tЭлемент \"{elements_key_to_task.get(k)}\"\033[34m не виден:\033[0m"
                  f"\n\t\033[90m{trimmed_text}\033[0m")
            print(f"{'':-<{l}}")




# Тестирование ВСЕХ элементов в меню, относящихся к классу "tn-atom".
class_name_elems = "tn-atom"

def test_is_displayed_elems(driver):
    """
    Проверяет, видны ли ВСЕ элементы из задания, которые, по сути,
     относятся к одному классу "tn-atom".
    """
    driver.get(web_page)

    # Клик по "Принять" куки:
    cookie_click = driver.find_element(By.CSS_SELECTOR, button_accept_cookie)
    cookie_click.click()

    try:
        display_elems = driver.find_element(By.CLASS_NAME, class_name_elems)
        display_elems.is_displayed()
        print(f"\t\033[33mВсе элементы из списка отображаются на странице:\033[0m")
        for k, v in elements_key_to_task.items():
            print(f"\t\033[90m{v}:\033[0m")
    except NoSuchElementException as e:
        error_text = str(e)
        trimmed_text = error_text.split("Stacktrace")[0].strip()
        print(f"\t\033[34m Или НЕ ВСЕ элементы видны, или все НЕ видны:\033[0m"
              f"\n\t\033[90m{trimmed_text}\033[0m")
        print(f"{'':-<{l}}")



""" ______  Task 3  ______________________________________________________________________________________________ """
# 3. Кликнуть по иконке с телефонной трубкой.

icon_selectors = {
    "icon_css_select": ".t396__elem.tn-elem.tn-elem__7178437221710153310161",   # +++ CSS_SELECTOR
    # "icon_class_name": "tn-elem__7178437221710153310161",                       # +++ CLASS_NAME
    # "icon_css": "#rec717843722",                                                # +++ CSS_SELECTOR
    # "icon_xpath": "//*[@id=\"rec717843722\"]/div/div/div[13]/a/img"             # +++ XPATH
}

text_element = "Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами"

def test_click_icon(driver):
    """
    Проверяет, выполняется ли клик по иконке.
    """
    driver.get(web_page)

    # Клик по "Принять" куки:
    cookie_click = driver.find_element(By.CSS_SELECTOR, button_accept_cookie)
    cookie_click.click()

    for k, v in icon_selectors.items():
        try:
            # click_icon = driver.find_element(By.CLASS_NAME, icon_selectors.get(k))      # +++
            click_icon = driver.find_element(By.CSS_SELECTOR, icon_selectors.get(k))    # +++
            # click_icon = driver.find_element(By.XPATH, "//*[@id=\"rec717843722\"]/div/div/div[13]/a/img")
            click_icon.click()
            # Проверка, что клик сработал: --> Task 4.
            print(f"\tКлик по иконке \"{k}\"\033[33m выполнен\033[0m.")
            print(f"{'':-<{l}}")
        except NoSuchElementException as e:
            error_text = str(e)
            trimmed_text = error_text.split("Stacktrace")[0].strip()
            print(f"\t\033[34m Клик НЕ выполнен:\033[0m"
                  f"\n\t\033[90m{trimmed_text}\033[0m")
            print(f"{'':-<{l}}")



""" ______  Task 4  ______________________________________________________________________________________________ """
# 4. Проверить что текст “Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вамиˮ
#    отображается.

def test_text(driver):
    """  Проверяет, что в модульном окне отображается определенный текст. """
    driver.get(web_page)

    # Клик по "Принять" куки:
    cookie_click = driver.find_element(By.CSS_SELECTOR, button_accept_cookie)
    cookie_click.click()

    try:
        # Клик по иконке с телефонной трубкой:
        click_icon = driver.find_element(By.CSS_SELECTOR, icon_selectors.get("icon_css_select"))
        click_icon.click()
        # Проверка, что текст виден на странице:
        assert text_element in driver.page_source
        print(f"\tЭлемент виден:\n\t\033[33m{text_element}\033[0m")
    except NoSuchElementException:
        print(f"\t\033[34mЭлемент не найден.\033[0m")
