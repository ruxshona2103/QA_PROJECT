from selenium.webdriver.common.by import By
from base_page import BasePage

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


    def enter_fullname(self, full_name):
        self.input_text(self.INPUT_FULLNAME, full_name)

    def enter_email(self, email):
        self.input_text(self.INPUT_EMAIL, email)

    def enter_crn_address(self, current_address):
        self.input_text(self.INPUT_CURRENT_ADDRESS, current_address)

    def enter_prm_adrees(self, permanent_address):
        self.input_text(self.INPUT_PERMANENT_ADDRESS, permanent_address)

    def click_btn(self):
        self.click(self.SUBMIT_BTN)


    #    ---------------------------------------------------------------------------------------------------------------


    def get_username(self):
        self.get_text(self.GET_FULLNAME)

    def get_email(self):
        self.get_text(self.GET_EMAIL)

    def get_crn_address(self):
        self.get_text(self.GET_CRN_ADDRESS)

    def get_prm_address(self):
        self.get_text(self.GET_PRMT_ADDRESS)
