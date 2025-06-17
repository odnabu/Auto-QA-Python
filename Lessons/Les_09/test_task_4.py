import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Фикстура для WebDriver
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# Тест для drag and drop
def test_drag_and_drop(browser):
    url = "https://crossbrowsertesting.github.io/drag-and-drop.html"
    browser.get(url)

    # Находим элементы
    draggable = browser.find_element(By.ID, "draggable")  # Что перетаскиваем
    droppable = browser.find_element(By.ID, "droppable")  # Куда перетаскиваем

    # Создаем объект ActionChains
    actions = ActionChains(browser)

    # Выполняем drag and drop
    actions.drag_and_drop(draggable, droppable).perform()

    # Ожидаем, что текст в droppable изменится на "Dropped!"
    wait = WebDriverWait(browser, 5)
    dropped_text = wait.until(EC.text_to_be_present_in_element((By.ID, "droppable"), "Dropped!"))

    # Проверяем результат
    assert dropped_text, "Текст в droppable не изменился на 'Dropped!'"
