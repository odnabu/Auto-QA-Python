# +++++++++++++++++++++++++++++++++++++++++++++
from Les01_14_05_Calculator import Calculator
import pytest
# +++++++++++++++++++++++++++++++++++++++++++++

# Тестирование класса «Калькулятор»
# Pytest
# Популярная библиотека для тестирования
# Python-кода. Она проста в использовании,
# поддерживает автоматический запуск тестов и
# генерацию отчетов.

# Для написания Пай-теста нужно:
#

# Используйте фикстуры Pytest для инициализации общего ресурса. В данном случае — экземпляра класса:
@pytest.fixture
def calculator():
    return Calculator()

@pytest.mark.skip
def test_sum_positive_numb(calculator):
    assert calculator.sum(1, 2) == 3

@pytest.mark.positiv_test
def test_div_positive_numb(calculator):
    assert calculator.div(1, 2) == 0.5

@pytest.mark.skipif(condition="sys.version_info < (3, 8)", reason="Требуется Python 3.8 или выше")
def test_sub_positive_numb(calculator):
    assert calculator.sub(4, 5) == -1

# KEYs:
# pytest - запустит ВСЕ файлы в папке.
# pytest -k "positiv" - запустит только те функции, в названии которых есть positiv.
# pytest -v - запустит с развернутой информацией.
# pytest -m positiv_test - запустит только те, которые помечены как positiv_test.
