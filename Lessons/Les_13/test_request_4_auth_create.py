# Video 13, 1:08:50
# Les13-Auto QA_7-NEW-Requests-24_06.pdf, слайд 73.
# test_request_4.py

# ____ Запрос на авторизацию ____________________________________________

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



base_url = "http://5.101.50.27:8000"


def test_auth():
    creds = {
        'username': login,
        'password': password
    }
    resp = requests.post(base_url + '/auth/login', json=creds)

    print("\n", resp.json())    # print() -- ДАМП - техническая информация.

    assert resp.status_code == 200
    assert resp.json()["user_token"] is not None  # Проверяем, что токен получен


def test_create_company():
    company = {
        "name": "python",
        "description": "requests"
    }

    resp = requests.post(base_url + '/company/create', json=company)

    assert resp.status_code == 201  # 201 означает, что компания успешно создана
