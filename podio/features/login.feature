Feature: Login

  Background:
    Given a browser
    And I visit the login page
    And I am a "US" user

  @positive
  Scenario: Login to the site as a user
    Given I have valid credentials
    When I fill in the login form
    And I submit the login form
    Then I should be on the home page

  @negative
  Scenario: Login to site with invalid credentials
    Given I fill in the login form
    And I submit the login form
    Then I should receive a login warning message