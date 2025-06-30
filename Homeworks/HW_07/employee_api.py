# See:
#   - example in Video 13, 1:08:50
#   - Les13-Auto QA_7-NEW-Requests-24_06.pdf, слайд 73.
#   - test_request_4.py, test_request_5.py


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



l = 60
header_before_check_in_model = f"\033[90;33m\n{'◇◇◇◇  Проверка в модели EmployeeApi ':◇<{l}}\033[0m"

class EmployeeApi:
    """ Класс для работы с API сотрудников """

    def __init__(self, url):
        """ Инициализация с базовым URL """

        self.url = url


    def get_employee_list(self, company_id):
        """ Получить список всех сотрудников """
        resp = requests.get(self.url + f'/employee/list/{company_id}')
        assert resp.status_code == 200, f"Ошибка:a ожидался статус 200, получен {resp.status_code}"
        return resp.json()


    def create_employee(self, first_name, last_name, # middle_name,
                        company_id, email, phone, birthdate, is_active=True):
        """ Создание нового сотрудника """

        employee_data = {
            "first_name": first_name,
            "last_name": last_name,
            # "middle_name": middle_name,
            "company_id": company_id,
            "email": email,
            "phone": phone,
            "birthdate": birthdate,
            "is_active": is_active
        }
        resp = requests.post(f"{self.url}/employee/create", json=employee_data)
        # assert resp.status_code == 201, f"Ошибка: ожидался статус 201, получен {resp.status_code}"
        assert resp.status_code in [200, 201], f"Ошибка: ожидался статус 200 или 201, получен {resp.status_code}"
        return resp.json()


    def get_employee(self, employee_id):
        """ Получение информации о сотруднике по ID """

        # ==========    ПРОБЛЕМА БЫЛА В   info?id=   ===============================
        # Вариант из примера решения в Les14-Auto QA_SUM7-27_06.pdf
        # resp = requests.get(f"{self.url}/employee/info?id={employee_id}")
        # ==========================================================================

        # Мой вариант (РАБОЧИЙ), откорректированный с учетом документации по ссылке
        # http://5.101.50.27:8000/docs#/employee/read_employee_employee_info__employee_id__get :
        resp = requests.get(f"{self.url}/employee/info/{employee_id}")

        # ----------------------------------------------
        # __ Отладочный вывод __ в get_employee(), чтобы понять, что именно возвращает сервер, и
        # действительно ли сотрудник "не найден".
        print(f"\n\t\033[90;36m {'____ ПРОВЕРКА, создан ли сотрудник ':_<{l}}\033[0m]")
        print(f"\n\t\033[90;36m Запрос:\033[0m {self.url}/employee/info/{employee_id}")
        print(f"\t\033[90;36m Код ответа:\033[0m {resp.status_code}")
        print(f"\t\033[90;36m Тело ответа:\033[0m {resp.text}")

        # if resp.status_code == 404:
        #     print(header_before_check_in_model)
        #     # API вернул "Not Found" — сотрудник не существует
        #     print(f"\t ⚠️ Сотрудник с ID \033[90;34m{employee_id}\033[0m \033[90;31m НЕ\033[0m найден.")
        #     return None
        # # Судя по всему, сервер-демо не сохраняет созданного сотрудника, или создаёт его в рамках
        # # одного запроса, но GET ищет в другой среде (например, сбрасывает данные между запросами).
        # # Это часто бывает у публичных учебных API.
        #
        # if resp.status_code != 200:
        #     raise Exception(f"Неожиданный статус: {resp.status_code}")
        # ----------------------------------------------

        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()



    def get_token(self):
        """Получить токен авторизации (добавьте корректные данные)"""

        creds = {"username": login, "password": password}
        resp = requests.post(self.url + '/auth/login', json=creds)
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()["user_token"]


    def update_employee(self, employee_id, **kwargs):
        """ Изменение данных сотрудника (передаются только изменяемые параметры) """

        client_token = self.get_token()
        url_with_token = f"{self.url}/employee/change/{employee_id}?client_token={client_token}"

        update_data = {key: value for key, value in kwargs.items() if value is not None}

        # ==========    ПРОБЛЕМА БЫЛА В   info?id=   ===============================
        # Вариант из примера решения в Les14-Auto QA_SUM7-27_06.pdf
        # resp = requests.patch(f"{self.url}/employee/change?id={employee_id}", json=update_data)
        # ==========================================================================

        # Мой вариант (РАБОЧИЙ), откорректированный с учетом документации по ссылке
        # http://5.101.50.27:8000/docs#/employee/read_employee_employee_info__employee_id__get :
        # resp = requests.patch(f"{self.url}/employee/change/{employee_id}", json=update_data)
        resp = requests.patch(url_with_token, json=update_data)

        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        print(f"\n\t\033[90;33m {'____ ПРОВЕРКА, обновлены ли данные сотрудника ':_<{l}}")
        print(f"\n\t\033[90;33m Запрос:\033[0m {self.url}/employee/info/{employee_id}")
        print(f"\t\033[90;33m Код ответа:\033[0m {resp.status_code}")
        print(f"\t\033[90;33m Тело ответа:\033[0m {resp.text}")
        return resp.json()


