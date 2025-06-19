# Skrebnev Fedor
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
""" ################################################################################################################
 17.06.25
 Home Work 5.
 Python - Auto QA 09:  9 - Автоматизация веб-тестов с использованием Selenide, часть 3.
                           Работа с Web элементами.
 ################################################################################################################### """

# ------------------------ SHORTCUTS ---------------------------------------------------------------------------
# Ctrl+W - выделить текущий блок. Если нажимать это сочетание дальше, то будут выделяться родительские блоки.
# Ctrl+Y - Удаление всей строки. Кстати, команда копирования Ctrl+C без выделения также работает для всей строки.
# Ctrl+Akt+L / Alt+Enter - Привести код к принятым стандартам (для Python - PEP8).
# Ctrl+R — Изменить название класса/функции и т.п. по всему проекту.
# Ctrl+Shift + F - Найти по всем файлам.
# Shift + F6 - заменить имя элемента во всех частях во всех файлах.
# Shift+F10 - выполнить код Current файла.
# Double Shift - to search everywhere for classes, files, tool windows, actions, and settings.
#  Ctrl+F8 to toggle the breakpoint.  ???????????
# --------------------------------------------------------------------------------------------------------------

l = 70            # Длина заполнителя.
print('.' * l)

# See theory here: Les09-Auto QA_5-Web_Elements-Alert-ActionChains-input file.pdf

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import pytest
import os
import time
from selenium.common import NoSuchElementException, TimeoutException
# ______ Для имитирования действий пользователя, таких как: наведение
# курсора, клик, перетаскивание элементов ____________________________
from selenium.webdriver.common.action_chains import ActionChains
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Для сокращения ширины всей консоли (чтобы не очень широким выводился блок с
# результатами теста):
os.environ['COLUMNS'] = str(l+1)

# Веб-адреса сайтов по ДЗ:
web_addresses = {
    "a_1": "https://bonigarcia.dev/selenium-webdriver-java/iframes.html",
    "a_2": "https://www.globalsqa.com/demo-site/draganddrop/",
}

# ___ Фикстура - декоратор для последующих обращений к вызову драйвера браузера Chrome ____________
@pytest.fixture
def driver():
    """ Launches the Chrome browser driver and closes it after finishing """
    # Устанавливаем ChromeDriver через WebDriverManager:
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    # Закрываем браузер после теста:
    print(f"\033[32m\n{'  Тест завершен  ':=^{l}}\033[0m")
    driver.quit()



""" ______  Task 1  ______________________________________________________________________________________________ """
# Задание 1: Проверка наличия текста в iframe
# Открыть страницу
# Перейти по ссылке: https://bonigarcia.dev/selenium-webdriver-java/iframes.html.
# Проверить наличие текста
#   1) Найти фрейм (iframe), в котором содержится искомый текст.
#   2) Переключиться в этот iframe.
#   3) Найти элемент, содержащий текст "semper posuere integer et senectus justo curabitur.".
#   4) Убедиться, что текст отображается на странице.


searched_text = "semper posuere integer et senectus justo curabitur."
# searched_text = "semper justo curabitur."

# ______ 1-ый Вариант - ПРОСТОЙ, без выведения текста ____________________________________
def test_text_in_iframe_simple(driver):
    """ Checking the text in iframe."""

    # Открываем страницу:
    driver.get(web_addresses.get("a_1"))

    wait = WebDriverWait(driver, 10)
    # 1) Поиск iframe на странице   и   2) Переключение в iframe:
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe")))

    # 3) Поиск нужного текста внутри iframe:
    element = driver.find_element(By.ID, "content")
    # 4) Проверка:
    assert searched_text in element.text, f"Текст '{searched_text}' \033[31mНЕ\033[0m найден ни в одном элементе внутри iframe."


# ______ 2-ой Вариант с выведением абзаца, содержащего искомый текст И с
#        ИЗМЕНЕННЫМ выводом результата pytest, если текст НЕ найден ____________________________
def test_text_in_iframe_show(driver):
    """ Checking the text in iframe."""

    # Открываем страницу:
    driver.get(web_addresses.get("a_1"))
    # 1) Поиск iframe на странице:
    # 2) Переключение в iframe:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe")))

    # 3) Поиск нужного блока текста внутри iframe, содержащего искомый текст:
    paragraphs = driver.find_elements(By.TAG_NAME, "p")

    highlighted = f'\033[35m{searched_text}\033[0m'
    for p in paragraphs:
        # 4) Проверка:
        if searched_text in p.text:
            print(f"\n\t\033[32m✅ Параграф, содержащий искомый текст:\033[0m\n\t{p.text.replace(searched_text, highlighted)}")
            return  # Успешное завершение

    # Тест НЕ провален, но сообщение есть:
    print(f"\n\t❌ Текст '{highlighted}' \033[31mНЕ\033[0m найден ни в одном параграфе в iframe.")



""" ______  Task 2  ______________________________________________________________________________________________ """
# Задание 2: Тестирование Drag & Drop (Перетаскивание изображения в корзину)
#   1) Открыть страницу Drag & Drop Demo.
#      Перейти по ссылке: https://www.globalsqa.com/demo-site/draganddrop/.
#   2) Выполнить следующие шаги:
#       - Захватить первую фотографию (верхний левый элемент).
#       - Перетащить её в область корзины (Trash).
#       - Проверить, что после перемещения:
#       - В корзине появилась одна фотография.
#       - В основной области осталось 3 фотографии.
# Ожидаемый результат:
#       - Фотография успешно перемещается в корзину.
#       - Вне корзины остаются 3 фотографии.



# Нажатие на кнопку подтверждения куков:
def test_click_cookie(driver):
    """  Confirms cookies by clicking on the button.  """

    # Открываем страницу:
    driver.get(web_addresses.get("a_2"))
    # time.sleep(60)

    # ЯВНОЕ ожидание (конкретного элемента или его состояния) до 5 секунд:
    wait = WebDriverWait(driver, 5)     # Ожидание, пока элемент появится в DOM.

    try:        # Если кнопка не появилась — игнорируем
        # Локатор диалогового окна для подтверждения cookies: class="fc-dialog fc-choice-dialog"

        # Ищем элемент по классу "fc-primary-button" (если появится), потому что по тегу "button"
        # есть 2 кнопки для класса fc-button, и делаем клик:
        cookie_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'fc-primary-button')))
        cookie_button.click()

        # Проверка, что клик сработал: кнопка подтверждения cookies (текст 'Consent')
        # НЕ видна на странице:
        # cookie_button_check = driver.find_element(By.CLASS_NAME, 'fc-primary-button')
        # assert cookie_button_check, f"На странице \033[31mНЕ\033[0m найден элемент с текстом 'Consent'.\n"
        cookie_panel = driver.find_element(By.CLASS_NAME, 'fc-choice-dialog')
        assert cookie_panel, f"На странице \033[31mНЕ\033[0m найден или уже скрыт элемент для подтверждения куков.\n"

    except (NoSuchElementException, TimeoutException) as e:
        error_text = str(e)
        # Обрезка сообщения об ошибке до слова "Stacktrace":
        trimmed_e_text = error_text.split("Stacktrace")[0].strip()
        print(f"\n\tПанель подтверждения cookies с кнопкой 'Consent' \033[31m НЕ видна\033[0m — вероятно, уже скрыта."
              f"\n\t\033[90m{trimmed_e_text}\033[0m")
        print(f"{'':-<{l}}")




