from selenium import webdriver
import time
import random
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, \
    StaleElementReferenceException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
1. Реализовать функционал добавление товара в корзину после нажатия на кнопку
"Načíst další produkty":
Когда пользователь нажал на кнопку "Načíst další produkty", потом продолжает
добавлять новые товары в корзину, товары должны добавляться в список, начиная с
того места, где закончился предыдущий список.
Либо сделать так, чтобы программа автоматически переключала страницы, загружая
новые товары при переходе на следующую страницу.
2. Проверить соответствие количества добавленных товаров с числом на значке
корзины:
После того как пользователь добавит несколько товаров в корзину, необходимо
сравнить количество товаров, которое программа добавила, с числом,
отображающимся на значке корзины.
Если количество товаров в корзине не совпадает с количеством добавленных
товаров, вывести сообщение об ошибке."""


# Опции браузера
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument("--start-maximized")
options.add_argument("--headless")

# Инициализация браузера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def add_to_cart_test():
    driver.get("https://www.dracek.cz/")

    # Ожидание загрузки страницы и принятия куки
    try:
        cookie_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@class="__cookiesNlink __cookiesSuccess"]'))
        )
        cookie_button.click()
    except TimeoutException:
        print("Куки уже приняты или кнопка не найдена.")

    try:
        categories = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//li[@class="mega-drop-down"]'))
        )

        if categories:
            random_category = random.choice(categories)
            random_category.click()
            print("Перешли в случайную категорию.")
        else:
            print("Категории не найдены.")
            driver.quit()
            return

        added_products = 0
        total_pruduct_cout = 32

        while added_products <= total_pruduct_cout:
            add_to_cards_buttons = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '//a[@class="btn main-action buyButton"]'))
            )

            for add_to_cart_button in add_to_cards_buttons:
                if added_products >= total_pruduct_cout:
                    break

                try:
                    # Прокрутка и клик по кнопке "Добавить в корзину"
                    time.sleep(1)
                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_to_cart_button)
                    driver.execute_script("arguments[0].click();", add_to_cart_button)
                    # add_to_cart_button.click()

                    try:
                        back_button = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, '//a[@class="btn modalGreyButton btn-lg dCloseModal"]'))
                        )

                        back_button.click()
                        time.sleep(1)
                    except Exception:
                        continue

                    added_products += 1

                except Exception:
                    continue

            if added_products < total_pruduct_cout:
                try:
                    next_page = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//a[@class="btn j-more-products nextProducts"]'))
                    )
                    next_page.click()
                except Exception:
                    break

        print(f"Тест завершён: добавлено {added_products} товаров в корзину.")




    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        driver.quit()


add_to_cart_test()