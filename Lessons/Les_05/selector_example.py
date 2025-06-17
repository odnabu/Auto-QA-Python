
print('.' * 70)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# https://suninjuly.github.io/cats.html
# test-data="some-data"

driver = webdriver.Chrome()
driver.get("http://example.com")

element = driver.find_element(By.TAG_NAME, "h1")
print(element.text)


try:
    element = driver.find_element(By.ID, "non-existent")
    print(f"\033[33mЭлемент найден\033[0m")
except NoSuchElementException:
    print(f"\033[34mЭлемент не найден\033[0m")


driver.quit()
