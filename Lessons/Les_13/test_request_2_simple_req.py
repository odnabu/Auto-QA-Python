# Video 13, 1:__:__
# Les13-Auto QA_7-NEW-Requests-24_06.pdf, слайд __.
# test_request_2.py

# ____ - _______________________
import requests

def test_req_text():
    resp = requests.get("https://jsonplaceholder.typicode.com/posts/1")

    print("\n", resp.text)  # Получаем ответ в виде строки

def test_req_json():
    resp = requests.get("https://jsonplaceholder.typicode.com/posts/1")

    data = resp.json()  # Преобразуем JSON в Python-объект
    print("\n", data["title"])  # Теперь можно обращаться к данным как к словарю

def test_req_not_json():

    resp = requests.get("https://example.com")  # HTML, не JSON
    # print("\n", resp.json())  # Ошибка: JSONDecodeError
    print("\n", resp.text)    # Ошибки НЕ будет.
