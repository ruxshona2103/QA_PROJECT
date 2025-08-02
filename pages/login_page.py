from selenium.webdriver.common.by import By
from base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.XPATH, '//input[@id="userName"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@id="login"]')
    ERROR_MESSAGE = (By.XPATH, '//p[@id="name"]')


    def enter_username(self, username):
        self.input_text(self.USERNAME_INPUT, username)


    def enter_password(self, password):
        self.input_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)