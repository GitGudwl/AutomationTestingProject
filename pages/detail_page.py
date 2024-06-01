from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DetailsPage(BasePage):
    PRODUCT_NAME = (By.CLASS_NAME, 'inventory_details_name')
    PRODUCT_DESC = (By.CLASS_NAME, 'inventory_details_desc')
    PRODUCT_PRICE = (By.CLASS_NAME, 'inventory_details_price')
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, 'btn_inventory')
    BACK_TO_PRODUCTS_BUTTON = (By.ID, 'back-to-products')

    def get_product_name(self):
        return self.find_element(*self.PRODUCT_NAME).text

    def get_product_description(self):
        return self.find_element(*self.PRODUCT_DESC).text

    def get_product_price(self):
        return self.find_element(*self.PRODUCT_PRICE).text

    def add_to_cart(self):
        self.find_element(*self.ADD_TO_CART_BUTTON).click()

    def back_to_products(self):
        self.find_element(*self.BACK_TO_PRODUCTS_BUTTON).click()
