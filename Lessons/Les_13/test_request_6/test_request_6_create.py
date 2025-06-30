# Video 13, _:__:__
# Les13-Auto QA_7-NEW-Requests-24_06.pdf, слайд __.
# test_request_6.py

# ____ - ____________________________________________


from company_api_auth_create import CompanyApi  # Импортируем класс

# **Тест: проверка увеличения списка компаний после создания**
def test_create_company_increases_count():
    """ Тест: создание компании увеличивает список компаний на 1 """

    base_url = "http://5.101.50.27:8000"
    api = CompanyApi(base_url)  # Инициализация API-клиента

    # 1. Получаем текущий список компаний
    companies_before = api.get_company_list()
    initial_count = len(companies_before)

    # 2. Создаём новую компанию
    api.create_company(name="Test Company", description="Automated test creation")
    # 3. Повторно получаем список компаний
    companies_after = api.get_company_list()
    final_count = len(companies_after)

    # 4. Проверяем, что длина списка увеличилась на 1
    assert final_count == initial_count + 1, f"Ожидалось {initial_count + 1} компаний, найдено {final_count}"
    print(f"Тест пройден: до {initial_count}, после {final_count} (добавлена 1 компания).")

