# Skrebnev Fedor
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
""" ################################################################################################################
 16.05.25
 Python - Auto QA 02:  Summary 1.
 ################################################################################################################### """

# Video Lesson 02: ------------.
# Video Practice __: wasn't.
# links:
#   - Presentation:
#   - Облегчаем себе жизнь с помощью BeautifulSoup4: https://habr.com/ru/articles/544828/
#   - Устанавливаем python-пакеты с помощью pip: https://pythonworld.ru/osnovy/pip.html
#
# def input_numb_list():
#     numb_list = [int(x) for x in input('Enter a list of numbers separated by space: ').split()]
#     return numb_list
# ------------------------ SHORTCUTS ------------------------
# Ctrl + W - выделить текущий блок. если нажимать это сочетание дальше, то будут выделяться родительские блоки.
# Ctrl+Y - Удаление всей строки. Кстати, команда копирования Ctrl+C без выделения также работает для всей строки.
# Ctrl+Akt+L / Alt+Enter - Привести код к принятым стандартам (для Python - PEP8).
# Ctrl+R — Изменить название класса/функции и т. п. по всему проекту.
# Ctrl+Shift + F - Найти по всем файлам.
# Shift + F6 - заменить имя элемента во всех частях во всех файлах.
# -----------------------------------------------------------

print('.' * 120)


""" ______  Task 1  ______________________________________________________________________________________________ """
#

# +++++++++++++
import pytest
# +++++++++++++

class SimpleMath:
    def sum(self, a, b):
        return a + b

    def square(self, x):
        return x * x

    def cube(self, y):
        return y * y * y


@pytest.fixture
def simple_math():
    return SimpleMath()

# def test_positive_square(simple_math):
#     assert simple_math.square(5) == 25

# def test_positive_cube(simple_math):
#     assert simple_math.cube(3) == 27

@pytest.mark.parametrize("a, b, expected", [        # __NB! __ TTP - Table Testing Pattern.
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
])
def test_sum(simple_math, a, b, expected):
    assert simple_math.sum(a, b) == expected


""" __ NB! __ """    # ЗАПУСК только через ТЕРМИНАЛ:
# pytest -v Lessons/Lesson_02/Les02-S01_16_05-test.py









""" ___________________________________  Review of previously covered material  ___________________________________ """


""" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%___________   ---   __________%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% """

""" __________ --- __________ """

""" __________ --- __________ """
#       ●
# ___ EXAMPLE __________________________________________________
# ___ END of Example __________________________________________________


""" ______  Task 1  ______________________________________________________________________________________________ """
#



