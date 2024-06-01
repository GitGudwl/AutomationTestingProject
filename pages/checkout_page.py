from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, 'first-name')
    LAST_NAME_INPUT = (By.ID, 'last-name')
    POSTAL_CODE_INPUT = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')
    FINISH_BUTTON = (By.ID, 'finish')

    def fill_information(self, first_name, last_name, postal_code):
        self.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)
        self.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.find_element(*self.POSTAL_CODE_INPUT).send_keys(postal_code)
    
    def fill_name_first_name(self, first_name):
        self.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)
        
    def fill_name_last_name(self, last_name):
        self.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
    
    def fill_zip_code(self, postal_code):
        self.find_element(*self.POSTAL_CODE_INPUT).send_keys(postal_code)    

    def continue_checkout(self):
        self.find_element(*self.CONTINUE_BUTTON).click()

    def finish_checkout(self):
        self.find_element(*self.FINISH_BUTTON).click()

    def get_error_message(self):
        error_message = self.find_element(By.CSS_SELECTOR, 'h3').text
        return error_message
