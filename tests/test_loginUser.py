from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import (BUTTON_LOGIN_REGISTRATION, NO_ACCOUNT,LOGIN_BUTTON, AVATAR_USER, NAME_USER)
from url import (URL)
from data import (BASE_EMAIL, BASE_PASSWORD)

#Login пользователя
class TestLoginUser:
    def test_user_login(self, driver):

        #Зайти на сайт:
        driver.get(URL)

        #Нажать на кнопку "Вход и регистрация"
        driver.find_element(BUTTON_LOGIN_REGISTRATION).click()

        #Ожидание открытия формы "Войти"
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(LOGIN_BUTTON))
        
        #Ввести e-mail, пароль, ввести повторно пароль
        driver.find_element(By.ID, "email").send_keys(BASE_EMAIL)
        driver.find_element(By.ID, "password").send_keys(BASE_PASSWORD)
        
        #Нажать кнопку "Войти"
        driver.find_element(LOGIN_BUTTON).click()

        #Выполнен переход на главную страницу, проверить видимость аватара и имени пользователя рядом с кнопкой «Разместить объявление»
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AVATAR_USER))
        display_name = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(NAME_USER)).text
        assert display_name == 'User'

