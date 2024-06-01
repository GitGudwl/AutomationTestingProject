from behave import when, then
from pages.base_page import BasePage

@when(u'I click on the logout button')
def step_impl(context):
    context.base_page = BasePage(context.browser)
    context.base_page.logout()

@then(u'I should be redirected to the login page')
def step_impl(context):
    assert "https://www.saucedemo.com/" in context.browser.current_url