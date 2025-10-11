from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import (BUTTON_LOGIN_REGISTRATION, NO_ACCOUNT, CREATE_ACCOUNT, AVATAR_USER, NAME_USER)

driver = webdriver.Chrome()


#регистрация пользователя
class TestRegistration:
    #Регистрация пользователя
    def test_success_registration(self, driver):
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
        driver.find_element(By.ID, "submintPassword").send_keys("123456")

        #Нажать кнопку "Создать аккаунт"
        driver.find_element(CREATE_ACCOUNT).click()

        #Выполнен переход на главную страницу, проверить видимость аватара и имени пользователя рядом с кнопкой «Разместить объявление»
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AVATAR_USER))
        display_name = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(NAME_USER)).text
        assert display_name == 'User'

        #Закрыть Браузер
        driver.quit()


#Регистрация пользователя c email не по маске  *******@*******.***
    def test_user_registration_with_email_without_mask(self, driver):
        driver = webdriver.Chrome()
        #Зайти на сайт:
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        #Нажать на кнопку "Вход и регистрация"
        driver.find_element(BUTTON_LOGIN_REGISTRATION).click()

        #Ожидание открытия формы "Войти" и нажатие кнопки "Нет аккаунта"
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(NO_ACCOUNT))
        driver.find_element(NO_ACCOUNT).click()

        #Ввести e-mail не по маске *******@*******.*** и нажать на кнопку "Создать аккаунт"
        driver.find_element(By.ID, "email").send_keys("marishka.yandex.ru")
        driver.find_element(CREATE_ACCOUNT).click()

        #Поля "Email", "Пароль", "Повторите пароль" выделены красным, под полем "Email" отображается сообщение «Ошибка»
        error = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, '//span[text()="Ошибка"]'))).text
        assert error == "Ошибка"

        #Закрыть Браузер
        driver.quit()

#Регистрация уже существующего пользователя
    def test_registration_existing_user(self, driver):
        driver = webdriver.Chrome()
        #Зайти на сайт:
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        #Нажать на кнопку "Вход и регистрация"
        driver.find_element(BUTTON_LOGIN_REGISTRATION).click()

        #Ожидание открытия формы "Войти" и нажатие кнопки "Нет аккаунта"
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(NO_ACCOUNT))
        driver.find_element(NO_ACCOUNT).click()

        #Ввести e-mail, пароль, ввести повторно пароль уже существующего пользователя
        driver.find_element(By.ID, "email").send_keys("marishka@yandex.ru")
        driver.find_element(By.ID, "password").send_keys("123456")
        driver.find_element(By.ID, "submintPassword").send_keys("123456")

        #Нажать кнопку "Создать аккаунт"
        driver.find_element(CREATE_ACCOUNT).click()

        #Поля "Email", "Пароль", "Повторите пароль" выделены красным, под полем "Email" отображается сообщение «Ошибка»
        error = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, '//span[text()="Ошибка"]'))).text
        assert error == "Ошибка"
        
        #Закрыть Браузер
        driver.quit()