from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, 'user-name')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')

    def login(self, username, password):
        self.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.find_element(*self.LOGIN_BUTTON).click()
        
    def fill_username(self, username):
        self.find_element(*self.USERNAME_INPUT).send_keys(username)
    
    def fill_password(self, password):
        self.find_element(*self.PASSWORD_INPUT).send_keys(password)
    
    def click_login(self):
        self.find_element(*self.LOGIN_BUTTON).click()
    
    def get_error_message(self):
        error_message = self.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
        return error_message
