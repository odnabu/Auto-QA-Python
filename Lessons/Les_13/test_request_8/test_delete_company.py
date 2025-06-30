# Video 13, _:__:__
# Les13-Auto QA_7-NEW-Requests-24_06.pdf, слайд __.
# test_request_8

# ____ - ____________________________________________

from company_api_auth_get_create_edit import CompanyApi

def test_delete_company():
    """Тест: удаление компании"""

    base_url = "http://5.101.50.27:8000"
    api = CompanyApi(base_url)

    # 1. Создаём компанию
    name = "Company to be deleted"
    descr = "Delete me"
    result = api.create_company(name, descr)
    company_id = result["id"]

    # 2. Получаем компанию по ID
    new_company = api.get_company(company_id)
    print(f"\n\033[34m{new_company}\033[0m")

    # 3. Проверяем, что компания создана корректно
    assert new_company["name"] == name, f"Ожидалось '{name}', получено '{new_company['name']}'"
    assert new_company["description"] == descr, f"Ожидалось '{descr}', получено '{new_company['description']}'"
    assert new_company["is_active"] is True, "Ожидалось, что компания активна"

    # 4. Получаем список компаний и запоминаем количество
    companies_before = api.get_company_list()
    print(f"\n\033[32m{companies_before[-1]}\033[0m")

    len_before = len(companies_before)
    print(f"\n\033[34m companies_before === {len_before}\033[0m")

    # 5. Удаляем компанию
    api.delete_company(company_id)

    # 6. Получаем список компаний после удаления
    companies_after = api.get_company_list()
    len_after = len(companies_after)
    print(f"\033[33m companies_after *** {len_after}\033[0m")

    # 7. Проверяем, что список компаний уменьшился на 1
    assert len_before - len_after == 1, f"Ожидалось {len_before - 1} компаний, найдено {len_after}"

    # 8. Проверяем, что удалённая компания больше не доступна
    deleted = api.get_company(company_id)
    assert deleted["detail"] == "Компания не найдена", f"Ожидалось 'Компания не найдена', получено '{deleted['detail']}'"

    print(f"Тест пройден: компания {company_id} успешно удалена.")

