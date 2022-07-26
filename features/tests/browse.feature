# Created by laurautarbayeva at 7/14/22
Feature: User sees correct categories under Browse
User sees click on categories under Browse and correct page opens


  Scenario Outline: Clicking on different Categories under Browse opens correct page
    Given Open GetTop browse page
    When Click on <search_word>
    Then Verify search results are shown for <expected_result>
    Examples:
    | search_word   | expected_result   |
    | Accessories   | "Accessories"     |
    | iPad          | "iPad"            |
    | iPhone        | "iPhone"          |
    | MacBook       | "MacBook"         |