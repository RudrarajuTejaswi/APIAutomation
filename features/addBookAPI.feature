# Created by aniln at 10-01-2024
Feature: Add book using addBook API and delete the book
  # Enter feature description here
  # @libraryAPI - to customize hook(after_scenario)
  @smoke @libraryAPI
  Scenario: Add a new book
    Given All book details
    When execute addBook Post API method
    Then Book added successfully
    And Successful access and response code 200

  # parameterized data sets for API test use scenario outline
  # isbn aisle should match with name in examples
  @regression @libraryAPI
  Scenario Outline: Add a new book
    Given book details with <isbn> and <aisle> as data sets
    When execute addBook Post API method
    Then Book added successfully
    Examples:
      | isbn   | aisle |
      | atg101 | 123 |
      | slkh101 | 777 |