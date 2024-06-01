Feature: Inventory page functionallity test

    Scenario: User can view all inventory items
        Given I am logged in as a user with username "standard_user" and password "secret_sauce"
        When I visit the inventory page
        Then I should see all inventory items

    Scenario: User can add an item to the cart
        Given I am logged in as a user with username "standard_user" and password "secret_sauce"
        When I visit the inventory page
        And I click the "Add to cart" button for the item with name "Sauce Labs Backpack"
        Then i clik the cart button
        Then I should see the item with name "Sauce Labs Backpack" in the cart

    Scenario: User can sort inventory items by price low to high
        Given I am logged in as a user with username "standard_user" and password "secret_sauce"
        When I visit the inventory page
        And I sort the inventory items by price low to high
        Then I should see the inventory items sorted by price low to high

    Scenario: User can sort inventory items by name A to Z
        Given I am logged in as a user with username "standard_user" and password "secret_sauce"
        When I visit the inventory page
        And I sort the inventory items by name A to Z
        Then I should see the inventory items sorted by name A to Z

    Scenario: User can sort inventory items by name Z to A
        Given I am logged in as a user with username "standard_user" and password "secret_sauce"
        When I visit the inventory page
        And I sort the inventory items by name Z to A
        Then I should see the inventory items sorted by name Z to A

    Scenario: User can sort inventory items by price high to low
        Given I am logged in as a user with username "standard_user" and password "secret_sauce"
        When I visit the inventory page
        And I sort the inventory items by price high to low
        Then I should see the inventory items sorted by price high to low