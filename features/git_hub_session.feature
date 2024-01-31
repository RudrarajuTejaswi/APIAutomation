# Created by aniln at 12-01-2024
Feature: Checking session with git hub url
  # Enter feature description here

  Scenario: Access git using session
   Given git credentials
    When Hit git url using session
    Then Successful access and response code 401