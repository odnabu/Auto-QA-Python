# See:
#   - example in Video 13, 1:08:50
#   - Les13-Auto QA_7-NEW-Requests-24_06.pdf, слайд 73.
#   - test_request_4.py, test_request_5.py

import time

from employee_api import EmployeeApi, l    # Импортируем класс

base_url = "http://5.101.50.27:8000"

api = EmployeeApi(base_url)

header_before_check_in_test = f"\033[90;35m\n{'====  Проверка в самом тесте ':=<{l}}\033[0m"
error_message_if_404_start = f"\t❗ Информация о сотруднике с ID"
error_message_if_404_end = (f"\033[90;31m НЕ\033[0m  найдена.\n\t   Возможно, сервер-демо не сохраняет данные или "
                            f"сбрасывает данные между запросами. Так бывает у публичных учебных API.")


""" _____  TASK 2 ________________________________________________________________________________________________ """

def test_get_employee_info():
    """Тест: получение информации о сотруднике"""

    # 1. Создание нового сотрудника
    employee = api.create_employee(
        first_name="Alice",
        last_name="Brown",
        company_id=2,
        email="alice.brown@example.com",
        phone="+4998765432100",
        birthdate="1938-01-01",
        is_active=True
    )
    employee_id = employee["id"]
    # Проверка, возвращает ли API действительно созданного сотрудника
    print('\n', '-' * l, f"\n\t\033[90;32mСоздан сотрудник с id {employee_id}\033[0m: {employee}")
    # Чтобы убедиться, что ID передаётся корректно и API действительно его не видит:
    # print('-' * 40, '\n', api.get_employee(employee_id).text)     #  НЕ ВИДИТ сотрудника!
    # Судя по всему, сервер-демо не сохраняет созданного сотрудника, или создаёт его в рамках
    # одного запроса, но GET ищет в другой среде (например, сбрасывает данные между запросами).
    # Это часто бывает у публичных учебных API.

    # 2. Запрашиваем информацию о сотруднике
    # ----------------------------------------------
    # КОСЫТЛЬ, чтобы не падал тест.
    # Добавление паузы перед GET, если сервер "ленивый", поскольку, возможно, серверу нужно
    # временя, чтобы обработать POST:
    # time.sleep(1)  # Пауза на 1 секунду    --->   НЕ помогло!
    # ----------------------------------------------
    # Собственно, вызов функции в employee_api.py с Запросом на получение инфо о пользователе:
    retrieved_employee = api.get_employee(employee_id)

    # ----------------------------------------------
    # КОСЫТЛЬ, чтобы не падал тест.
    # # Проверка: есть ли данные
    # if retrieved_employee is None:
    #     print(header_before_check_in_test)
    #     print(error_message_if_404_start, f"\033[90;34m{employee_id}\033[0m", error_message_if_404_end)
    #     return  # Прерывание теста без падения с ошибкой
    # # # Проверка на возвращение None, если сотрудник не найден:
    # # assert retrieved_employee is not None, f"Сотрудник с ID {employee_id} не найден — get вернул None"
    # ----------------------------------------------

    # 3. Проверяем, что данные совпадают
    assert retrieved_employee["id"] == employee_id, f"Ожидался ID {employee_id}, получено {retrieved_employee['id']}"
    assert retrieved_employee["first_name"] == "Alice", f"Ожидалось 'Alice', получено'{retrieved_employee['first_name']}'"
    assert retrieved_employee["last_name"] == "Brown", f"Ожидалось 'Brown', получено'{retrieved_employee['last_name']}'"
    assert retrieved_employee["email"] == "alice.brown@example.com", (f"Ожидалось 'alice.brown@example.com', "
                                                                     f"получено '{retrieved_employee['email']}'")
    assert employee["phone"] == "+4998765432100", f"Ожидалось '+4998765432100', получено '{employee['phone']}'"
    assert employee["birthdate"] == "1938-01-01", f"Ожидалось '1938-01-01', получено '{employee['birthdate']}'"
    assert employee["is_active"] is True, "Ожидалось, что сотрудник активен"

    print(f"Тест пройден: информация о сотруднике {employee_id} получена корректно.")

