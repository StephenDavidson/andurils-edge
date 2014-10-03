Feature: Post

  Background:
    Given a browser
    And I log in
    And I am a "US" user

  Scenario: Customer makes a status post
    When I enter a status post
    And I submit the status post
    Then I should see the status post
