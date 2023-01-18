from .base_page import BasePage
from .locators import BaseLocators, RegPageLocators, EmailConfirmPageLocators, UserAgreementPageLocators


class RegPage(BasePage):
    # RT021 метод проверки расположения полей ввода, кнопки "Зарегистрироваться", ссылки на пользовательское соглашение
    def location_of_input_fields_and_buttons_and_links(self):
        assert self.is_element_present(RegPageLocators.REG_FIRST_NAME_INPUT_PAGE_RIGHT), "element not found"
        assert self.is_element_present(RegPageLocators.REG_REGISTER_BUTTON_PAGE_RIGHT), "element not found"
        assert self.is_element_present(RegPageLocators.REG_USER_AGREEMENT_LINK_PAGE_RIGHT), "element not found"

    # RT022 метод проверки валидации текстового поля (ввод валидных данных)
    def text_field_validation_valid_data(self, input_text):
        self.find_element(RegPageLocators.REG_FIRST_NAME_INPUT).send_keys(input_text)
        self.find_element(BaseLocators.BODY).click()
        assert self.is_not_element_present(RegPageLocators.REG_ERROR_FIRST_NAME_INPUT), "element found"

    # RT023 метод проверки на валидацию поля ввода email или мобильного телефона (ввод валидных данных)
    def email_or_phone_field_validation_valid_data(self, input_text):
        self.find_element(RegPageLocators.REG_EMAIL_PHONE_INPUT).send_keys(input_text)
        self.find_element(BaseLocators.BODY).click()
        element = self.find_element(RegPageLocators.REG_EMAIL_PHONE_INPUT_VALUE)
        value = element.get_attribute("value")
        assert input_text == value, "email or phone do not match"
        assert self.is_not_element_present(RegPageLocators.REG_ERROR_INVALID_EMAIL_OR_PHONE_INPUT), "element found"

    # RT024 метод проверки на валидацию поля ввода пароля (ввод валидных данных)
    def password_field_validation_valid_data(self, input_text):
        self.find_element(RegPageLocators.REG_PASSWORD_INPUT).send_keys(input_text)
        self.find_element(BaseLocators.BODY).click()
        assert self.is_not_element_present(RegPageLocators.REG_ERROR_INVALID_PASSWORD_INPUT), "element found"

    # RT025 метод проверки регистрации с валидными данными
    def registration_with_valid_data(self, first_name, last_name, email_phone, password):
        self.find_element(RegPageLocators.REG_FIRST_NAME_INPUT).send_keys(first_name)
        self.find_element(RegPageLocators.REG_LAST_NAME_INPUT).send_keys(last_name)
        self.find_element(RegPageLocators.REG_EMAIL_PHONE_INPUT).send_keys(email_phone)
        self.find_element(RegPageLocators.REG_PASSWORD_INPUT).send_keys(password)
        self.find_element(RegPageLocators.REG_PASSWORD_CONFIRM_INPUT).send_keys(password)
        self.find_element(RegPageLocators.REG_ENTER_BUTTON).click()
        assert self.is_element_present(EmailConfirmPageLocators.EMAIL_CONF_HEADING), "element not found"

    # RT026 метод проверки ссылки под кнопкой "Зарегистрироваться" на страницу с пользовательским соглашением
    def link_to_the_user_agreement_page(self):
        original_window = self.browser.current_window_handle
        assert len(self.browser.window_handles) == 1
        self.find_element(RegPageLocators.REG_USER_AGREEMENT_LINK).click()
        for window_handle in self.browser.window_handles:
            if window_handle != original_window:
                self.browser.switch_to.window(window_handle)
            else:
                pass
        assert self.is_element_present(UserAgreementPageLocators.USER_AGREEMENT_HEADING), "element not found"
        assert "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html" in self.browser.current_url, \
            "url do not match"

    # RT027 метод проверки ссылки в футере на страницу с пользовательским соглашением
    def link_fut_to_the_user_agreement_page(self):
        original_window = self.browser.current_window_handle
        assert len(self.browser.window_handles) == 1
        self.find_element(RegPageLocators.REG_PRIVACY_POLICY_LINK).click()
        for window_handle in self.browser.window_handles:
            if window_handle != original_window:
                self.browser.switch_to.window(window_handle)
            else:
                pass
        assert self.is_element_present(UserAgreementPageLocators.USER_AGREEMENT_HEADING), "element not found"
        assert "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html" in self.browser.current_url, \
            "url do not match"

    # RT028 метод проверки валидации текстового поля (ввод невалидных данных)
    def text_field_validation_invalid_data(self, input_text):
        self.find_element(RegPageLocators.REG_FIRST_NAME_INPUT).send_keys(input_text)
        self.find_element(BaseLocators.BODY).click()
        assert self.is_element_present(RegPageLocators.REG_ERROR_FIRST_NAME_INPUT), "element not found"

    # RT029 метод проверки валидации поля ввода email или мобильного телефона (ввод невалидных данных)
    def email_or_phone_field_validation_invalid_data(self, input_text):
        self.find_element(RegPageLocators.REG_EMAIL_PHONE_INPUT).send_keys(input_text)
        self.find_element(BaseLocators.BODY).click()
        assert self.is_element_present(RegPageLocators.REG_ERROR_INVALID_EMAIL_OR_PHONE_INPUT), "element not found"

    # RT030 метод проверки валидации поля ввода пароля (ввод невалидных данных)
    def password_field_validation_invalid_data(self, input_text):
        self.find_element(RegPageLocators.REG_PASSWORD_INPUT).send_keys(input_text)
        self.find_element(BaseLocators.BODY).click()
        assert self.is_element_present(RegPageLocators.REG_ERROR_INVALID_PASSWORD_INPUT), "element not found"

    # RT031 метод проверки заполнения поля подтверждения пароля данными, отличными от введенных в поле ввода пароля
    def entering_data_in_the_password_confirmation_field(self, password1, password2):
        self.find_element(RegPageLocators.REG_PASSWORD_INPUT).send_keys(password1)
        self.find_element(RegPageLocators.REG_PASSWORD_CONFIRM_INPUT).send_keys(password2)
        self.find_element(RegPageLocators.REG_ENTER_BUTTON).click()
        assert self.is_element_present(RegPageLocators.REG_ERROR_PASSWORD_DONT_MATCH), "element not found"

    # RT032 метод проверки регистрации с невалидными данными
    def registration_with_invalid_data(self, first_name, last_name, email_phone, password):
        self.find_element(RegPageLocators.REG_FIRST_NAME_INPUT).send_keys(first_name)
        self.find_element(RegPageLocators.REG_LAST_NAME_INPUT).send_keys(last_name)
        self.find_element(RegPageLocators.REG_EMAIL_PHONE_INPUT).send_keys(email_phone)
        self.find_element(RegPageLocators.REG_PASSWORD_INPUT).send_keys(password)
        self.find_element(RegPageLocators.REG_PASSWORD_CONFIRM_INPUT).send_keys(password)
        self.find_element(RegPageLocators.REG_ENTER_BUTTON).click()
        assert self.is_not_element_present(EmailConfirmPageLocators.EMAIL_CONF_HEADING), "element found"