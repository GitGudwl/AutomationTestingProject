Feature:Logout
    As a user
    I want to be able to logout from my account
    So that I can securely exit my session


    Scenario: Successful logout from account
        Given I am logged in as a user with username "standard_user" and password "secret_sauce"
        When I click on the logout button
        Then I should be redirected to the login page