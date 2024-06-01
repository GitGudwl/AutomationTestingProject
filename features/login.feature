Feature: Login
    As a user
    I want to be able to login to my account
    So that I can access my personalized content
    @positive
    Scenario: Attempted login with valid credentials
        Given I am on the login page
        When I fill in "username" with "standard_user"
        And I fill in "Password" with "secret_sauce"
        And I press "Login"
        Then I should see the head to inventory page

    @negative
    Scenario Outline: Attempted login with invalid credentials and some empty data
        Given I am on the login page
        When I fill in "username" with "<username>"
        And I fill in "Password" with "<password>"
        And I press "Login"
        Then I should see the error message "<error_message>"

        Examples:
            | username      | password        | error_message                                                             |
            | standard      | bond123         | Epic sadface: Username and password do not match any user in this service |
            |               |                 | Epic sadface: Username and password are required                          |
            | standard_user | standarduser321 | Epic sadface: Username and password do not match any user in this service |
            | standard_user |                 | Epic sadface: Password is required                                        |
            | standard_bond | secret_sauce    | Epic sadface: Username and password do not match any user in this service |
            |               | secret_sauce    | Epic sadface: Username is required                                        |
            | standard_bond |                 | Epic sadface: Password is required                                        |
            |               | standarduser321 | Epic sadface: Username is required                                        |
