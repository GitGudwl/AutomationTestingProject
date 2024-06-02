Feature: Api testing for create endpoint

    Scenario: create new user with valid app id header
        Given I have a new user data located at "features/data/user_data1.json" with generated email
        When I send a POST request to "/user/create" with app id: "6636324525a5b823ed8a1d31"
        Then the response status code should be 200
        And the response should contain the user data

    Scenario: Invalid APP_ID header
        Given I have a new user data located at "features/data/user_data1.json" with generated email
        When I send a POST request to "/user/create" with app id: "6636324525a5b823ed8a1121434"
        Then the response status code should be 403
        And the response should contain error "APP_ID_NOT_EXIST" with value "APP_ID_NOT_EXIST"

    Scenario: Missing firstName in request body
        Given I have a new user data located at "features/data/user_data2.json" with generated email
        When I send a POST request to "/user/create" with app id: "6636324525a5b823ed8a1d31"
        Then the response status code should be 400
        And the response should contain error "BODY_NOT_VALID" with value "'firstName': 'Path `firstName` is required.'"

    Scenario: Missing lastName in request body
        Given I have a new user data located at "features/data/user_data3.json" with generated email
        When I send a POST request to "/user/create" with app id: "6636324525a5b823ed8a1d31"
        Then the response status code should be 400
        And the response should contain error "BODY_NOT_VALID" with value "'lastName': 'Path `lastName` is required.'"

    Scenario: Create a post with existing email
        Given I have a new user data located at "features/data/user_data4.json" without generated email
        When I send a POST request to "/user/create" with app id: "6636324525a5b823ed8a1d31"
        Then the response status code should be 400
        And the response should contain error "BODY_NOT_VALID" with value "'email': 'Email already used'"