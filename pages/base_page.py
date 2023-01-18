from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from .locators import AuthPageLocators


# Конструктор класса. Принимает browser — экземпляр webdriver
class BasePage():
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        # команда для неявного ожидания со значением по умолчанию в 5c:
        self.browser.implicitly_wait(timeout)

    # метод find_element ищет один элемент и возвращает его
    def find_element(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator),
                                                       message=f"Can't find element by locator {locator}")

    # метод open открывает нужную страницу в браузере, используя метод get()
    def open(self):
        self.browser.get(self.url)

    # метод open_reg_page открывает форму регистрации в браузере, используя метод get()
    def open_reg_page(self):
        self.browser.get(self.url)
        self.find_element(AuthPageLocators.AUTH_REGISTER_LINK).click()

    # метод is_element_present перехватывает исключение
    # будет использоваться для проверки присутствия элемента на странице
    def is_element_present(self, what):
        try:
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((what)))
        except (NoSuchElementException):
            return False
        return True

    # метод is_not_element_present будет использоваться для проверки отсутствия элемента на странице
    def is_not_element_present(self, what):
        try:
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((what)))
        except (TimeoutException):
            return True
        return False


    