Feature: Post

  Background:
    Given a browser
    And I log in
    And I am a "US" user

  @positive
  Scenario: Customer makes a status post
    When I enter a status post
    And I click share post
    And I select the default workspace
    Then I should see the status post

  @negative
  Scenario: Customer does not enter status and tries to post a status
    When I click share post
    Then I should see a status post error icon
