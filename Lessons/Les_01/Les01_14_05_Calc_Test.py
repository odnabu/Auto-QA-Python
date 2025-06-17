# # +++++++++++++++++++++++++++++++++++++++++++++
# from Les01_14_05_Calculator import Calculator
# # +++++++++++++++++++++++++++++++++++++++++++++
#
# # Создайте экземпляр класса Calculator:
# calculator = Calculator()
#
# # Положительные числа
# res = calculator.sum(4, 5)
# print(res)
# # assert res == 3                   # Метод assert осуществляет проверку результата. Возвращает True or False.
# assert res == 9                     # Метод assert осуществляет проверку результата. Возвращает True or False.
#
# # Отрицательные числа
# res = calculator.sum(-6, -10)
# assert res == -16
# print(res)
#
# # Сложение положительного и отрицательного числа
# res = calculator.sum(-6, 6)
# assert res == 0
#
# # Сложение дробных чисел
# res = calculator.sum(5.6, 4.3)
# res = round(res, 1)
# assert res == 9.9
#
# # Сложение числа и нуля
# res = calculator.sum(10, 0)
# assert res == 10
#
# # Обычное деление
# res = calculator.div(10, 2)
# assert res == 5
#
# # Деление на ноль
# # try:
# #     calculator.div(10, 0)
# # except ArithmeticError as e:
# #     assert str(e) == "На ноль делить нельзя"
#
# # numbers = []
# # res = calculator.avg(numbers)
# # assert res == 0
# # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
# # res = calculator.avg(numbers)
# # assert res == 5
# # Пустой список Список чисел
#
