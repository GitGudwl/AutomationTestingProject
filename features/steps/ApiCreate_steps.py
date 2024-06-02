# features/steps/create_steps.py

from behave import given, when, then
from helpers.api_helper import ApiHelper
from helpers.Json_helper import JsonHelper

@given(u'I have a new user data located at "{path}" with generated email')
def step_impl(context, path):
    # Load user data from JSON file
    context.user_data = JsonHelper.load(path)
    # modified the email address to avoid conflict with existing data
    context.user_data['email'] = JsonHelper.random_email(10)

@when('I send a POST request to "{endpoint}" with app id: "{appid}"')
def step_impl(context, appid, endpoint):
    # Send POST request with user data
    ApiHelper.set_endpoint()
    ApiHelper.set_app_id(appid)
    context.response = ApiHelper.post(context.user_data)

@then('the response status code should be {status_code:d}')
def step_impl(context, status_code):
    print(ApiHelper.ENDPOINT)
    print(context.response.json())
    print(context.response.status_code)
    
    assert context.response.status_code == status_code

@then('the response should contain the user data')
def step_impl(context):
    response_json = context.response.json()
    print(response_json)
    assert 'id' in response_json
    # Check if user data in the response matches the data from the JSON file
    assert response_json['firstName'] == context.user_data['firstName']
    assert response_json['lastName'] == context.user_data['lastName']
    assert response_json['email'] == context.user_data['email']

@then(u'the response should contain error "{error_type}" with value "{error_message}"')
def step_impl(context,error_type, error_message):
    response_json = context.response.json()
    print(response_json)
    assert error_type in response_json['error']
    #check if the response include 'data' key
    if 'data' in response_json:
        assert str(response_json['data'])[1:-1]== error_message

@given(u'I have a new user data located at "{path}" without generated email')
def step_impl(context, path):
    # Load user data from JSON file
    context.user_data = JsonHelper.load(path)