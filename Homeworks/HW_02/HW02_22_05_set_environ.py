# Skrebnev Fedor
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
""" ################################################################################################################
 22.05.25
 Python - Auto QA 02:  Set Environment.
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


""" ______  Task 1  ______________________________________________________________________________________________ """
# Написать скрипт, который:
#   1) Открывает в браузере Firefox https://itcareerhub.de/ru
#   2) Переходит в раздел “Способы оплаты”
#   3) Делает скриншот этой секции страницы
# В качестве ответа на задание необходимо приложить ссылку на git репозиторий.

# Сначала см. Les03-Auto QA_LfS2.pdf, с. 8.

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# __ NB! __ В новой версии Selenium (4.6 и выше) больше не поддерживается параметр executable_path
# напрямую в webdriver.Firefox(...).

@pytest.fixture
def setup_browser():
    options = webdriver.FirefoxOptions()
    # Правильная! настройка драйвера с использованием Service
    service = Service(GeckoDriverManager().install())
    # Настройка браузера Firefox с использованием WebDriver Manager:
    driver = webdriver.Firefox(service=service, options=options)
    yield driver
    driver.quit()

def test_payment_methods_section(setup_browser):
    driver = setup_browser
    # Шаг 1: Открыть страницу https://itcareerhub.de/ru
    driver.get("https://itcareerhub.de")
    # Шаг 2: Перейти в раздел "Способы оплаты":
    payment_methods_link = driver.find_element(By.LINK_TEXT, "Zahlungsarten")
    payment_methods_link.click()

    # Шаг 3: Найти секцию с информацией о способах оплаты и сделать скриншот:
    payment_section = driver.find_element(By.ID, "rec725797078")     # Обновить ID, если он другой.
    payment_section.screenshot("payment_methods_section.png")




""" ___ Как найти актуальный ID нужной секции на сайте: ____________________________________________ """
# По сути, найти id="payment-methods" на сайте:
#   1) Открыть сайт
#   2) Перейти в браузере на https://itcareerhub.de.
#   3) Найти раздел "Zahlungsarten".
#      Прокрутить страницу вниз или нажать на ссылку "Zahlungsarten" в верхнем меню.
#   4) Открыть инструменты разработчика.
#      Нажать F12 или кликнуть правой кнопкой мыши по нужной секции → "Просмотреть код" (Inspect).
#   5) Посмотреть на HTML-структуру.
#      В панели разработчика (обычно справа или снизу) будет выделен HTML-код элемента.
#      Найти id, например: <section id="payment-methods">...</section> или <div id="some-other-id">...</div>.
#      Если нет id, можно использовать class, aria-label, data-* или даже XPath.
# Что делать, если ID отсутствует. Если у секции нет id, то можно:
#   1) Найти по class: payment_section = driver.find_element(By.CLASS_NAME, "название-класса")
#   2) Или использовать XPath:
#      payment_section = driver.find_element(By.XPATH, "//h2[text()='Zahlungsarten']/following-sibling::*[1]")
#       (Это найдёт элемент сразу после заголовка "Zahlungsarten").
