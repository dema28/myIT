import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()


driver.get("https://demoqa.com/buttons")
time.sleep(5)

try:

    # button = driver.find_element(By.XPATH, "//h1[text()='Buttons']")
    # print(f"заголовок {button.text} найден")


    buttonClickMy = (WebDriverWait(driver, 10)
                     .until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Click Me']"))))
    buttonClickMy.click()
    print(f"заголовок {buttonClickMy.text} найден")
    text = driver.find_element(By.ID, "dynamicClickMessage")
    print(f"заголовок {text.text} найден")

    assert message.text == buttonClickMy, "ghgh"
    print("Тест пройден успешно")



    #
    # buttonRightClickMe = (WebDriverWait(driver, 10)
    #                       .until(EC.element_to_be_clickable((By.XPATH, "//*[@id='rightClickBtn']"))))
    # buttonRightClickMe.click()
    #
    # buttonDableClick = (WebDriverWait(driver, 10)
    #                       .until(EC.element_to_be_clickable((By.XPATH, "//*[@id='doubleClickBtn']"))))
    # buttonDableClick.click()

    time.sleep(3)
    print("Good")




except Exception as e:
    print(f"error: {e}")


finally:
    driver.quit()





# # Find and click the "Secondary" button
# secondary_button = (WebDriverWait(driver, 10)
#                     .until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-secondary']"))))
# secondary_button.click()
