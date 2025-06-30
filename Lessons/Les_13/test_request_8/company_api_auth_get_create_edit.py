# Video 13, _:__:__
# Les13-Auto QA_7-NEW-Requests-24_06.pdf, слайд __.
# ----.py

# ____ - ____________________________________________

# Для загрузки пароля из .env:
from dotenv import load_dotenv
import os
import requests


# ///  Загрузка пароля из .env   /////////////////////////
# ____ Через пары в переменной __________________________
# Загрузка переменных из .env
load_dotenv()
creds_str = os.getenv("CREDENTIALS_LES_13")
pairs = [item.split(":") for item in creds_str.split(",")]
credentials = [(login, pwd) for login, pwd in pairs]
# Для использования вызвать:
login = credentials[0][0]
password = credentials[0][1]



class CompanyApi:
    """Класс для работы с API компаний"""

    def __init__(self, url):
        """Инициализация с базовым URL"""
        self.url = url

    def get_company_list(self):
        """ Получить список всех компаний """
        resp = requests.get(self.url + '/company/list')
        assert resp.status_code == 200, f"Ошибка:a ожидался статус 200, получен {resp.status_code}"
        return resp.json()

    def create_company(self, name, description=""):
        """ Создать новую компанию """
        company = {"name": name, "description": description}
        resp = requests.post(self.url + '/company/create', json=company)
        assert resp.status_code == 201, f"Ошибка: ожидался статус 201, получен {resp.status_code}"
        return resp.json()

    def get_company(self, company_id):
        """ Получить информацию о компании по ID """
        resp = requests.get(self.url + f'/company/{company_id}')
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()

    def get_token(self):
        """ Получить токен авторизации (добавьте корректные данные) """
        creds = {"username": login, "password": password}
        resp = requests.post(self.url + '/auth/login', json=creds)
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()["user_token"]

    def edit_company(self, company_id, new_name, new_descr):
        """ Изменить название и описание компании по ID """
        client_token = self.get_token()
        url_with_token = f"{self.url}/company/update/{company_id}?client_token={client_token}"

        company_data = {
            "name": new_name,
            "description": new_descr
        }

        resp = requests.patch(url_with_token, json=company_data)
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()


    def delete_company(self, company_id):
        """ Удалить компанию по ID """
        client_token = self.get_token()
        url_with_token = f"{self.url}/company/update/{company_id}?client_token={client_token}"

        resp = requests.delete(url_with_token, json=company_id)
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()

