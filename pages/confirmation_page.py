from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support import expected_conditions as EC

class ConfirmationPage(BasePage):
    CONFIRMATION_TEXT = (By.CLASS_NAME, 'complete-header')

    def get_confirmation_message(self):
        return self.find_element(*self.CONFIRMATION_TEXT).text

    def back_to_home(self):
        wait = WebDriverWait(self.browser, 10)
        finish_button = wait.until(EC.element_to_be_clickable((By.ID, "back-to-products")))
        finish_button.click()