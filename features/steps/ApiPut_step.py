# features/steps/put_steps.py

import json
from behave import given, when, then
from helpers.api_helper import ApiHelper

@given('the PUT header "app-id" is "{app_id}"')
def step_impl(context, app_id):
    ApiHelper.set_app_id(app_id)

@given('the PUT request body is read from "{file_name}"')
def step_impl(context, file_name):
    with open(f'features/data/Put/{file_name}', 'r') as file:
        context.request_body = json.load(file)

@when('I make a PUT request to "{user_id}"')
def step_impl(context, user_id):
    ApiHelper.set_endpoint(user_id)
    context.response = ApiHelper.put(context.request_body)

@then('the PUT status code should be {status_code:d}')
def step_impl(context, status_code):
    assert context.response.status_code == status_code

@then('the PUT response should contain "{key}" with value "{value}"')
def step_impl(context, key, value):
    response_json = context.response.json()
    assert response_json[key] == value

@given(u'the PUT header "app-id" is ""')
def step_impl(context):
    ApiHelper.set_app_id("")