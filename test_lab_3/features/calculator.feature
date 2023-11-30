Feature: Calculator


    Scenario: Add two numbers
        Given I have a calculator
        When I add 5 and 7
        Then the result should be 12


    Scenario: Diff two numbers
        Given I have a calculator
        When I diff 5 and 7
        Then the result should be -2
