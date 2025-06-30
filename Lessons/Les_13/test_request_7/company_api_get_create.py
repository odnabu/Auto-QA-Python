# Video 13, _:__:__
# Les13-Auto QA_7-NEW-Requests-24_06.pdf, слайд __.
# ---.py

# ____ - ____________________________________________

import requests


# ____  Создание Компании  ____

class CompanyApi:
    """ Класс для работы с API компаний """

    def __init__(self, url):
        """ Инициализация с базовым URL"""
        self.url = url

    def get_company_list(self):
        """ Получить список всех компаний"""
        resp = requests.get(self.url + '/company/list')
        assert resp.status_code == 200, f"Ошибка:a ожидался статус 200, получен {resp.status_code}"
        return resp.json()

    def create_company(self, name, description=""):
        """ Создать новую компанию"""
        company = {"name": name, "description": description}
        resp = requests.post(self.url + '/company/create', json=company)
        assert resp.status_code == 201, f"Ошибка: ожидался статус 201, получен {resp.status_code}"
        return resp.json()

    def get_company(self, company_id):
        """ Получить информацию о компании по ID"""
        resp = requests.get(self.url + f'/company/{company_id}')
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()

