from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class DriverManager:
    @staticmethod
    def create_driver():
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        # chrome_options.add_argument("--headless")  # Раскомментируйте для headless-режима

        driver = webdriver.Chrome(options=chrome_options)
        driver.implicitly_wait(10)  # Неявное ожидание 10 секунд
        return driver

    @staticmethod
    def quit_driver(driver):
        driver.quit()