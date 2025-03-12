import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Настройка опций браузера
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Запуск браузера в полноэкранном режиме
# chrome_options.add_argument("--headless")  # Запуск браузера в headless-режиме (без графического интерфейса)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Отключение автоматизации

# Инициализация драйвера Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


def open_category():
    """
    Открывает случайную категорию на сайте и добавляет товары в корзину.
    """
    # Переход на главную страницу сайта
    driver.get("https://www.dracek.cz/")

    # Принятие куки, если появляется соответствующее окно
    try:
        cookie_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='__cookiesNlink __cookiesSuccess']"))
        )
        cookie_button.click()
    except Exception:
        print("Кнопка куки не найдена или уже принята.")

    # Поиск и выбор случайной категории
    try:
        categories = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//li[@class='mega-drop-down']"))
        )
        if categories:
            random_category = random.choice(categories)
            random_category.click()
            print("Случайная категория выбрана.")
        else:
            print("Категории не найдены.")
            driver.quit()
            return
    except Exception as e:
        print(f"Ошибка при выборе категории: {e}")
        driver.quit()
        return

    # Добавление товаров в корзину
    add_products = 0
    total_products = 20  # Общее количество товаров для добавления

    while add_products < total_products:
        try:
            # Поиск кнопок "Добавить в корзину"
            add_to_cart_buttons = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//a[@class='btn main-action buyButton']"))
            )

            for button in add_to_cart_buttons:
                if add_products >= total_products:
                    break

                try:
                    # Прокрутка к кнопке и клик
                    time.sleep(1)
                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
                    driver.execute_script("arguments[0].click();", button)

                    # Обработка модального окна, если оно появляется
                    try:
                        back_button = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, "//a[@class='btn modalGreyButton btn-lg dCloseModal']"))
                        )
                        time.sleep(1)
                        back_button.click()
                    except Exception:
                        pass  # Если модальное окно не появилось, продолжаем

                    add_products += 1
                    print(f"Добавлено товаров: {add_products}")

                except Exception as e:
                    print(f"Ошибка при добавлении товара: {e}")
                    continue

        except Exception as e:
            print(f"Ошибка при поиске товаров: {e}")
            break

    print(f"Добавлено {add_products} товаров в корзину.")


# Запуск функции
open_category()

# Закрытие браузера после завершения
driver.quit()