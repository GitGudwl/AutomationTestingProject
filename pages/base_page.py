from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find_element(self, *locator):
        return self.browser.find_element(*locator)

    def find_elements(self, *locator):
        return self.browser.find_elements(*locator)

    def click_burger_menu_button(self):
        burger_menu_button = self.find_element(By.ID, "react-burger-menu-btn")
        burger_menu_button.click()

    def click_logout_link(self):
        wait = WebDriverWait(self.browser, 10)
        logout_link = wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
        logout_link.click()
    
    def logout(self):
        self.click_burger_menu_button()
        self.click_logout_link()

    def is_visible(self, *locator):
        # Method to check if an element is visible without waiting
        elements = self.find_elements(*locator)
        return bool(elements)
    
    def go_to_cart(self):
        cart_button = self.find_element(By.CLASS_NAME, 'shopping_cart_link')
        cart_button.click()
