from behave import given, when, then
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.confirmation_page import ConfirmationPage

@given('the user is on the login page')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('https://www.saucedemo.com')
    context.login_page = LoginPage(context.browser)

@when('the user logs in with with "{user}" username and password "{pwd}"')
def step_impl(context,user,pwd):
    context.login_page.login(user, pwd)

@then('the user should be logged in successfully')
def step_impl(context):
    context.inventory_page = InventoryPage(context.browser)
    assert "inventory.html" in context.browser.current_url

@when('the user adds items to the cart')
def step_impl(context):
    items_to_add = [
        'sauce-labs-backpack',
        'sauce-labs-bike-light',
        'sauce-labs-bolt-t-shirt'
    ]
    context.inventory_page.add_items_to_cart(items_to_add)


@when('the user proceeds to checkout')
def step_impl(context):
    context.inventory_page.go_to_cart()
    context.cart_page = CartPage(context.browser)
    context.cart_page.proceed_to_checkout()

@when('the user completes the checkout process with credentials first name "{first_name}", last name "{last_name}", postal code "{postal_code}"')
def step_impl(context, first_name, last_name, postal_code):
    context.checkout_page = CheckoutPage(context.browser)
    context.checkout_page.fill_information(first_name, last_name, postal_code)
    context.checkout_page.continue_checkout()
    context.checkout_page.finish_checkout()

@then('the user should see the order confirmation')
def step_impl(context):
    context.confirmation_page = ConfirmationPage(context.browser)
    confirmation_text = context.confirmation_page.get_confirmation_message()

    assert confirmation_text == 'Thank you for your order!'

@then('the user click back to home button')
def step_impl(context):
    context.confirmation_page.back_to_home()

@then('the user should be navigated to the inventory page')
def step_impl(context):
    assert "inventory.html" in context.browser.current_url

@when('the user logs out')
def step_impl(context):
    context.confirmation_page.click_burger_menu_button()
    context.confirmation_page.click_logout_link()

@then('the user should be logged out successfully')
def step_impl(context):
    assert "https://www.saucedemo.com/" in context.browser.current_url
    context.browser.quit()
