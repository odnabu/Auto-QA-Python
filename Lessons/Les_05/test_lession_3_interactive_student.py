

print('.' * 70)


""" 
        pytest Lessons/Lesson_05/test_lession_3_interactive_student.py -v
"""

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

@pytest.fixture(params=["chrome"])
def driver(request):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

# # Задание 1
# # Написать тест, который проверяет наличия теста “Cat memesˮ в заголовке страницы.
# def test_header_text(driver):
#     #Решение
#     driver.get("https://suninjuly.github.io/cats.html")
#     get_h1 = driver.find_element(By.TAG_NAME, "h1")
#     print(get_h1.text)
#     assert get_h1.text == "Cat memes"


# Задание 2
# Написать тест, который проверяет наличия теста "9 mins" в значении времени карточки номер 1.
# body > main > div > div > div > div:nth-child(1) > div > div > div > small
# def test_time_of_first_cat_card(driver):
#     #Решение
#     driver.get("https://suninjuly.github.io/cats.html")
#     first_cat = driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > div > div > div > small")
#     print(first_cat.text)
#     assert first_cat.text == "9 mins"

# # Задание 3
# # Написать тест, который проверяет наличие теста "I love you so much" в названии последней карточки.
# def test_last_cat_card_name(driver):
#     #Решение
#     driver.get("https://suninjuly.github.io/cats.html")
#     find_text = driver.find_element(By.CSS_SELECTOR, "div:nth-child(6) > div > div > p")
#     print(find_text)
#     assert find_text.text == "I love you so much"


# # Задание 4
# # Написать тест, который проверяет наличия теста "Cats album" возле иконки фото
# def test_cats_album_text(driver):
#     #Решение
#     driver.get("https://suninjuly.github.io/cats.html")
#     find_text_1 = driver.find_element(By.TAG_NAME, "strong")
#     print(find_text_1.text)
#     assert find_text_1.text == "Cats album"

# Задание 5
# Проверить, что первая карточка отображается целиком.
def test_first_cat_card_is_displayed(driver):
    #Решение
    driver.get("https://suninjuly.github.io/cats.html")
    cart = driver.find_element(By.CSS_SELECTOR, ".col-sm-4:nth-child(1)")
    assert cart.is_displayed()







# Задание
# def test_photo_icon_is_displayed(driver):
#     #Решение
#     driver.get("https://suninjuly.github.io/cats.html")


# Задание
# def test_check_image_quantity(driver):
#     #Решение
#     driver.get("https://suninjuly.github.io/cats.html")


# Задание
# def test_check_cards_quantity(driver):
#     #Решение
#     driver.get("https://suninjuly.github.io/cats.html")


# Задание
# def test_check_all_cards_are_displayed(driver):
#     #Решение
#     driver.get("https://suninjuly.github.io/cats.html")


# Задание
# def test_check_all_images_are_displayed(driver):
#     #Решение
#     driver.get("https://suninjuly.github.io/cats.html")
