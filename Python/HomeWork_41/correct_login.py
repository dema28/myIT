import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from utils import URL, EMAIL_V, PASSWORD_V

chrome_options = Options()
# chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
wait = WebDriverWait(driver, 10)

class AddLogin:
    def is_valid_email(self, email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(pattern, email) is not None

    def incorrect_login(self):
        try:
            driver.get(URL)

            wait.until(EC.element_to_be_clickable((By.ID, "c-p-bn"))).click()

            login_btn = wait.until(EC.presence_of_element_located((By.ID, "head-login-sign-up")))
            login_btn.click()

            email_input = wait.until(EC.presence_of_element_located((By.ID, "frm-login")))
            password_input = wait.until(EC.presence_of_element_located((By.ID, "frm-password")))

            email_input.send_keys("")
            password_input.send_keys(PASSWORD_V)

            submit_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-login")))
            submit_btn.click()

            error_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "error-text")))

            assert error_message.is_displayed(), "Ошибка: Сообщение об ошибке не отображается для пустого email"

            print("Тест с невалидным email успешно пройден!")

        except AssertionError as ve:
            print(f"Ошибка в тесте с невалидным email: {ve}")
        except Exception as e:
            print(f"Тест завершился с ошибкой: {e}")

    def correct_login(self):
        try:
            assert self.is_valid_email(EMAIL_V), f"Ошибка: некорректный email -> {EMAIL_V}"

            driver.get(URL)

            login_btn = wait.until(EC.presence_of_element_located((By.ID, "head-login-sign-up")))
            login_btn.click()

            email_input = wait.until(EC.presence_of_element_located((By.ID, "frm-login")))
            password_input = wait.until(EC.presence_of_element_located((By.ID, "frm-password")))

            email_input.send_keys(EMAIL_V)
            password_input.send_keys(PASSWORD_V)

            submit_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-login")))
            submit_btn.click()

            assert wait.until(EC.presence_of_element_located(
                (By.XPATH, "//span[@data-id='26997985']"))), "Ошибка: пользователь не вошёл!"

            print("Тест с корректным email успешно пройден!")

        except AssertionError as ve:
            print(f"Ошибка в тесте с корректным email: {ve}")
        except Exception as e:
            print(f"Тест завершился с ошибкой: {e}")

    def run_tests(self):
        self.incorrect_login()
        self.correct_login()


login_test = AddLogin()
login_test.run_tests()


driver.quit()
