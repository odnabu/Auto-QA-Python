# Skrebnev Fedor
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
""" ################################################################################################################
 16.06.25
 Home Work 4.
 Python - Auto QA 07:  7 - Автоматизация веб-тестов с использованием Selenide часть 2.
 ################################################################################################################### """

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

l = 70            # Длина заполнителя.
print('.' * l)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import pytest
import os
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Для сокращения ширины всей консоли (чтобы не очень широким выводился блок с
# результатами теста):
os.environ['COLUMNS'] = str(l+1)

# Веб-адреса сайтов по ДЗ:
web_addresses = {
    "a_1": "http://uitestingplayground.com/textinput",
    "a_2": "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html",
}

# ___ Фикстура - декоратор для последующих обращений к вызову драйвера браузера Chrome ____________
@pytest.fixture
def driver():
    """ _______ """
    # Устанавливаем ChromeDriver через WebDriverManager:
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    # Закрываем браузер после теста:
    print(f"\033[32m\n{'  Тест завершен  ':=^{l}}\033[0m")
    driver.quit()



""" ______  Task 1  ______________________________________________________________________________________________ """
# Проверка изменения текста кнопки
# Тестируемый сайт: http://uitestingplayground.com/textinput
# Шаги теста:
#   1) Перейдите на сайт Text Input.
#   2) Введите в поле ввода текст "ITCH".
#   3) Нажмите на синюю кнопку.
#   4) Проверьте, что текст кнопки изменился на "ITCH".


def test_wait_for_text(driver):
    """ Checking the state change of a button: a different button name appears."""
    # 1) Открываем страницу:
    driver.get(web_addresses.get("a_1"))

    # ЯВНОЕ ожидание (конкретного элемента или его состояния) состояния кнопки
    # (clickable, затем contains text) до 5 секунд:
    wait = WebDriverWait(driver, 3)     # Ожидание, пока элемент появится в DOM.
    # Установка НЕявного ожидания (глобальной задержки) ко всем методам find_element/s,
    # чтобы Selenium ждал заданное время перед тем, как выбросить исключение, ЕСЛИ
    # элемент не найден сразу. Здесь используется для ожидания загрузки элементов на странице:
    driver.implicitly_wait(10)      # Selenium будет ждать до 10 секунд для каждого поиска элемента.

    # 2) Вводим текст "ITCH":
    text_input_field = driver.find_element(By.ID, "newButtonName")
    text_input_field.send_keys("ITCH")

    # 3) Нажимаем кнопку "Button That Should Change it's Name Based on Input Value":
    text_button = driver.find_element(By.ID, "updatingButton")
    text_button.click()

    # Ожидаем изменения состояния кнопки - появления на ней текста "ITCH"
    text_itch = wait.until(
        EC.text_to_be_present_in_element((By.ID, "updatingButton"), "ITCH")
    )
    print(f"\n\ttext_itch = '\033[35m{text_button.text}\033[m'.")


    # 4) Проверяем, что заголовок содержит "Dashboard"
    assert text_itch, "Текст заголовка не содержит 'ITCH'"


""" ______  Task 2  ______________________________________________________________________________________________ """
# Проверка загрузки изображений
# Тестируемый сайт: https://bonigarcia.dev/selenium-webdriver-java/loading-images.html
# Шаги теста:
#   1) Перейдите на сайт Loading Images.
#   2) Дождитесь загрузки всех изображений.
#   3) Получите значение атрибута alt у третьего изображения.
#   4) Убедитесь, что значение атрибута alt равно "award".

def test_alt_image(driver):
    """ Checking the 'alt' attribute of image. """
    # 1) Открываем страницу:
    driver.get(web_addresses.get("a_2"))

    # 2) Установка НЕявного ожидания (глобальной задержки) ко всем методам find_element/s,
    # чтобы Selenium ждал заданное время перед тем, как выбросить исключение, ЕСЛИ элемент не найден сразу.
    # Здесь используется для ожидания загрузки ВСЕХ изображений на странице:
    driver.implicitly_wait(20)      # Ожидание до 10 секунд для каждого поиска элемента

    # ЯВНОЕ ожидание состояния 3-го изображения (contains text) до 10 секунд:
    wait = WebDriverWait(driver, 10)

    # Ожидаем, пока появится 3-е изображение с <img id="award"> станет доступным в DOM:
    text_img_3_alt = wait.until(
        EC.presence_of_element_located((By.ID, "award"))
    )

    # 3) Получаем значение атрибута alt:
    alt_text = text_img_3_alt.get_attribute("alt")
    print(f"\n\talt_text = '\033[35m{alt_text}\033[m'.")

    # 4) Проверяем, что в alt есть текст "award":
    assert alt_text == "award", f"Ожидалось alt='award', а получили: {alt_text}"



