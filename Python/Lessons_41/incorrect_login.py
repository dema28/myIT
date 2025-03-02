from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from config import URL, correct_login, incorrect_password


# Опции браузера
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument("--start-maximized")

# Инициализация браузера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 10)


def incorrect_login():
    try:
        driver.get(URL)

        # Согласие с куки
        coockie_btn = wait.until(EC.element_to_be_clickable((By.ID, "c-p-bn")))
        coockie_btn.click()

        login_btn = wait.until(EC.presence_of_element_located((By.ID, "head-login-sign-up")))
        login_btn.click()

        login_field = wait.until(EC.presence_of_element_located((By.ID, "frm-login")))
        login_field.clear()
        login_field.send_keys(correct_login)

        password_field = wait.until(EC.presence_of_element_located((By.ID, "frm-password")))
        password_field.send_keys(incorrect_password)

        submit_btn = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "btn.btn-login")))
        submit_btn.click()

        message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "errorMessage.mb-3"))).text
        incorrect_password_message = "Zadali jste špatné údaje. Zkuste to znovu."

        if message == incorrect_password_message:
            print("Incrorrect Password - Test Passed")
        else:
            print("Incrorrect Password - Test Failed")
    except NoSuchElementException:
        print('Элемент не найден')

    try:
        login_field = wait.until(EC.presence_of_element_located((By.ID, "frm-login")))
        login_field.clear()
        login_field.send_keys('rrrrrr')

        password_field = wait.until(EC.presence_of_element_located((By.ID, "frm-password")))
        # password_field.send_keys(incorrect_password)
        # password_field.click()



        time.sleep(16)
    except NoSuchElementException:
        print('Элемент не найден')







incorrect_login()