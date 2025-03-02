import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestTextBox(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://demoqa.com/text-box")

    def test_add_full_name(self):
        full_name_input = self.driver.find_element(By.XPATH, "//*[@id='userName']")
        full_name_input.send_keys("Denis Novicov")

        self.assertEqual(full_name_input.get_attribute("value"), "Denis Novicov")

    def test_add_email(self):
        email_input = self.driver.find_element(By.XPATH, "//*[@id='userEmail']")
        email_input.send_keys("denisnovicov@gmail.com")

        self.assertEqual(email_input.get_attribute("value"), "denisnovicov@gmail.com")

    def test_current_address(self):
        address_input = self.driver.find_element(By.XPATH, "//*[@id='currentAddress']")
        address_input.send_keys("Prague, Chehia")

        self.assertEqual(address_input.get_attribute("value"), "Prague, Chehia")

    def test_permanent_adress(self):
        permanent_address_input = self.driver.find_element(By.XPATH, "//*[@id='permanentAddress']")
        permanent_address_input.send_keys("Brno, Kramarska")

        self.assertEqual(permanent_address_input.get_attribute("value"), "Brno, Kramarska")

    def test_submit(self):
        self.test_add_full_name()
        self.test_add_email()
        self.test_current_address()
        self.test_permanent_adress()

        submit_button = self.driver.find_element(By.XPATH, "//*[@id='submit']")
        submit_button.click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='output']"))
        )
        output = self.driver.find_element(By.XPATH, "//*[@id='output']")
        self.assertTrue(output.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()