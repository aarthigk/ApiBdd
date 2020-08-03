Feature: To check the basic post, get, put, and delete operations are returning valid response

Background:
	Given a user has set REST API url

Scenario: To assert POST behaviour
  Given a user specifies POST api endpoint
 When a user Sets HEADER param request content type as "application/json."
    And Sets request Body
 And Sends a POST HTTP request
 Then the user will recieve valid HTTP response code 201
    And Response BODY "POST" is non-empty.

Scenario: To assert GET behaviour
  Given user specifies GET api endpoint with param as "1"
  When a user Sets HEADER param request content type as "application/json"
	And Sends GET HTTP request
  Then the user will receive valid HTTP response code 200 for "GET."
	And Response BODY "GET" is non-empty
