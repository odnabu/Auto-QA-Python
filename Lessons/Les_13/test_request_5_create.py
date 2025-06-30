# Video 13, _:__:__
# Les13-Auto QA_7-NEW-Requests-24_06.pdf, слайд __.
# test_request_5.py

# ____ - ____________________________________________

import requests

base_url = "http://5.101.50.27:8000"

def test_create_company_empty_body():
    """Отправка пустого JSON
    +
    ___ ПРОВЕРКА  ВАЛИДАЦИИ ___ """

    resp = requests.post(base_url + '/company/create', json={})
    response = resp.json()

    print("\n", resp.status_code)

    assert resp.status_code == 422, f"Ожидался 422, получен {resp.status_code}"
    assert response["detail"][0]["msg"] == "Field required"

def test_create_company_increases_count():
    """ ___ ВЛОЖЕННЫЕ ТЕСТЫ ___
    Тест: создание компании увеличивает список компаний на 1"""

    # 1. Получаем текущий список компаний
    resp = requests.get(base_url + "/company/list")
    assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"

    # Количество компаний, созданных ДО:
    companies_before = resp.json()  # Преобразуем ответ в JSON
    initial_count = len(companies_before)  # Запоминаем количество компаний до создания новой

    # 2. Создаём новую компанию
    new_company = {
        "name": "Test Company",
        "description": "Automated test creation"
    }
    resp_create = requests.post(base_url + "/company/create", json=new_company)
    assert resp_create.status_code == 201, f"Ошибка: ожидался статус 201, получен {resp_create.status_code}"

    # 3. Повторно получаем список компаний
    resp_after = requests.get(base_url + "/company/list")
    assert resp_after.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp_after.status_code}"

    # Количество компаний, созданных ПОСЛЕ:
    companies_after = resp_after.json()  # Преобразуем ответ в JSON
    final_count = len(companies_after)  # Запоминаем количество компаний после создания новой
    
    # 4. Проверяем, что длина списка увеличилась на 1
    assert final_count == initial_count + 1, f"Ожидалось {initial_count + 1} компаний, найдено {final_count}"

    print(f"Тест пройден: до {initial_count}, после {final_count} (добавлена 1 компания).")
