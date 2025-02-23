import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class TestPageNavigation(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://demoqa.com/text-box")  # Начальная страница

    def test_navigation(self):
        try:
            # Переход на страницу с книгами
            self.driver.get("https://demoqa.com/books")

            # Подтверждение, что мы на странице с книгами
            try:
                WebDriverWait(self.driver, 10).until(EC.title_is("ToolsQA"))  # Ожидание заголовка
                self.assertEqual(self.driver.current_url, "https://demoqa.com/books")  # Проверка URL
            except TimeoutException:
                self.fail("Страница с книгами не загрузилась вовремя")

            # Проверка наличия уникального элемента на странице
            try:
                books_header = self.driver.find_element(By.XPATH, "//div[@class='main-header' and text()='Book Store']")
                self.assertTrue(books_header.is_displayed())
            except NoSuchElementException:
                self.fail("Элемент 'Book Store' не найден на странице")

            # Возврат на предыдущую страницу
            self.driver.back()

            # Подтверждение, что мы вернулись на страницу text-box
            try:
                WebDriverWait(self.driver, 10).until(EC.title_contains("ToolsQA"))  # Ожидание заголовка
                self.assertEqual(self.driver.current_url, "https://demoqa.com/text-box")  # Проверка URL
            except TimeoutException:
                self.fail("Не удалось вернуться на страницу text-box")

        except Exception as e:
            self.fail(f"Тест завершился с ошибкой: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()