# python -m pytest -v --tb=line tests/test_change_pass_page.py

import pytest
from pages.change_pass_page import ChangePassPage
from settings import url_change_page


class TestChangePassPage():
    def test_RT013_default_password_recovery_type(self, browser):
        change_pass_page = ChangePassPage(browser, url_change_page)
        change_pass_page.open()
        change_pass_page.default_password_recovery_type()

    @pytest.mark.xfail
    def test_RT014_phone_field_validation_valid_data(self, browser):
        """ Поле принимает 11-значное число в случае если первая цифра 3, 7 или 8.
        В остальных случаях поле принимает 10-значное число """
        change_pass_page = ChangePassPage(browser, url_change_page)
        change_pass_page.open()
        change_pass_page.phone_field_validation_valid_data()

    def test_RT015_email_field_validation_valid_data(self, browser):
        change_pass_page = ChangePassPage(browser, url_change_page)
        change_pass_page.open()
        change_pass_page.email_field_validation_valid_data()

    def test_RT016_go_back_button(self, browser):
        change_pass_page = ChangePassPage(browser, url_change_page)
        change_pass_page.open()
        change_pass_page.go_back_button()

    def test_RT017_link_fut_to_the_user_agreement_page(self, browser):
        change_pass_page = ChangePassPage(browser, url_change_page)
        change_pass_page.open()
        change_pass_page.link_to_the_user_agreement_page()

    def test_RT018_password_recovery_with_blank_fields(self, browser):
        change_pass_page = ChangePassPage(browser, url_change_page)
        change_pass_page.open()
        change_pass_page.password_recovery_with_blank_fields()

    def test_RT019_password_recovery_with_blank_captcha(self, browser):
        change_pass_page = ChangePassPage(browser, url_change_page)
        change_pass_page.open()
        change_pass_page.password_recovery_with_blank_fields()

    def test_RT020_sql_injection_in_a_text_field(self, browser):
        change_pass_page = ChangePassPage(browser, url_change_page)
        change_pass_page.open()
        change_pass_page.sql_injection_in_a_text_field()

