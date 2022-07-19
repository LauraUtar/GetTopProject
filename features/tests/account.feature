# Created by laurautarbayeva at 7/8/22
Feature: Clicking on Account icon opens Login form
  Scenario: User can see login page by clicking on account icon
    Given Open GetTop
    When Click on Account icon
    Then Verify login form opens

#
#Code is getting executed. However, the verification seems to be incorrect.
#  You are verifying the visibility of the ACCOUNT icon.
#  This is incorrect. You can verify any element from the Login form including the LOGIN button.
#  Please update and resubmit. Moving the Jira back to ‘In Progress’