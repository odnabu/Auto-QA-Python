# See:
#   - example in Video 13, 1:08:50
#   - Les13-Auto QA_7-NEW-Requests-24_06.pdf, слайд 73.
#   - test_request_4.py, test_request_5.py

import time

from employee_api import EmployeeApi, l    # Импортируем класс

base_url = "http://5.101.50.27:8000"

api = EmployeeApi(base_url)


""" _____  TASK 1 ________________________________________________________________________________________________ """

def test_create_employee():
    """Тест 1: создание нового сотрудника"""

    # 1. Создание сотрудника
    employee = api.create_employee(
        first_name="John",
        last_name="Doe",
        company_id=1,
        email="john_doe@example.com",
        phone="+4912345678900",
        birthdate="2020-12-31",
        is_active=True
    )

    # 2. Проверяем, что ID созданного сотрудника есть в ответе
    assert "id" in employee, "Ожидалось наличие ключа 'id' в ответе"

    # 3. Проверяем, что данные сотрудника соответствуют отправленным
    assert employee["first_name"] == "John", f"Ожидалось 'John', получено '{employee['first_name']}'"
    assert employee["last_name"] == "Doe", f"Ожидалось 'Doe', получено '{employee['last_name']}'"
    assert employee["company_id"] == 1, f"Ожидалось 1, получено '{employee['company_id']}'"
    assert employee["email"] == "john_doe@example.com", (f"Ожидалось 'john_doe@example.com', "
                                                        f"получено '{employee['email']}'")
    assert employee["phone"] == "+4912345678900", f"Ожидалось '+4912345678900', получено '{employee['phone']}'"
    assert employee["birthdate"] == "2020-12-31", f"Ожидалось '2020-12-31', получено '{employee['birthdate']}'"
    assert employee["is_active"] is True, "Ожидалось, что сотрудник активен"
    print(f"Тест пройден: сотрудник {employee['id']} успешно создан.")
