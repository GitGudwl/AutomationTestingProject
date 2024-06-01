Feature: Checkout Page functionality testing

    @positive
    Scenario: User fills in the checkout form with valid credentials
        Given the user is logged in and has items in the cart
        When the user proceeds to checkout from the cart page
        Then the user should be on the checkout page
        Then the user fill in the form "name" with "<name>"
        Then the user fill the "lastName" with "<lastName>"
        Then The user fill the "zipcode" with "<zip>"
        Then the user clicks on the continue button
        Then the user should be on the checkout step 2 page
        Then the user click on the finish button
        Then the user should see the message "Thank you for your order"

    @negative
    Scenario Outline: user did not fill some of the checkout form element
        Given the user is logged in and has items in the cart
        When the user proceeds to checkout from the cart page
        Then the user should be on the checkout page
        Then the user fill in the form "name" with "<name>"
        Then the user fill the "lastName" with "<lastName>"
        Then The user fill the "zipcode" with "<zip>"
        Then the user clicks on the continue button
        Then the user should see an error message "<error_message>"

        Examples:
            | name | lastName | zip   | error_message                                 |
            | Jane |          |       | Error: Last Name and Postal Code is required  |
            | Jane | Doe      |       | Error: Postal Code is required                |
            |      | Doe      | 12345 | Error: First Name is required                 |
            |      | Doe      |       | Error: First Name and Postal Code is required |
            |      | Doe      | 12345 | Error: First Name is required                 |
            | Jack |          | 67890 | Error: Last Name is required                  |
            |      |          | 12345 | Error: First Name and Last Name is required   |
            |      |          |       | Error: Data is required                       |