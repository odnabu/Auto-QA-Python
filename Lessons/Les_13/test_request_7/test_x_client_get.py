# Video 13, _:__:__
# Les13-Auto QA_7-NEW-Requests-24_06.pdf, слайд __.
# test_request_7.py

# ____ - ____________________________________________

from company_api_get_create import CompanyApi  # Импортируем класс



def test_get_one_company():
    base_url = "http://5.101.50.27:8000"
    api = CompanyApi(base_url)
    # Создаем компанию
    name = "PyCharm"
    descr = "IDE"
    result = api.create_company(name, descr)
    new_id = result["id"]

    # Обращаемся к компании
    new_company = api.get_company(new_id)

    # Проверим название, описание и статус новой компании:
    assert new_company["name"] == name
    assert new_company["description"] == descr
    assert new_company["is_active"] is True
