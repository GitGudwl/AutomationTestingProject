# features/steps/delete_steps.py

# features/steps/delete_steps.py

from behave import given, when, then
from helpers.api_helper import ApiHelper



@given('the DELETE header "app-id" is "{app_id}"')
def step_impl(context, app_id):
    ApiHelper.set_app_id(app_id)

@given('the DELETE request user ID is "{user_id}"')
def step_impl(context, user_id):
    ApiHelper.set_endpoint(user_id)
    
@when('I make a DELETE request to it')
def step_impl(context):
    context.response = ApiHelper.delete()

@then('the DELETE status code should be {status_code:d}')
def step_impl(context, status_code):
    print(context.response.status_code)
    assert context.response.status_code == status_code

@then('the DELETE response should contain "{key}" with value "{value}"')
def step_impl(context, key, value):
    response_json = context.response.json()
    print(response_json)
    assert response_json[key] == value


@given(u'the DELETE header "app-id" is ""')
def step_impl(context):
    pass