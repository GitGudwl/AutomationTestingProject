from behave import given, when, then
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@given('the user is logged in and has items in the cart')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('https://www.saucedemo.com')
    context.login_page = LoginPage(context.browser)

    # Login
    context.login_page.login('standard_user', 'secret_sauce')
    assert "inventory.html" in context.browser.current_url
    
    context.inventory_page = InventoryPage(context.browser)
    # Add items to cart
    items_to_add = ['sauce-labs-backpack', 'sauce-labs-bike-light', 'sauce-labs-bolt-t-shirt']
    context.inventory_page.add_items_to_cart(items_to_add)

    # Go to cart
    context.inventory_page.go_to_cart()
    assert "cart.html" in context.browser.current_url
    context.cart_page = CartPage(context.browser)


@when('the user proceeds to checkout from the cart page')
def step_impl(context):
    context.cart_page.proceed_to_checkout()
    context.checkout_page = CheckoutPage(context.browser)


@then('the user should be on the checkout page')
def step_impl(context):
    context.checkout_page = CheckoutPage(context.browser)
    assert "checkout-step-one.html" in context.browser.current_url

@given(u'I am logged in as a user with username "standard_user" and password "secret_sauce"')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('https://www.saucedemo.com')
    context.login_page = LoginPage(context.browser)
    context.login_page.login('standard_user', 'secret_sauce')


@when(u'I visit the inventory page')
def step_impl(context):
    context.inventory_page = InventoryPage(context.browser)
    assert "inventory.html" in context.browser.current_url

