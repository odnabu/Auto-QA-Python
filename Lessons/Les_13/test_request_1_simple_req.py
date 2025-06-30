# Video 13, 1:06:25
# Les13-Auto QA_7-NEW-Requests-24_06.pdf, слайд 68.
# test_request_1.py

# ____ Запрос на получение списка компаний _______________________

import requests

def test_simple_req():
    resp = requests.get('http://5.101.50.27:8000/company/list')

    assert resp.status_code == 200  # Проверяем успешный статус
    assert resp.headers["Content-Type"] == "application/json"  # Проверяем тип контента


def test_simple_req2():
    resp = requests.get('http://5.101.50.27:8000/company/list')

    response_body = resp.json()  # Преобразуем ответ в JSON

    print("\n", response_body)
    
    first_company = response_body[0]  # Получаем первую компанию из списка

    # ____  СНАЧАЛА нужно проверять СТУС-код!!!
    assert resp.status_code == 200
    # ____  потом проверять ЗАГОЛОВКИ!
    assert resp.headers["Content-Type"] == "application/json"
    # ____  и ТОЛЬКО потому переходим к проверке БОДИ - содержимого!
    assert first_company["name"] == "QA Студия 'ТестировщикЪ'"

