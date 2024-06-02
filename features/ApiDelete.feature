Feature: Api testing for delete endpoint
Feature: API TEST - DELETE

    Scenario: Missing APP_ID header
        Given the DELETE header "app-id" is ""
        And the DELETE request user ID is "60d0fe4f5311236168a109fb"
        When I make a DELETE request to it
        Then the DELETE status code should be 403
        And the DELETE response should contain "error" with value "APP_ID_MISSING"

    Scenario: Invalid APP_ID header
        Given the DELETE header "app-id" is "663765958f1bd4014ac31abc"
        And the DELETE request user ID is "60d0fe4f5311236168a109fb"
        When I make a DELETE request to it
        Then the DELETE status code should be 403
        And the DELETE response should contain "error" with value "APP_ID_NOT_EXIST"

    Scenario: Valid request with correct APP_ID
        Given the DELETE header "app-id" is "665acdd5b842089f2e37b051"
        And the DELETE request user ID is "60d0fe4f5311236168a10a00"
        When I make a DELETE request to it
        Then the DELETE status code should be 200
        And the DELETE response should contain "id" with value "60d0fe4f5311236168a10a00"

    Scenario: User ID does not exist
        Given the DELETE header "app-id" is "665acdd5b842089f2e37b051"
        And the DELETE request user ID is "60d0fe4f5311236168a109f1"
        When I make a DELETE request to it
        Then the DELETE status code should be 404
        And the DELETE response should contain "error" with value "RESOURCE_NOT_FOUND"

    Scenario: Invalid User ID format
        Given the DELETE header "app-id" is "665acdd5b842089f2e37b051"
        And the DELETE request user ID is "0"
        When I make a DELETE request to it
        Then the DELETE status code should be 400
        And the DELETE response should contain "error" with value "PARAMS_NOT_VALID"
