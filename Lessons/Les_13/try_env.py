
# Для загрузки пароля из .env:
from dotenv import load_dotenv
import os


# ///  Загрузка пароля из .env   /////////////////////////
# ____ Через пары в переменной __________________________
# Загрузка переменных из .env
load_dotenv()
creds_str = os.getenv("CREDENTIALS_LES_13")
pairs = [item.split(":") for item in creds_str.split(",")]
credentials = [(login, pwd) for login, pwd in pairs]
# Для использования вызвать:
print(f"\033[31m{'':*<20} {credentials}\033[0m")
login = credentials[0][0]
password = credentials[0][1]
print(f"\033[31m{'':=<5} {login, password}\033[0m")


# ____ Через load_dotenv() по отдельности  _____________
# # Загрузка переменных из .env
# load_dotenv()
# # Получаем значения
# login = os.getenv("LOGIN")
# password = os.getenv("PASSWORD")
