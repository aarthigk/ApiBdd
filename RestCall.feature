Feature: This is simple python rest api testing feature file

Background:
	Given user sets a REST API url

Scenario: POST post example
  Given user Set POST posts api endpoint
 When user Set HEADER param request content type as "application/json."
    And Set request Body
 And Send a POST HTTP request
 Then user receives valid HTTP response code 201
    And Response BODY "POST" is non-empty.
