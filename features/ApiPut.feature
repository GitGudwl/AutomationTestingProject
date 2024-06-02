Feature: Api testing for put endpoint

  Scenario: Missing APP_ID header
    Given the PUT header "app-id" is ""
    And the PUT request body is read from "missing_app_id_body.json"
    When I make a PUT request to "60d0fe4f5311236168a109ff"
    Then the PUT status code should be 403
    And the PUT response should contain "error" with value "APP_ID_MISSING"

  Scenario: Invalid APP_ID header
    Given the PUT header "app-id" is "6635747e0de1363eba89ff1g"
    And the PUT request body is read from "invalid_app_id_body.json"
    When I make a PUT request to "60d0fe4f5311236168a109ff"
    Then the PUT status code should be 403
    And the PUT response should contain "error" with value "APP_ID_NOT_EXIST"

  Scenario: Valid request with correct APP_ID
    Given the PUT header "app-id" is "6635747e0de1363eba89ff1f"
    And the PUT request body is read from "valid_request_body.json"
    When I make a PUT request to "60d0fe4f5311236168a109ff"
    Then the PUT status code should be 200
    And the PUT response should contain "id" with value "60d0fe4f5311236168a109ff"
    And the PUT response should contain "firstName" with value "Josefina"
    And the PUT response should contain "lastName" with value "Calvi"

  Scenario: Valid request with full update
    Given the PUT header "app-id" is "6635747e0de1363eba89ff1f"
    And the PUT request body is read from "full_update_body.json"
    When I make a PUT request to "60d0fe4f5311236168a109ff"
    Then the PUT status code should be 200
    And the PUT response should contain "id" with value "60d0fe4f5311236168a109ff"
    And the PUT response should contain "firstName" with value "Josafina"
    And the PUT response should contain "lastName" with value "Calvi"

  Scenario: Invalid request with incorrect gender type
    Given the PUT header "app-id" is "6635747e0de1363eba89ff1f"
    And the PUT request body is read from "invalid_gender_body.json"
    When I make a PUT request to "60d0fe4f5311236168a109ff"
    Then the PUT status code should be 400
    And the PUT response should contain "error" with value "BODY_NOT_VALID"
