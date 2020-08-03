from behave import given, when, then, step
import requests

api_endpoints = {}
request_headers = {}
response_codes ={}
response_texts={}
request_bodies = {}
api_url=None

@given(u'a user has set REST API url')
def step_impl(context):
    global api_url
    api_url = 'http://jsonplaceholder.typicode.com'


@given(u'a user specifies POST api endpoint')
def step_impl(context):
    api_endpoints['POST_URL'] = api_url + '/posts'
    print('url :' + api_endpoints['POST_URL'])


@when(u'a user Sets HEADER param request content type as "{header_conent_type}"')
def step_impl(context,header_conent_type):
    request_headers['Content-Type'] = header_conent_type


@when(u'Sets request Body')
def step_impl(context):
    request_bodies['POST'] = {"title": "foo", "body": "bar", "userId": "1"}


@when(u'Sends a POST HTTP request')
def step_impl(context):
    response = requests.post(url=api_endpoints['POST_URL'], json=request_bodies['POST'], headers=request_headers)
    response_texts['POST'] = response.text
    print("post response :" + response.text)
    statuscode = response.status_code
    response_codes['POST'] = statuscode


@then(u'the user will recieve valid HTTP response code 201')
def step_impl(context):
    print('Post rep code ;' + str(response_codes['POST']))
    assert response_codes['POST'] is 201


@then(u'Response BODY "{request_name}" is non-empty.')
def step_impl(context,request_name):
    print('request_name: ' + request_name)
    print(response_texts)
    assert response_texts[request_name] is not None


@given(u'user specifies GET api endpoint with param as "{id}"')
def step_impl(context,id):
    api_endpoints['GET_URL'] = api_url + '/posts/' + id
    print('url :' + api_endpoints['GET_URL'])


@when(u'Sends GET HTTP request')
def step_impl(context):
    response = requests.get(url=api_endpoints['GET_URL'],headers=request_headers)
    response_texts['GET'] = response.text
    statuscode = response.status_code
    response_codes['GET'] = statuscode

@then(u'the user will receive valid HTTP response code 200 for "{request_name}."')
def step_impl(context,request_name):
    print('Get rep code for '+request_name+':'+ str(response_codes[request_name]))
    assert response_codes[request_name] is 200

@then(u'Response BODY "{request_name}" is non-empty')
def step_impl(context,request_name):
    print('request_name: ' + request_name)
    print(response_texts)
    assert response_texts[request_name] is not None

@given(u'user specifies PUT posts api endpoint with param as "{1}"')
def step_impl(context,id):
    api_endpoints['PUT_URL'] = api_url + '/posts/' + id
    print('url :' + api_endpoints['PUT_URL'])


@when(u'a user Sets Update request Body')
def step_impl(context):
    request_bodies['PUT']={"title": "foo","body": "bar","userId": "1","id": "1"}


@when(u'Send PUT HTTP request')
def step_impl(context):
    se = requests.post(url=api_endpoints['POST_URL'],headers=request_headers)  # https://jsonplaceholder.typicode.com/posts
    response = requests.put(url=api_endpoints['PUT_URL'], json=request_bodies['PUT'], headers=request_headers)
    response_texts['PUT'] = response.text
    print("update response :" + response.text)
    statuscode = response.status_code
    response_codes['PUT'] = statuscode


@given(u'user specifies DELETE posts api endpoint for param as "{1}"')
def step_impl(context,id):
    api_endpoints['DELETE_URL'] = api_url + '/posts/' + id
    print('url :' + api_endpoints['DELETE_URL'])


@when(u'a user Send DELETE HTTP request')
def step_impl(context):
    response = requests.delete(url=api_endpoints['DELETE_URL'])
    response_texts['DELETE'] = response.text
    print("DELETE response :" + response.text)
    statuscode = response.status_code
    response_codes['DELETE'] = statuscode
