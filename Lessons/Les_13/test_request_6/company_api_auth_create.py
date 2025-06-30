# Video 13, _:__:__
# Les13-Auto QA_7-NEW-Requests-24_06.pdf, слайд __.
# ----.py

# ____ - ____________________________________________

import requests



class CompanyApi:
    """ Класс для взаимодействия с API компаний """

    def __init__(self, url):
        """ Инициализация класса с базовым URL API """
        self.url = url

    def get_company_list(self):
        """ Получить список всех компаний """
        resp = requests.get(self.url + '/company/list')
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()

    def get_token(self, user, password):
        """ Получить токен авторизации """
        creds = {"username": user, "password": password}    # ____ так делать НЕЛЬЗЯ! __________________
                                                            # Но, здесь допустимо, потому что учебный сервер
        resp = requests.post(self.url + '/auth/login', json=creds)
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()["user_token"]

    def create_company(self, name, description=""):
        """ Создать новую компанию """
        company = {"name": name, "description": description}
        resp = requests.post(self.url + '/company/create', json=company)
        assert resp.status_code == 201, f"Ошибка: ожидался статус 201, получен {resp.status_code}"
        return resp.json()
