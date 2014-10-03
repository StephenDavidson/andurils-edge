Feature: Login

  Background:
    Given a browser

  Scenario: Login to the site as a user
    Given I visit the login page
    And I am a "US" user
    And I have valid credentials
    When I fill in the login form
    And I submit the login form
    Then I should be on the home page