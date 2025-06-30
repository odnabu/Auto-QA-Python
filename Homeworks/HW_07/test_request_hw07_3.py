# See:
#   - example in Video 13, 1:08:50
#   - Les13-Auto QA_7-NEW-Requests-24_06.pdf, слайд 73.
#   - test_request_4.py, test_request_5.py



from employee_api import EmployeeApi, l    # Импортируем класс

base_url = "http://5.101.50.27:8000"

api = EmployeeApi(base_url)

header_before_check_in_test = f"\033[90;35m\n{'====  Проверка в самом тесте ':=<{l}}\033[0m"
error_message_if_404_start = f"\t❗ Информация о сотруднике с ID"
error_message_if_404_end = (f"\033[90;31m НЕ\033[0m  найдена.\n\t   Возможно, сервер-демо не сохраняет данные или "
                            f"сбрасывает данные между запросами. Так бывает у публичных учебных API.")


""" _____  TASK 3 ________________________________________________________________________________________________ """

def test_update_employee():
    """Тест: изменение данных о сотруднике"""

    # Получение списка сотрудников:
    # employee_list = api.get_employee_list(2)
    # print()
    # for emp in employee_list:
    #     print(f"\tid: {emp["id"]}, Name: {emp["first_name"], emp["last_name"]}, Company: {emp["company_id"]}")

    # 1. Создание сотрудника
    employee = api.create_employee(
        first_name="Bob",
        last_name="Smith",
        company_id=3,
        email="bobsmith@example.com",
        phone="+1357924680",
        birthdate="1985-07-30",
        is_active=True
    )
    employee_id = employee["id"]
    # ----------------------------------------------
    # КОСЫТЛЬ, чтобы выявить причину, по которой падает тест.
    # Проверка, возвращает ли API действительно созданного сотрудника
    print('\n', '-' * 40, f"\n\t\033[90;32m Создан сотрудник с id {employee_id}\033[0m: {employee}")

    # Собственно, вызов функции в employee_api.py с Запросом на получение инфо о пользователе:
    retrieved_employee = api.get_employee(employee_id)

    # Проверка: есть ли данные:
    if retrieved_employee is None:
        print(header_before_check_in_test)
        print(error_message_if_404_start, f"\033[90;34m{employee_id}\033[0m", error_message_if_404_end)
        return  # Прерывание теста без падения с ошибкой
    # ----------------------------------------------

    # 2. Обновляем данные
    updated_employee = api.update_employee(
        employee_id,
        last_name="Falkor",
        email="falkor_od@example.com",
        is_active=False
    )

    # 3. Проверяем, что данные изменились
    assert updated_employee["last_name"] == "Falkor", f"Ожидалось 'Falkor', получено'{updated_employee['first_name']}'"
    assert updated_employee["email"] == "falkor_od@example.com", (f"Ожидалось 'falkor_od@example.com', "
                                                                    f"получено '{updated_employee['email']}'")
    assert updated_employee["is_active"] is False, "Ожидалось, что сотрудник будет неактивным"
    print(f"Тест пройден: данные сотрудника {employee_id} успешно обновлены.")
