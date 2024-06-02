Feature: Api testing for create endpoint

    Scenario: create new user
        Given I have a new user
        When I send a POST request to "/users"
        Then the response status code should be 201
        And the response should contain the user data
    
    