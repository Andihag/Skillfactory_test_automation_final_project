from selenium.webdriver.common.by import By

class BaseLocators:
    BODY = (By.XPATH, "//body")

class AuthPageLocators:
    AUTH_HEADING = (By.XPATH, "//h1[contains(text(),'Авторизация')]")
    AUTH_LOGO = (By.XPATH, "//section[@id='page-left']/*/div[@class='what-is-container__logo-container']/*")
    AUTH_SLOGAN = (By.XPATH,
                   "//section[@id='page-left']/*//p[contains(text(),'Персональный помощник в цифровом мире "
                   "Ростелекома')]")
    AUTH_TAB_MENU = (By.XPATH,
                     "//section[@id='page-right']/*//div[@id='t-btn-tab-phone' or @id='t-btn-tab-mail' or "
                     "@id='t-btn-tab-login' or @id='t-btn-tab-ls']")
    AUTH_USERNAME_INPUT_PLACEHOLDER_TELEPHONE = (By.XPATH, "//span[contains(text(),'Мобильный телефон')]")
    AUTH_USERNAME_INPUT = (By.XPATH, "//input[@id='username']")
    AUTH_USERNAME_INPUT_ACTIV_EMAIL = (By.XPATH, "//span[contains(text(),'Электронная почта')]")
    AUTH_FORGOT_PASSWORD_LINK = (By.XPATH, "//a[@id='forgot_password']")
    AUTH_REGISTER_LINK = (By.XPATH, "//a[@id='kc-register']")
    AUTH_USER_AGREEMENT_LINK = (By.XPATH,
                                "//span[contains(text(),'Нажимая кнопку «Войти», вы принимаете "
                                "условия')]/following-sibling::a")
    AUTH_PRIVACY_POLICY_LINK = (By.XPATH, "//a[@id='rt-footer-agreement-link']")
    AUTH_SOCIAL_VK_LINK = (By.XPATH, "//a[@id='oidc_vk']")
    AUTH_TAB_PHONE = (By.XPATH, "//div[@id='t-btn-tab-phone']")
    AUTH_ENTER_BUTTON = (By.XPATH, "//button[@id='kc-login']")
    AUTH_ERROR_ENTER_PHONE_NUMBER = (By.XPATH, "//span[contains(text(),'Введите номер телефона')]")
    AUTH_PASSWORD_INPUT = (By.XPATH, "//input[@id='password']")

class ChangePassPageLocators:
    CHANGE_PASS_HEADING = (By.XPATH, "//h1[contains(text(),'Восстановление пароля')]")
    CHANGE_PASS_USERNAME_INPUT_PLACEHOLDER_TELEPHONE = (By.XPATH, "//span[contains(text(),'Мобильный телефон')]")
    CHANGE_PASS_TAB_PHONE = (By.XPATH, "//div[@id='t-btn-tab-phone']")
    CHANGE_PASS_USERNAME_INPUT = (By.XPATH, "//input[@id='username']")
    CHANGE_PASS_USERNAME_INPUT_VALUE = (By.XPATH, "//input[@name='username']")
    CHANGE_PASS_TAB_MAIL = (By.XPATH, "//div[@id='t-btn-tab-mail']")
    CHANGE_PASS_GO_BACK_BUTTON = (By.XPATH, "//button[@id='reset-back']")
    CHANGE_PASS_PRIVACY_POLICY_LINK = (By.XPATH, "//a[@id='rt-footer-agreement-link']")
    CHANGE_PASS_CONTINUE_BUTTON = (By.XPATH, "//button[@id='reset']")
    CHANGE_PASS_ERROR_ENTER_PHONE_NUMBER = (By.XPATH, "//span[contains(text(),'Введите номер телефона')]")
    CHANGE_PASS_ERROR_INVALID_USERNAME_OR_TEXT = (
    By.XPATH, "//span[@id='form-error-message' and contains(text(),'Неверный логин или текст с картинки')]")

class RegPageLocators:
    REG_HEADING = (By.XPATH, "//h1[contains(text(),'Регистрация')]")
    REG_FIRST_NAME_INPUT_PAGE_RIGHT = (
    By.XPATH, "//section[@id='page-right']//span[contains(text(),'Имя')]/preceding-sibling::input")
    REG_REGISTER_BUTTON_PAGE_RIGHT = (
    By.XPATH, "//section[@id='page-right']//span[contains(text(),'Зарегистрироваться')]")
    REG_USER_AGREEMENT_LINK_PAGE_RIGHT = (By.XPATH,
                                          "//section[@id='page-right']//span[contains(text(),'Нажимая кнопку "
                                          "«Зарегистрироваться», вы принимаете условия')]/following-sibling::a")
    REG_FIRST_NAME_INPUT = (By.XPATH, "//span[contains(text(),'Имя')]/preceding-sibling::input")
    REG_ERROR_FIRST_NAME_INPUT = (
    By.XPATH, "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")
    REG_EMAIL_PHONE_INPUT = (By.XPATH, "//input[@id='address']")
    REG_EMAIL_PHONE_INPUT_VALUE = (By.XPATH, "//input[@type='hidden' and @name='address']")
    REG_ERROR_INVALID_EMAIL_OR_PHONE_INPUT = (
    By.XPATH, "//span[contains(text(),'Введите телефон в формате +7ХХХХХХХХХХ или +375XXX')]")
    REG_PASSWORD_INPUT = (By.XPATH, "//input[@id='password']")
    REG_ERROR_INVALID_PASSWORD_INPUT = (
    By.XPATH, "//span[contains(text(),'Пароль должен') or contains(text(),'Длина пароля')]")
    REG_LAST_NAME_INPUT = (By.XPATH, "//span[contains(text(),'Фамилия')]/preceding-sibling::input")
    REG_PASSWORD_CONFIRM_INPUT = (By.XPATH, "//input[@id='password-confirm']")
    REG_ENTER_BUTTON = (
    By.XPATH, "//button[@class='rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded register-form__reg-btn']")
    REG_USER_AGREEMENT_LINK = (By.XPATH,
                               "//span[contains(text(),'Нажимая кнопку «Зарегистрироваться», "
                               "вы принимаете условия')]/following-sibling::a")
    REG_PRIVACY_POLICY_LINK = (By.XPATH, "//a[@id='rt-footer-agreement-link']")
    REG_ERROR_PASSWORD_DONT_MATCH = (By.XPATH, "//span[contains(text(),'Пароли не совпадают')]")

class EmailConfirmPageLocators:
    EMAIL_CONF_HEADING = (By.XPATH, "//p[contains(text(),'Kод подтверждения отправлен')]")

class UserAgreementPageLocators:
    USER_AGREEMENT_HEADING = (By.XPATH, "//h1[contains(text(),'Пользователь')]")

class RejectedRequestPageLocators:
    REJECTED_REQUEST_HEADING = (
    By.XPATH, "//h2[contains(text(),'Ваш запрос был отклонен из соображений безопасности.')]")
    REJECTED_REQUEST_INFO = (By.XPATH, "//div[contains(text(),'Код запроса: ')]")
