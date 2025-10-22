from selenium.webdriver.common.by import By

#Вход и регистрация
BUTTON_LOGIN_REGISTRATION = (By.XPATH, './/button[text()="Вход и регистрация"]')
NO_ACCOUNT = (By.XPATH, './/button[text()="Нет аккаунта"]')
CREATE_ACCOUNT = (By.XPATH, '//button[text()="Создать аккаунт"]')
LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]')
LOGOUT_BUTTON = (By.XPATH, '//button[text()="Выйти"]')
ERROR = (By.XPATH, '//span[text()="Ошибка"]')

#Кнопки
BUTTON_PLACE_AN_AD = (By.XPATH, './/button[text()="Разместить объявление"]')
BUTTON_APPLY = (By.XPATH, './/button[text()="Применить"]')

#Данные пользователя.Аватар
AVATAR_USER = (By.CSS_SELECTOR, './/button.circleSmall')
NAME_USER = (By.XPATH, './/h3[text()="User."]')

#Разместить объявление
MODAL_OUTH = (By.XPATH, './/h1[text()="Чтобы разместить объявление, авторизуйтесь"]')

BUTTON_ADD_AD = (By.XPATH, './/button[text()="Разместить объявление"]')
PRODUCT_NAME = (By.XPATH, './/input[@placeholder="Название"]')

CATEGORY_DROPDOWN_LIST = (By.XPATH, './/input[@name="category"]')
CATEGORY_VALUE = (By.XPATH, './/button[normalize-space()="Авто"]')

CITY_DROPDOWN_LIST = (By.XPATH, './/input[@name="city"]')
CITY_VALUE = (By.XPATH, './/button[normalize-space()="Казань"]')

PUBLISH_BUTTON = (By.XPATH, './/button[text()="Опубликовать"]')
MY_PROFILE_BUTTON = (By.CLASS_NAME, "circleSmall").click()

PRODUCT_DESCRIPTION = (By.XPATH, '//textarea[@placeholder="Описание товара"]')
PRICE = (By.XPATH, '//input[@placeholder="Стоимость"]')
CONDITION_SECONDHAND = (By.XPATH, '//input[@name="condition" and @value="Б/У"]')
CLASS_CARD = (By.XPATH, "//div[contains(@class,'card')]")
MY_AD = (By.XPATH, "//h1['Мои объявления']")