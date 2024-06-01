from behave import given, when, then
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@given('I am on the login page')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('https://www.saucedemo.com')
    context.login_page = LoginPage(context.browser)
    assert "https://www.saucedemo.com/" in context.browser.current_url

@when('I fill in "username" with "{username}"')
def step_impl(context, username):
    context.login_page.fill_username(username)

@when('I fill in "Password" with "{pwd}"')
def step_impl(context,pwd):
    context.login_page.fill_password(pwd)

@when('I press "Login"')
def step_impl(context):
    context.login_page.click_login()

@then('I should see the head to inventory page')
def step_impl(context):
    context.inventory_page = InventoryPage(context.browser)
    assert "inventory.html" in context.browser.current_url
    
@then('I should see the error message "{error_message}"')
def step_impl(context, error_message):
    real_error_message = context.login_page.get_error_message()
    assert error_message == real_error_message

@when(u'I fill in "username" with ""')
def step_impl(context):
    pass


@when(u'I fill in "Password" with ""')
def step_impl(context):
    pass