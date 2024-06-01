from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, 'checkout')
    CONTINUE_SHOPPING_BUTTON = (By.ID, 'continue-shopping')

    def proceed_to_checkout(self):
        self.find_element(*self.CHECKOUT_BUTTON).click()

    def return_to_inventory(self):
        self.find_element(*self.CONTINUE_SHOPPING_BUTTON).click()

    def get_Cart_item_names(self):
        items = self.find_elements(By.CLASS_NAME, 'inventory_item_name')
        names = []
        for item in items:
            name = item.text
            names.append(name)
        return names

    def get_Cart_item_prices(self):
        items = self.find_elements(By.CLASS_NAME, 'inventory_item_price')
        prices = []
        for item in items:
            price = item.text
            prices.append(price)
        return prices

    def remove_item(self, item_name):
        remove_button = (By.XPATH, f"//div[text()='{item_name}']/ancestor::div[@class='cart_item']//button")
        self.find_element(*remove_button).click()

    def check_existence_of_item(self, item_name):
        item_locator = (By.XPATH, f"//div[text()='{item_name}']")
        return self.is_visible(*item_locator)

