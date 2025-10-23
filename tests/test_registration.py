from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import (BUTTON_LOGIN_REGISTRATION, NO_ACCOUNT, CREATE_ACCOUNT, AVATAR_USER, NAME_USER, ERROR, INPUT_EMAIL, INPUT_PASSWORD, INPUT_SUBMINT_PASSWORD)
from url import (URL)
from data import (BASE_EMAIL, BASE_PASSWORD, ERROR_EMAIL)
from helpers import generate_email

#регистрация пользователя
class TestRegistration:
    #Регистрация пользователя
    def test_success_registration(self, driver):

        #Зайти на сайт:
        driver.get(URL)

        #Нажать на кнопку "Вход и регистрация"
        driver.find_element(BUTTON_LOGIN_REGISTRATION).click()

        #Ожидание открытия формы "Войти" и нажатие кнопки "Нет аккаунта"
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(NO_ACCOUNT))
        driver.find_element(NO_ACCOUNT).click()
        
        #Ввести e-mail, пароль, ввести повторно пароль
        email = generate_email()
        driver.find_element(INPUT_EMAIL).send_keys(email)
        driver.find_element(INPUT_PASSWORD).send_keys(BASE_PASSWORD)
        driver.find_element(INPUT_SUBMINT_PASSWORD).send_keys(BASE_PASSWORD)

        #Нажать кнопку "Создать аккаунт"
        driver.find_element(CREATE_ACCOUNT).click()

        #Выполнен переход на главную страницу, проверить видимость аватара и имени пользователя рядом с кнопкой «Разместить объявление»
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AVATAR_USER))
        display_name = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(NAME_USER)).text
        assert display_name == 'User'




#Регистрация пользователя c email не по маске  *******@*******.***
    def test_user_registration_with_email_without_mask(self, driver):

        #Зайти на сайт:
        driver.get(URL)

        #Нажать на кнопку "Вход и регистрация"
        driver.find_element(BUTTON_LOGIN_REGISTRATION).click()

        #Ожидание открытия формы "Войти" и нажатие кнопки "Нет аккаунта"
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(NO_ACCOUNT))
        driver.find_element(NO_ACCOUNT).click()

        #Ввести e-mail не по маске *******@*******.*** и нажать на кнопку "Создать аккаунт"
        driver.find_element(INPUT_EMAIL).send_keys(ERROR_EMAIL)
        driver.find_element(CREATE_ACCOUNT).click()

        #Поля "Email", "Пароль", "Повторите пароль" выделены красным, под полем "Email" отображается сообщение «Ошибка»
        error = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((ERROR))).text
        assert error == "Ошибка"



#Регистрация уже существующего пользователя
    def test_registration_existing_user(self, driver):

        #Зайти на сайт:
        driver.get(URL)

        #Нажать на кнопку "Вход и регистрация"
        driver.find_element(BUTTON_LOGIN_REGISTRATION).click()

        #Ожидание открытия формы "Войти" и нажатие кнопки "Нет аккаунта"
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(NO_ACCOUNT))
        driver.find_element(NO_ACCOUNT).click()

        #Ввести e-mail, пароль, ввести повторно пароль уже существующего пользователя
        driver.find_element(INPUT_EMAIL).send_keys(BASE_EMAIL)
        driver.find_element(INPUT_PASSWORD).send_keys(BASE_PASSWORD)
        driver.find_element(INPUT_SUBMINT_PASSWORD).send_keys(BASE_PASSWORD)

        #Нажать кнопку "Создать аккаунт"
        driver.find_element(CREATE_ACCOUNT).click()

        #Поля "Email", "Пароль", "Повторите пароль" выделены красным, под полем "Email" отображается сообщение «Ошибка»
        error = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((ERROR))).text
        assert error == "Ошибка"
