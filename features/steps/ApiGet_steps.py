# features/steps/get_steps.py

from behave import given, when, then
from helpers.api_helper import ApiHelper

@given('the GET header "app-id" is "{app_id}"')
def step_impl(context, app_id):
    ApiHelper.set_app_id(app_id)

@when('I make a GET request to "{user_id}"')
def step_impl(context, user_id):
    ApiHelper.set_endpoint(user_id)
    context.response = ApiHelper.get()

@then('the GET status code should be {status_code:d}')
def step_impl(context, status_code):
    assert context.response.status_code == status_code

@then('the GET response should contain "{key}" with value "{value}"')
def step_impl(context, key, value):
    response_json = context.response.json()
    print(response_json[key])
    assert response_json[key] == value

@given(u'the GET header "app-id" is ""')
def step_impl(context):
    pass