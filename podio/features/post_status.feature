Feature: Post

  Background:
    Given a browser
    And I log in
    And I am on the home page
    And I am a "US" user

  @positive
  Scenario: Customer makes a status post
    When I click the status
    And I enter a status post
    And I click the share button
    And I click the default_workspace
    Then The status post should be displayed

  @negative
  Scenario: Customer does not enter status and tries to post a status
    When I click the status
    And I click the share button
    Then I should see the status_error_icon
