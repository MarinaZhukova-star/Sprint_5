from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import (BUTTON_PLACE_AN_AD, MODAL_OUTH, BUTTON_LOGIN_REGISTRATION, LOGIN_BUTTON, AVATAR_USER, BUTTON_ADD_AD, PRODUCT_NAME, CATEGORY_DROPDOWN_LIST,CATEGORY_VALUE, CITY_DROPDOWN_LIST, CITY_VALUE, PUBLISH_BUTTON, MY_PROFILE_BUTTON, PRODUCT_DESCRIPTION, PRICE, CONDITION_SECONDHAND, CLASS_CARD, MY_AD, INPUT_EMAIL, INPUT_PASSWORD)
from url import (URL)
from data import (BASE_EMAIL, BASE_PASSWORD)

#Создание объявления неавторизованным пользователем
class TestCreatingAd:
    def test_creting_ad_unauthorized_user(self, driver):
        
        #Зайти на сайт:
        driver.get(URL)

        #Нажать кнопку «Разместить объявление»
        driver.find_element(BUTTON_PLACE_AN_AD).click()

        #Отображается модальное окно с заголовком «Чтобы разместить объявление, авторизуйтесь»
        modal_window_for_outh = WebDriverWait(driver, 10).until
        (expected_conditions.visibility_of_element_located(MODAL_OUTH)).text
        assert modal_window_for_outh == "Чтобы разместить объявление, авторизуйтесь"


#Создание объявления авторизованным пользователем
    def test_creting_ad_authorized_user(self, driver):
       
        #Зайти на сайт:
        driver.get(URL)

        #Нажать на кнопку "Вход и регистрация"
        driver.find_element(BUTTON_LOGIN_REGISTRATION).click()

        #Ожидание открытия формы "Войти" и нажатие кнопки "Нет аккаунта"
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(LOGIN_BUTTON))
        
        #Ввести e-mail, пароль, ввести повторно пароль
        driver.find_element(INPUT_EMAIL).send_keys(BASE_EMAIL)
        driver.find_element(INPUT_PASSWORD).send_keys(BASE_PASSWORD)
        
        #Нажать кнопку "Войти"
        driver.find_element(LOGIN_BUTTON).click()

        #Ожидание перехода на главную страницу
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AVATAR_USER))

        #Нажать кнопку «Разместить объявление»
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(BUTTON_ADD_AD))
        driver.find_element(BUTTON_ADD_AD).click()

        #Заполнить поля формы: «Название», «Описание товара», «Стоимость»
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(PRODUCT_NAME))
        driver.find_element(PRODUCT_NAME).send_keys("Ford Focus II")
        driver.find_element(PRODUCT_DESCRIPTION).send_keys("Автомобиль с пробегом 2007 года")
        driver.find_element(PRICE).send_keys(str("500000"))

        #Выбрать из Dropdown «Категорию» и «Город»
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(CATEGORY_DROPDOWN_LIST)).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(CATEGORY_VALUE)).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(CITY_DROPDOWN_LIST)).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(CITY_VALUE)).click()

        #Выбрать RabioButton «Состояние товара»
        driver.find_element(CONDITION_SECONDHAND).click()
        
        #Нажать кнопку «Опубликовать»
        driver.find_element(PUBLISH_BUTTON).click()

        #Перейти в профиль пользователя
        driver.find_element(MY_PROFILE_BUTTON).click()

        #Проверить: в блоке «Мои объявления» отображается созданное объявление
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MY_AD))
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(CLASS_CARD))
        titles = [el.text for el in driver.find_elements(CLASS_CARD)]
        assert "Ford Focus II" in titles



