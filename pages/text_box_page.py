from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TextBoxPage(BasePage):
    INPUT_FULLNAME = (By.XPATH, '//input[@id="userName"]')
    INPUT_EMAIL = (By.XPATH,  '//input[@id="userEmail"]')
    INPUT_CURRENT_ADDRESS = (By.XPATH, '//textarea[@id="currentAddress"]')
    INPUT_PERMANENT_ADDRESS = (By.XPATH, '//textarea[@id="permanentAddress"]')
    SUBMIT_BTN = (By.XPATH, '//button[@id="submit"]')
    GET_FULLNAME = (By.XPATH, '//p[@id="name"]')
    GET_EMAIL = (By.XPATH, '//p[@id="email"]')
    GET_CRN_ADDRESS = (By.XPATH, '//p[@id="currentAddress"]')
    GET_PRMT_ADDRESS = (By.XPATH, '//p[@id="permanentAddress"]')

    # ------------------------------------------------------------------------------------------------------------------

    def open(self):
        self.driver.get('https://demoqa.com/text-box')


    def input_info(self):
        self.input_text(self.INPUT_FULLNAME, "Aglamkhujayeva Ruxshona")
        self.input_text(self.INPUT_EMAIL, "ruxshonaaglamkhujayeva@gmail.com")
        self.input_text(self.INPUT_CURRENT_ADDRESS, "Tashkent city")
        self.input_text(self.INPUT_PERMANENT_ADDRESS, "Bektemir district ")



    def click_btn(self):
        self.click(self.SUBMIT_BTN)


    #    ---------------------------------------------------------------------------------------------------------------

    def get_info(self):
        self.get_text(self.GET_FULLNAME)
        self.get_text(self.GET_EMAIL)
        self.get_text(self.GET_CRN_ADDRESS)
        self.get_text(self.GET_PRMT_ADDRESS)
