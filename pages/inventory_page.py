from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class InventoryPage(BasePage):
    ITEM_BUTTON_PREFIX = "add-to-cart-"
    PRODUCT_SORT_SELECTOR = (By.CLASS_NAME, 'product_sort_container')

    def add_items_to_cart(self, item_names):
        for item in item_names:
            add_to_cart_button = (By.ID, f'{self.ITEM_BUTTON_PREFIX}{item}')
            self.find_element(*add_to_cart_button).click()

    def go_to_product_details(self, item_name):
        item = self.get_all_items()
        for item in item:
            if item_name in item.find_element(By.CLASS_NAME, 'inventory_item_name').text:
                #select the href of the item than click
                item.find_element(By.TAG_NAME, 'a').click()
                break

    def get_all_items(self):
        items = self.find_elements(By.CLASS_NAME, 'inventory_item')
        return items

    def sort(self, sort_type):
        self.find_element(*self.PRODUCT_SORT_SELECTOR).click()
        name_sort_select = Select(self.find_element(*self.PRODUCT_SORT_SELECTOR))
        name_sort_select.select_by_value(sort_type)
    
    def get_all_items_prices(self):
        items = self.get_all_items()
        prices = []
        for item in items:
            price = item.find_element(By.CLASS_NAME, 'inventory_item_price').text
            prices.append(price)
        return prices
    
    def get_all_items_names(self):
        items = self.get_all_items()
        names = []
        for item in items:
            name = item.find_element(By.CLASS_NAME, 'inventory_item_name').text
            names.append(name)
        return names

    def check_sorting_names(self):
        names = self.get_all_items_names()
        sorted_names = sorted(names)
        return names == sorted_names

    def check_sorting_prices(self):
        prices = self.get_all_items_prices()
        # Convert prices to numerical values
        numerical_prices = [float(price.strip('$')) for price in prices]
        print(f"un:  {numerical_prices}")
        sorted_prices = sorted(numerical_prices)
        print(f"sorted:  {sorted_prices}")
        # Check if the sorted prices match the original order
        return numerical_prices == sorted_prices

    def check_sorting_prices_desc(self):
        prices = self.get_all_items_prices()
        # Convert prices to numerical values
        numerical_prices = [float(price.strip('$')) for price in prices]
        sorted_prices = sorted(numerical_prices, reverse=True)
        # Check if the sorted prices match the original order
        return numerical_prices == sorted_prices

    def check_sorting_names_desc(self):
        names = self.get_all_items_names()
        sorted_names = sorted(names, reverse=True)
        return names == sorted_names