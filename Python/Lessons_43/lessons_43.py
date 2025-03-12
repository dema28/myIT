"""00. - Задание Search
📌 Задание: Автоматизированный тест поиска товара на сайте
🔹 Описание задачи:
Написать автоматизированный тест с использованием Selenium (Python), который проверит
работу поиска на сайте Datart.cz.
Тест должен убедиться, что после ввода ключевого слова в поиск, на странице появятся
товары, содержащие это слово в названии или описании.
📝 Требования к тесту:
✅ 1. Открыть сайт Datart.cz
✅ 2. Принять куки (если появляется всплывающее окно)
✅ 3. Найти строку поиска и ввести туда ключевое слово (например, "iPhone")
✅ 4. Нажать Enter, чтобы запустить поиск
✅ 5. Дождаться загрузки результатов (убедиться, что на странице есть хотя бы один
товар)
✅ 6. Найти все товары на странице и проверить их заголовки и описания
✅ 7. Подсчитать, сколько товаров содержат искомое слово в названии или описании
✅ 8. Вывести в консоль результат
📌 Название или описание товара может содержать искомое слово в разном регистре
(например, iphone vs iPhone) — это нужно учесть
🔍 Подсказки по XPath локаторам:
🔹 Поле поиска:
🔹 Результаты товаров (контейнеры):
Если найдено 2 или больше товаров, тест пройден
Если найдено меньше 2, тест не пройден
✅ 9. Закрыть браузер после завершения теста
//input[@type='search']🔹 Название товара:
🔹 Описание товара:
🎯 Ожидаемый результат работы кода:
✅ Если поиск работает корректно и найдено 2 или больше товаров:
❌ Если найдено меньше 2 товаров:
📌 Дополнительные задания:
🔹 Сохранить количество найденных товаров в переменную и записать её в файл
(results.txt)
🔹 Добавить проверку ошибки: если сайт не загрузился или поиск не работает, тест
должен вывести "Ошибка" и не падать
//div[@class='col-md-6 col-xl-4']
.//h3[@class='item-title']
.//div[@class='item-description']
Проверка пройдена: найдено 5 упоминаний ключевого слова 'iphone'.
Проверка не пройдена."""


import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
wait = WebDriverWait(driver, 10)

def wait_site():
    driver.get("https://www.datart.cz/")
    wait.until(EC.element_to_be_clickable((By.ID, "c-p-bn"))).click()
    time.sleep(5)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='q']"))).send_keys("iPhone")
    wait.until(EC.element_to_be_clickable((By.XPATH,
                                           "//button[@class='ufo-button ufo-button--secondary search-widget__input-submit']"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='col-md-6 col-xl-4']")))
    return driver

def check_results(driver):
    items = driver.find_elements(By.XPATH, "//div[@class='col-md-6 col-xl-4']")
    if len(items) < 2:
        print("Ошибка: Найдено меньше 2 товаров.")
        driver.quit()
        return False
    return True

def count_items(driver):
    items = driver.find_elements(By.XPATH, "//div[@class='col-md-6 col-xl-4']")
    return len(items)

driver = wait_site()

if check_results(driver):
    print(f"Найдено {count_items(driver)} упоминаний ключевого слова 'iPhone'.")
    with open("results.txt", "w") as file:
        file.write(str(count_items(driver)))
        print("Количество найденных товаров записано в results.txt.")
        print("Тест пройден успешно.")


driver.quit()

























# try:
#     driver.get("https://www.datart.cz/")
#     wait.until(EC.element_to_be_clickable((By.ID, "c-p-bn"))).click()
#     time.sleep(5)
#     wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='q']"))).send_keys("iPhone")
#     wait.until(EC.element_to_be_clickable((By.XPATH,
#                                            "//button[@class='ufo-button ufo-button--secondary search-widget__input-submit']"))).click()
#     wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='col-md-6 col-xl-4']")))
#     print(f"Найдено {count_items(driver)} упоминаний ключевого слова 'iPhone'.")
#     # Сохранить количество найденных товаров в переменную и записать её в файл
#     with open("results.txt", "w") as file:
#         file.write(str(count_items(driver)))
#         print("Количество найденных товаров записано в results.txt.")
# except Exception as e:
#     print("Ошибка:", str(e))
#     driver.quit()







# driver.quit()


























