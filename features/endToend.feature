Feature: Sauce Demo End-to-End Testing

    Scenario: End to end testing of the Sauce Demo website
        Given the user is on the login page
        When the user logs in with with "standard_user" username and password "secret_sauce"
        Then the user should be logged in successfully
        When the user adds items to the cart
        And the user proceeds to checkout
        And the user completes the checkout process with credentials first name "Zahri", last name "Hidayat", postal code "12345"
        Then the user should see the order confirmation
        Then the user click back to home button
        Then the user should be navigated to the inventory page
        When the user logs out
        Then the user should be logged out successfully

