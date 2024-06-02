Feature: API TEST - GET

    Scenario: Missing APP_ID header
        Given the GET header "app-id" is ""
        When I make a GET request to "60d0fe4f5311236168a10a06"
        Then the GET status code should be 403
        And the GET response should contain "error" with value "APP_ID_MISSING"

    Scenario: Invalid APP_ID header
        Given the GET header "app-id" is "6635747e0de1363eba89ff1g"
        When I make a GET request to "60d0fe4f5311236168a109fa"
        Then the GET status code should be 403
        And the GET response should contain "error" with value "APP_ID_NOT_EXIST"

    Scenario: Valid request with correct APP_ID
        Given the GET header "app-id" is "665acdd5b842089f2e37b051"
        When I make a GET request to "60d0fe4f5311236168a109fa"
        Then the GET status code should be 200
        And the GET response should contain "id" with value "60d0fe4f5311236168a109fa"
        And the GET response should contain "firstName" with value "Ann"
        And the GET response should contain "lastName" with value "Mason"

    Scenario: User ID not found
        Given the GET header "app-id" is "66367c7b3ec826592a67a062"
        When I make a GET request to "60d0fe4f5311236168a109f1"
        Then the GET status code should be 404
        And the GET response should contain "error" with value "RESOURCE_NOT_FOUND"

    Scenario: Invalid User ID
        Given the GET header "app-id" is "66367c7b3ec826592a67a062"
        When I make a GET request to "0"
        Then the GET status code should be 400
        And the GET response should contain "error" with value "PARAMS_NOT_VALID"
