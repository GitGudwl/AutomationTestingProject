Feature: Detail page functionallity test

    Scenario Outline: User can see the detail page of each product
        Given I am logged in as a user with username "standard_user" and password "secret_sauce"
        When I visit the inventory page
        And I click on the product with name "<product_name>"
        Then I should see the detail page of the product wit all its content and the correct product name "<product_name>", "<price>", "<description>"

        Examples:
            | product_name                      | price  | description                                                                                                                                                            |
            | Sauce Labs Backpack               | $29.99 | carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.                                 |
            | Sauce Labs Bike Light             | $9.99  | A red light isn't the desired state in testing but it sure helps when riding your bike at night. Water-resistant with 3 lighting modes, 1 AAA battery included.        |
            | Sauce Labs Bolt T-Shirt           | $15.99 | Get your testing superhero on with the Sauce Labs bolt T-shirt. From American Apparel, 100% ringspun combed cotton, heather gray with red bolt.                        |
            | Sauce Labs Fleece Jacket          | $49.99 | It's not every day that you come across a midweight quarter-zip fleece jacket capable of handling everything from a relaxing day outdoors to a busy day at the office. |
            | Sauce Labs Onesie                 | $7.99  | Rib snap infant onesie for the junior automation engineer in development. Reinforced 3-snap bottom closure, two-needle hemmed sleeved and bottom won't unravel.        |
            | Test.allTheThings() T-Shirt (Red) | $15.99 | This classic Sauce Labs t-shirt is perfect to wear when cozying up to your keyboard to automate a few tests. Super-soft and comfy ringspun combed cotton.              |



    Scenario Outline: User can add a product to the cart from each detail page
        Given I am logged in as a user with username "standard_user" and password "secret_sauce"
        When I visit the inventory page
        And I click on the product with name "<product_name>"
        And I click on the "Add to cart" button
        Then I go to the cart page
        Then I should see the product "<product_name>" in the cart

        Examples:
            | product_name                      |
            | Sauce Labs Backpack               |
            | Sauce Labs Bike Light             |
            | Sauce Labs Bolt T-Shirt           |
            | Sauce Labs Fleece Jacket          |
            | Sauce Labs Onesie                 |
            | Test.allTheThings() T-Shirt (Red) |