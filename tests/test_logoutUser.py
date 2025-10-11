from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import (BUTTON_LOGIN_REGISTRATION, NO_ACCOUNT,LOGIN_BUTTON, AVATAR_USER, LOGOUT_BUTTON)

driver = webdriver.Chrome()

#Logout пользователя
class TestLogoutUser:
     def test_user_logout(self, driver):
        driver = webdriver.Chrome()
        #Зайти на сайт:
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        #Нажать на кнопку "Вход и регистрация"
        driver.find_element(BUTTON_LOGIN_REGISTRATION).click()

        #Ожидание открытия формы "Войти" и нажатие кнопки "Нет аккаунта"
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(NO_ACCOUNT))
        driver.find_element(NO_ACCOUNT).click()
        
        #Ввести e-mail, пароль, ввести повторно пароль
        driver.find_element(By.ID, "email").send_keys("marishka@yandex.ru")
        driver.find_element(By.ID, "password").send_keys("123456")
        
        #Нажать кнопку "Войти"
        driver.find_element(LOGIN_BUTTON).click()

        #Ожидание перехода на главную страницу
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AVATAR_USER))

        #Нажать кнопку "Войти"
        driver.find_element(LOGOUT_BUTTON).click()

        # Проверить отсутствие аватара и имени пользователя в правом верхнем углу
        button_text = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(BUTTON_LOGIN_REGISTRATION)).text
        assert button_text == "Вход и регистрация"

        #Закрыть Браузер
        driver.quit()


        

