from behave import given, when, then
from pages.confirmation_page import ConfirmationPage

@then('the user fill in the form "name" with "{name}"')
def step_impl(context, name):
    context.checkout_page.fill_name_first_name(name)

@then('the user fill the "lastName" with "{lastname}"')
def step_impl(context, lastname):
    context.checkout_page.fill_name_last_name(lastname)

@then('The user fill the "zipcode" with "{zip}"')
def step_impl(context, zip):
    context.checkout_page.fill_zip_code(zip)

@then('the user clicks on the continue button')
def step_impl(context):
    context.checkout_page.continue_checkout()

@then('the user should be on the checkout step 2 page')
def step_impl(context):
    assert "checkout-step-two.html" in context.browser.current_url

@then('the user click on the finish button')
def step_impl(context):
    context.checkout_page.finish_checkout()
    context.confirmation_page = ConfirmationPage(context.browser)

@then(u'the user should see the message "{message}"')
def step_impl(context,message):
    real_message = context.confirmation_page.get_confirmation_message()
    assert message == real_message

@then('the user should see an error message "{error_message}"')
def step_impl(context, error_message):
    real_error_message = context.checkout_page.get_error_message()
    print(real_error_message)
    assert error_message == real_error_message



@then('the user fill in the form "name" with ""')
def step_impl(context):
    pass

@then('the user fill the "lastName" with ""')
def step_impl(context):
    pass

@then('The user fill the "zipcode" with ""')
def step_impl(context):
    pass

