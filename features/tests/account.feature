# Created by laurautarbayeva at 7/8/22
Feature: Clicking on Account icon opens Login form
  Scenario: User can see login page by clicking on account icon
    Given Open GetTop
    When Click on Account icon
    Then Verify login form opens

  Scenario: User can see login page in mobile version
    Given Open GetTop
    When Click over hamburger menu
    And Click login option
    Then Verify login form opens
