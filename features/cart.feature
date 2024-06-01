Feature: Cart Page functionality testing

    Scenario: Proceed to checkout from the cart page
        Given the user is logged in and has items in the cart
        When the user proceeds to checkout from the cart page
        Then the user should be on the checkout page

    Scenario: Return to inventory from the cart page
        Given the user is logged in and has items in the cart
        When the user returns to inventory from the cart page
        Then the user should be on the inventory page

    Scenario: Verify cart item names and prices
        Given the user is logged in and has items in the cart
        When the user checks the cart item names and prices
        Then the cart item names should be correct
        And the cart item prices should be correct

    Scenario: remove item from cart
        Given the user is logged in and has items in the cart
        When the user checks the cart item names and prices
        And the user removes an item from the cart
        Then the user check if the item is removed from the cart
