# Skrebnev Fedor
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
""" ################################################################################################################
 19.05.25
 Python - Auto QA 01:  INTRODUCTION.
 ################################################################################################################### """


print('.' * 80)

# +++++++++++++++++++++++++++++++++++++++++++++
from HW01_19_05_simple_math import SimpleMath
# +++++++++++++++++++++++++++++++++++++++++++++

# Экземпляр класса для тестов:
math = SimpleMath()


def test_square_positive():
    """ Тест метода square для положительного числа."""
    assert math.square(2) == 4

res = math.square(2)
print(res)



def test_square_negative():
    """ Тест метода square для отрицательного числа."""
    assert math.square(-3) == 9

res = math.square(-3)
print(res)



def test_square_zero():
    """Тест метода square для нуля."""
    assert math.square(0) == 0

res = math.square(0)
print(res)



def test_cube_positive():
    """Тест метода cube для положительного числа."""
    assert math.cube(3) == 27

res = math.cube(3)
print(res)



def test_cube_negative():
    """Тест метода cube для отрицательного числа."""
    assert math.cube(-2) == -8

res = math.cube(-2)
print(res)



def test_cube_zero():
    """Тест метода cube для нуля."""
    assert math.cube(0) == 0

res = math.cube(0)
print(res)

