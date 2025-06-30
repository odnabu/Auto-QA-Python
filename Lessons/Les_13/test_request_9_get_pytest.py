# Video 13, _:__:__
# Les13-Auto QA_7-NEW-Requests-24_06.pdf, слайд __.
# test_request_9.py

# ____ - ____________________________________________

import requests
import pytest

BASE_URL = "https://reqres.in/api/users"

@pytest.mark.parametrize("user_id, expected_first_name, expected_last_name, expected_email", [
    (2, "Janet", "Weaver", "janet.weaver@reqres.in"),
    # (3, "Karl", "Lagerfeld", "karl_lager@reqres.in"),   # ____ Тут тест УПАДЕТ.
])
def test_get_existing_user(user_id, expected_first_name, expected_last_name, expected_email):
    """Тест: получение информации о существующем пользователе"""
    response = requests.get(f"{BASE_URL}/{user_id}")

    # Проверяем, что запрос выполнен успешно (код 200)
    assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"

    data = response.json()

    # Проверяем, что в ответе есть ключ "data"
    assert "data" in data, "Ответ API не содержит ключ 'data'"

    user = data["data"]

    # Проверяем, что данные пользователя совпадают с ожидаемыми
    assert user["id"] == user_id, f"Ожидался ID {user_id}, получен {user['id']}"
    assert user["first_name"] == expected_first_name, f"Ожидалось '{expected_first_name}', получено '{user['first_name']}'"
    assert user["last_name"] == expected_last_name, f"Ожидалось '{expected_last_name}', получено '{user['last_name']}'"
    assert user["email"] == expected_email, f"Ожидалось '{expected_email}', получено '{user['email']}'"

