# Импортируем нужные модули для работы с браузером и веб-элементами
from selenium import webdriver
import time
import random
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


# Опции браузера
options = webdriver.ChromeOptions()
options.add_argument(
    "--disable-blink-features=AutomationControlled")  # Отключение автоматического определения бот-активности
options.add_argument("--start-maximized")  # Запуск браузера в полноэкранном режиме

# Инициализация браузера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 10)

def price_sorting():
    driver.get("https://www.datart.cz/")

    # Согласие с куки
    cookie_btn = wait.until(EC.element_to_be_clickable((By.ID, "c-p-bn")))
    cookie_btn.click()

    try:
        categories = driver.find_elements(By.XPATH, '//li[@class="main-menu-catalog-category"]')
        if len(categories)>0:
            random_category = random.choice(categories)
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", random_category)  # Прокрутка
            driver.execute_script("arguments[0].focus();", random_category)  # Фокусировка
            random_category.click()
            time.sleep(4)
            print('Categories = OK')
        else:
            print('No categories found')
            driver.quit()
            exit()

        refresh_container = wait.until(EC.presence_of_element_located((By.ID, "snippet--login-refresh")))

        # subcategories= refresh_container.find_elements(By.XPATH, '//div[@class="category-tree-box bg-white"]')
        subcategories = refresh_container.find_elements(By.CLASS_NAME, "category-tree-box.bg-white")

        if len(subcategories)>0:
            random_subcategory = random.choice(subcategories)
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", random_subcategory)  # Прокрутка
            driver.execute_script("arguments[0].focus();", random_subcategory)  # Фокусировка
            time.sleep(2)
            random_subcategory.click()
            time.sleep(2)
            print('subcategories = OK')
        else:
            print('No subcategories found')
            driver.quit()
            exit()

        time.sleep(10)
    except Exception as ex:
        print(ex)


price_sorting()