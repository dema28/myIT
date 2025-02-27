import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestFormPractice(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://demoqa.com/automation-practice-form")
        self.driver.implicitly_wait(10)

    def addFirstName(self):
        first_name_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='firstName']"))
        )
        first_name_input.send_keys("Denis")

    def addLastName(self):
        last_name_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='lastName']"))
        )
        last_name_input.send_keys("Novicov")

    def addEmail(self):
        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='userEmail']"))
        )
        email_input.send_keys("denisnovicov@example.com")

    def addNumberPhone(self, phone_number):
        if not isinstance(phone_number, str):
            raise ValueError("Номер телефона должен быть строкой")

        cleaned_number = ''.join(filter(str.isdigit, phone_number))


        if len(cleaned_number) != 10:
            raise ValueError("Номер телефона должен содержать ровно 10 цифр")

        phone_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='userNumber']"))
        )
        phone_input.send_keys(phone_number)

    def pickGender(self):
        gender_radio_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(text(),'Male')]"))
        )
        gender_radio_button.click()


    def pickSubject(self):
        subject_select = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='subjectsInput']"))
        )
        subject_select.send_keys("English")
        WebDriverWait(self.driver, 2)

        first_item = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".subjects-auto-complete__control"))
        )
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ENTER).perform()

        subject_select = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='subjectsInput']"))
        )

        subject_select.send_keys("Commerce")
        WebDriverWait(self.driver, 2)

        last_item = WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".subjects-auto-complete__control")))
        time.sleep(10)

        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ENTER).perform()







        # Найдем все элементы в выпадающем списке (предполагаем, что это div элементы с классом option)
        # suggestion_items = self.driver.find_elements(By.XPATH,
        #                                              "//div[@class='subjects-auto-complete__control']//div[contains(@class, 'subjects-auto-complete__option')]")
        #
        # # Перебираем все элементы и кликаем по тому, который совпадает с введенным названием
        # for item in suggestion_items:
        #     if "English" in item.text:
        #         item.click()  # Это действие выбирает элемент из выпадающего списка
        #         break
        #
        # first_item.click()
        #
        # actions = ActionChains(self.driver)
        # actions.send_keys(Keys.ENTER).perform()  # Нажать Enter для подтверждения выбора

        # Очистить поле ввода или продолжить вводить другую букву
        # subject_select.clear()
        #
        # # Вводим вторую букву (например, "M")
        # subject_select.send_keys("M")
        # WebDriverWait(self.driver, 2)  # Даем время для появления нового списка
        #
        # # Ожидаем появления второго элемента и кликаем на него
        # second_item = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//ul[@class='autocomplete-items']/li[1]"))
        # )
        # second_item.click()
        #
        # # Очистить поле ввода для следующей буквы
        # subject_select.clear()
        #
        # # Вводим третью букву (например, "T")
        # subject_select.send_keys("C")
        # WebDriverWait(self.driver, 2)  # Даем время для появления нового списка
        #
        # # Ожидаем появления третьего элемента и кликаем на него
        # third_item = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//ul[@class='autocomplete-items']/li[1]"))
        # )
        # third_item.click()

    def test_form_practice(self):
        self.addFirstName()
        self.addLastName()
        self.addEmail()
        self.addNumberPhone("7999999999")
        self.pickGender()
        self.pickSubject()




    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()