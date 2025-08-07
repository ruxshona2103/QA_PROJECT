from selenium.webdriver.common.by import By
from pages.base_page  import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.XPATH, '//input[@id="userName"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@id="login"]')
    ERROR_MSG = (By.XPATH, "//form[@id='userForm']//p[@id='name']")

    def open(self):
        self.driver.get("https://demoqa.com/login")

    def login(self, username, password):
        self.input_text(self.USERNAME_INPUT, username)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MSG)

    def get_input_border_color(self, locator):
        element = self.driver.find_element(locator)
        return element.value_of_css_property("border-color")