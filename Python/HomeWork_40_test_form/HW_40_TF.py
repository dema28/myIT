import os
import unittest
import time
from time import sleep
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
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

        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ENTER).perform()


    def pick_check_boxes(self):
        checkbox1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[@for='hobbies-checkbox-1']"))
        )
        checkbox1.click()

        checkbox2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[@for='hobbies-checkbox-2']"))
        )
        checkbox2.click()

        checkbox3 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[@for='hobbies-checkbox-3']"))
        )
        checkbox3.click()


    def add_current_address(self):
        address_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//textarea[@id='currentAddress']"))
        )
        address_input.send_keys("Prague, Vodickova 123/34")


    def scroll_to_element_city(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='stateCity-label']"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)


    def pick_state_city(self) :

        state = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='state']"))
        )
        state.click()

        state_select = WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='react-select-3-option-0']"))
        )
        state_select.click()

        city = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='city']"))
        )
        city.click()

        city_select = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='react-select-4-option-0']"))
        )
        city_select.click()

    def submit(self):
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='submit']"))
        )
        submit_button.click()


    def Date_of_birth(self):
        dob_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='dateOfBirthInput']"))
        )
        dob_input.click()

        choose_a_yaer = WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH, "//select[@class='react-datepicker__year-select']"))
        )
        choose_a_yaer.send_keys("2000")

        choose_a_month = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//select[@class='react-datepicker__month-select']"))
        )
        choose_a_month.send_keys("December")

        choose_a_date = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--012']"))
        )
        choose_a_date.click()
        time.sleep(1)

    def scroll_to_element_select_picture(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[@for='uploadPicture']"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def download_file(self):
        download_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[@for='uploadPicture']"))
        )
        download_button.click()
        os.system("file_update.exe")




    def validation_tests(self):
        try:
            modal = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='modal-title h4' and text()='Thanks for submitting the form']"))  # Пример поиска по классу
            )
            print(modal)


            table = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//table[@class='table table-dark table-striped table-bordered table-hover']"))
            )
            self.assertTrue(table.is_displayed(), "Table is not displayed")


            student_name = self.driver.find_element(By.XPATH, "//td[text()='Student Name']/following-sibling::td")
            self.assertEqual(student_name.text, "Denis Novicov", "Student Name is incorrect")

            student_email = self.driver.find_element(By.XPATH, "//td[text()='Student Email']/following-sibling::td")
            self.assertEqual(student_email.text, "denisnovicov@example.com", "Student Email is incorrect")

            gender = self.driver.find_element(By.XPATH, "//td[text()='Gender']/following-sibling::td")
            self.assertEqual(gender.text, "Male", "Gender is incorrect")

            mobile = self.driver.find_element(By.XPATH, "//td[text()='Mobile']/following-sibling::td")
            self.assertEqual(mobile.text, "7999999999", "Mobile number is incorrect")

            dob = self.driver.find_element(By.XPATH, "//td[text()='Date of Birth']/following-sibling::td")
            self.assertEqual(dob.text, "12 December,2000", "Date of Birth is incorrect")

            subjects = self.driver.find_element(By.XPATH, "//td[text()='Subjects']/following-sibling::td")
            self.assertEqual(subjects.text, "English, Commerce", "Subjects are incorrect")

            hobbies = self.driver.find_element(By.XPATH, "//td[text()='Hobbies']/following-sibling::td")
            self.assertEqual(hobbies.text, "Sports, Reading, Music", "Hobbies are incorrect")

            picture = self.driver.find_element(By.XPATH, "//td[text()='Picture']/following-sibling::td")
            self.assertEqual(picture.text, "DN_QA.jpg", "Picture is incorrect")

            address = self.driver.find_element(By.XPATH, "//td[text()='Address']/following-sibling::td")
            self.assertEqual(address.text, "Prague, Vodickova 123/34", "Address is incorrect")

            state_city = self.driver.find_element(By.XPATH, "//td[text()='State and City']/following-sibling::td")
            self.assertEqual(state_city.text, "NCR Delhi", "State and City are incorrect")

        except TimeoutException:
            print("Модальное окно не появилось в течение времени ожидания.")
            self.fail("Модальное окно не появилось.")

    def test_form_practice(self):
        self.addFirstName()
        self.addLastName()
        self.addEmail()
        self.addNumberPhone("7999999999")
        self.Date_of_birth()
        self.scroll_to_element_select_picture()
        self.pickGender()
        self.pickSubject()
        self.pick_check_boxes()
        self.download_file()
        self.add_current_address()
        self.scroll_to_element_city()
        self.pick_state_city()
        self.submit()
        self.validation_tests()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()