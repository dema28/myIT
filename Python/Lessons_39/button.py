# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.maximize_window()
#
#
# driver.get("https://demoqa.com/buttons")
# time.sleep(5)
#
# try:
#
#     # button = driver.find_element(By.XPATH, "//h1[text()='Buttons']")
#     # print(f"заголовок {button.text} найден")
#
#
#     buttonClickMy = (WebDriverWait(driver, 10)
#                      .until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Click Me']"))))
#     buttonClickMy.click()
#     print(f"заголовок {buttonClickMy.text} найден")
#     text = driver.find_element(By.ID, "dynamicClickMessage")
#     print(f"заголовок {text.text} найден")
#
#     assert message.text == buttonClickMy, "ghgh"
#     print("Тест пройден успешно")
#
#
#
#
#
#     buttonRightClickMe = (WebDriverWait(driver, 10)
#                           .until(EC.element_to_be_clickable((By.XPATH, "//*[@id='rightClickBtn']"))))
#     buttonRightClickMe.click()
#
#     buttonDableClick = (WebDriverWait(driver, 10)
#                           .until(EC.element_to_be_clickable((By.XPATH, "//*[@id='doubleClickBtn']"))))
#     buttonDableClick.click()
#
#     time.sleep(3)
#     print("Good")
#
#
#
#
# except Exception as e:
#     print(f"error: {e}")
#
#
# finally:
#     driver.quit()
#
#
#
#
#
# Find and click the "Secondary" button
# secondary_button = (WebDriverWait(driver, 10)
#                     .until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-secondary']"))))
# secondary_button.click()


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome()
driver.implicitly_wait(10)  # Неявное ожидание элементов
driver.maximize_window()  # Максимизация окна браузера

# Переход на страницу
driver.get("https://demoqa.com/buttons")
time.sleep(5)  # Пауза для загрузки страницы

try:
    # Нажатие на кнопку "Click Me"
    buttonClickMe = (WebDriverWait(driver, 10)
                     .until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Click Me']"))))
    buttonClickMe.click()
    print(f"Кнопка '{buttonClickMe.text}' найдена и нажата")

    # Проверка сообщения после нажатия кнопки
    text = driver.find_element(By.ID, "dynamicClickMessage")
    print(f"Сообщение: '{text.text}'")

    # Проверка, что сообщение соответствует ожидаемому
    assert text.text == "You have done a dynamic click", "Сообщение не соответствует ожидаемому"
    print("Тест на кнопку 'Click Me' пройден успешно")

    # Нажатие на кнопку "Right Click Me"
    buttonRightClickMe = (WebDriverWait(driver, 10)
                          .until(EC.element_to_be_clickable((By.XPATH, "//*[@id='rightClickBtn']"))))
    buttonRightClickMe.click()
    print(f"Кнопка 'Right Click Me' найдена и нажата")

    # Проверка сообщения после нажатия правой кнопки
    right_click_message = driver.find_element(By.ID, "rightClickMessage")
    print(f"Сообщение: '{right_click_message.text}'")

    # Нажатие на кнопку "Double Click Me"
    buttonDoubleClick = (WebDriverWait(driver, 10)
                          .until(EC.element_to_be_clickable((By.XPATH, "//*[@id='doubleClickBtn']"))))
    buttonDoubleClick.click()
    print(f"Кнопка 'Double Click Me' найдена и нажата")

    # Проверка сообщения после двойного нажатия
    double_click_message = driver.find_element(By.ID, "doubleClickMessage")
    print(f"Сообщение: '{double_click_message.text}'")

    # Нажатие на кнопку "Secondary"
    secondary_button = (WebDriverWait(driver, 10)
                        .until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-secondary']"))))
    secondary_button.click()
    print("Кнопка 'Secondary' найдена и нажата")

    time.sleep(3)  # Пауза для визуальной проверки
    print("Все тесты выполнены успешно")

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    # Закрытие браузера
    driver.quit()