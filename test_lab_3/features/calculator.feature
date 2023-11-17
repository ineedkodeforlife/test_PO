Feature: Calculator functionality

  Scenario: Addition
    Given the calculator is open
    When I enter "2" into the first argument
    And I enter "3" into the second argument
    And I press the "+" button
    Then the result should be "5"

  Scenario: Subtraction
    Given the calculator is open
    When I enter "5" into the first argument
    And I enter "2" into the second argument
    And I press the "-" button
    Then the result should be "3"

  Scenario: Multiplication
    Given the calculator is open
    When I enter "2" into the first argument
    And I enter "4" into the second argument
    And I press the "*" button
    Then the result should be "8"

  Scenario: Division
    Given the calculator is open
    When I enter "8" into the first argument
    And I enter "2" into the second argument
    And I press the "/" button
    Then the result should be "4"

  Scenario: Division by zero
    Given the calculator is open
    When I enter "8" into the first argument
    And I enter "0" into the second argument
    And I press the "/" button
    Then I should see an error message "Cannot divide by zero"
