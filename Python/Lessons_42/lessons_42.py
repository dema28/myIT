"""Выбрать товары на сайте и проверить что их цены отсортированы в порядке убывания.
нужно использовать selenimum"""
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
# chrome_options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
wait = WebDriverWait(driver, 10)


def get_products_from_website():
    # Открываем сайт
    driver.get("https://www.datart.cz/")

    wait.until(EC.element_to_be_clickable((By.ID, "c-p-bn"))).click()

    tel_btn = wait.until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='link-name'][strong[text()='Telefony']]")))
    tel_btn.click()

    xiaomi_btn = wait.until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='snippet--login-refresh']/div/div[4]/a/span")))
    xiaomi_btn.click()

    time.sleep(4)

    # Получаем все товары с сайта
    products = []

    product_elements = driver.find_elements(By.CSS_SELECTOR, "div.product-item")

    for product_element in product_elements:
        # Получаем название и цену товара
        title = product_element.find_element(By.CSS_SELECTOR, "h2.product-title").text

        # Получаем цену товара

        price_element = product_element.find_element(By.CSS_SELECTOR, "span.product-price")

        price = float(price_element.text.replace("$", ""))

        # Добавляем товар в список


        products.append({
            "title": title,
            "price": price
        })

    # Закрываем драйвер
    driver.quit()

    return products


def check_price_ordering():
    # Получаем список товаров с сайта
    products = get_products_from_website()

    # Проверяем, что цены отсортированы в порядке убывания
    for i in range(len(products) - 1):
        assert products[i]['price'] >= products[i + 1]['price']

    print("All prices are in descending order")
    return True

# Проверяем цены отсортированы в порядке убывания
check_price_ordering()
