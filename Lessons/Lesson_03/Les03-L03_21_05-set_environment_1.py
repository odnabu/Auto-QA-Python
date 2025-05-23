# Skrebnev Fedor
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
""" ################################################################################################################
 21.05.25
 Python - Auto QA 03:  Настройка окружения.
 ################################################################################################################### """

# ------------------------ SHORTCUTS ------------------------
# Ctrl + W - выделить текущий блок. если нажимать это сочетание дальше, то будут выделяться родительские блоки.
# Ctrl+Y - Удаление всей строки. Кстати, команда копирования Ctrl+C без выделения также работает для всей строки.
# Ctrl+Akt+L / Alt+Enter - Привести код к принятым стандартам (для Python - PEP8).
# Ctrl+R — Изменить название класса/функции и т. п. по всему проекту.
# Ctrl+Shift + F - Найти по всем файлам.
# Shift + F6 - заменить имя элемента во всех частях во всех файлах.
# -----------------------------------------------------------

print('.' * 120)


""" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%______________   Selenium   _____________%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% """

# +++++++++++++++++++++++++++++++++++++++++++++++++++++
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

import requests
# +++++++++++++++++++++++++++++++++++++++++++++++++++++

# curl -X POST http://localhost:52345/session -d '{"capabilities": {"browserName": "chrome"}}'
# export PATH="$HOME/Downloads:$PATH"

# Укажите путь к драйверу
driver_path = r"C:\Users\odnab\PycharmProjects\Python_Auto_QA\Lessons\Lesson_03\chromedriver-win64"

# В консоли перейти в папку с ДРАЙВЕРОМ:
# cd C:\Users\odnab\PycharmProjects\Python_Auto_QA\Lessons\Lesson_03\chromedriver-win64

# После команды просмотра ls в консоли я увижу -->
# (.venv) PS C:\Users\odnab\PycharmProjects\Python_Auto_QA\Lessons\Lesson_03\chromedriver-win64> ls
#
#     Directory: C:\Users\odnab\PycharmProjects\Python_Auto_QA\Lessons\Lesson_03\chromedriver-win64
#
#
# Mode                 LastWriteTime         Length Name
# ----                 -------------         ------ ----
# -a----         5/21/2025  12:55 PM       18942464 chromedriver.exe
# -a----         5/21/2025  12:55 PM           1536 LICENSE.chromedri
#                                                   ver
# -a----         5/21/2025  12:55 PM         685225 THIRD_PARTY_NOTIC
#                                                   ES.chromedriver

# Запустить через консоль ДРАЙВЕР:
# (.venv) PS C:\Users\odnab\PycharmProjects\Python_Auto_QA\Lessons\Lesson_03\chromedriver-win64> ./chromedriver
# Starting ChromeDriver 136.0.7103.94 (fa0be0b33debeb378a8e6ad9c599be34e2dc3b37-refs/branch-heads/7103@{#1842}) on port 0
# Only local connections are allowed.
# Please see https://chromedriver.chromium.org/security-considerations for suggestions on keeping ChromeDriver safe.
# ChromeDriver was started successfully on port 51705.

# Потом во ВТОРОМ ОКНЕ ТЕРМИНАЛА (клацнуть на + чтобы создать Local (2)) консоли выполнить команду:
#  __ NOT  WORKING __
# curl -X POST http://localhost:51705/session -d '{"capabilities": {"browserName": "chrome"}}'

# Потом во ВТОРОМ ОКНЕ ТЕРМИНАЛА (клацнуть на + чтобы создать Local (2)) консоли выполнить команду для Windows:
# __ NOT  WORKING  __
# curl.exe -X POST http://localhost:51705/session -H "Content-Type: application/json" -d "{`"capabilities`": {`"alwaysMatch`": {`"browserName`": `"chrome`"}}}"

# --- Какие-то команды, непонятно куда их вставлять и что будет ------------------
# resp = requests.post(
#     "http://localhost:51705/session",
#     json={"capabilities": {"alwaysMatch": {"browserName": "chrome"}}}
# )
# print(resp.json())
# --------------------------------------------------------------------------------


# Создание сервиса для драйвера
service = Service(driver_path)

# Инициализация драйвера с использованием сервиса
driver = webdriver.Chrome()     #  Chrome(service=service)

try:
    driver.get("https://www.wikipedia.org/")
    sleep(1)

    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys("Selenium WebDriver")
    sleep(1)
    search_box.send_keys(Keys.RETURN)

    sleep(1)
    print(driver.title)
finally:

    driver.quit()


# Снипет - Команды для консоли --> для проверки скрипта в примере ДЗ 02:
# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager
# # Настройка драйвера для Firefox с использованием WebDriverManager
# driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))



""" ___________________________________  Review of previously covered material  ___________________________________ """


""" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%___________   ---   __________%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% """

""" __________ --- __________ """

""" __________ --- __________ """
#       ●
# ___ EXAMPLE __________________________________________________
# ___ END of Example __________________________________________________


""" ______  Task 1  ______________________________________________________________________________________________ """
#