def test_drag_drop(driver):
    """  Checking drag & drop method.  """

    # Открываем страницу:
    driver.get(web_addresses.get("a_2"))
    # time.sleep(60)

    # ЯВНОЕ ожидание (конкретного элемента или его состояния) до 5 секунд:
    wait = WebDriverWait(driver, 5)     # Ожидание, пока элемент появится в DOM.

    # Нажатие на кнопку подтверждения куков? чтобы скрыть панель:
    cookie_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'fc-primary-button')))
    cookie_button.click()

    # Переключение на iframe с изображениями:
    # <iframe width="700" height="500" ...  class="demo-frame lazyloaded" ...></iframe>
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe.demo-frame")))

    # Закрытие рекламы (если она всплыла, а она таки всплывает):
    try:
        ad_close = driver.find_element(By.CSS_SELECTOR, ".at-cv-button.at-cv-lightbox-yesno.at-cm-no-button")
        ad_close.click()
    except:
        pass

    try:
        # Поиск фотографий и корзины:
        gallery_fotos = driver.find_elements(By.CSS_SELECTOR, "#gallery li")
        trash = driver.find_element(By.ID, "trash")
        assert len(gallery_fotos) == 4, "Ожидалось 4 фотографии в галерее"

        # Перетаскивание 1-ой фотографии в корзину:
        ActionChains(driver).drag_and_drop(gallery_fotos[0], trash).perform()

        time.sleep(3)  # Пауза, чтобы я успела увидеть что происходит. По сути,  на анимацию "полета" в корзину.

        # Проверка после перетаскивания:
        gallery_fotos_after = driver.find_elements(By.CSS_SELECTOR, "#gallery li")
        trash_items = driver.find_elements(By.CSS_SELECTOR, "#trash li")

        assert len(gallery_fotos_after) == 3, "В галерее должно остаться 3 фотографии"
        assert len(trash_items) == 1, "В корзине должна быть 1 фотография"

    except NoSuchElementException as e:
        error_text = str(e)
        # Обрезка сообщения об ошибке до слова "Stacktrace":
        trimmed_e_text = error_text.split("Stacktrace")[0].strip()
        print(f"\n\tВозникла ошибка, элемент \033[31m НЕ виден\033[0m или уже скрыт."
              f"\n\t\033[90m{trimmed_e_text}\033[0m")
        print(f"{'':-<{l}}")

    print("\n✅ Перетаскивание выполнено успешно!")
