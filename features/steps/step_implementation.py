from behave import *
from utilities.configurations import *  # for url
from utilities.endpoints import *  # for resources
import requests
from payload import *  # to sent request params from external file(payload.py)


# adding the book
@given('All book details')
def step_impl(context):
    context.url_addBook = getConfig()['API']['base_url'] + ApiResources.addBook
    context.headers = {'Content-Type': 'application/json'}
    context.addBook_params = addBookParams("abc221", 666)


@when('execute addBook Post API method')
def step_impl(context):
    context.response = requests.post(context.url_addBook, json=context.addBook_params,
                                             headers=context.headers, )


@then('Book added successfully')
def step_impl(context):
    print(f"json response is:{context.response.json()}")
    addBook_response_data = context.response.json()
    context.book_id = addBook_response_data.get("ID")
    print(context.book_id)
    assert not addBook_response_data.get("Msg") == "Book Already Exists"

# parameterization of data sets
@given('book details with {isbn} and {aisle} as data sets')
def step_impl(context, isbn, aisle):
    context.url_addBook = getConfig()['API']['base_url'] + ApiResources.addBook
    context.headers = {'Content-Type': 'application/json'}
    context.addBook_params = addBookParams(isbn, aisle)

#using session
@given('git credentials')
def step_impl(context):
    context.git_session = requests.session()
    context.git_session .auth = auth = git_login()  # auth is given here in session


@when('Hit git url using session')
def step_impl(context):
    url = getConfig()['API']['git_url']
    # verify=False is to avoid SSL errors
    context.response = context.git_session .get(url, verify=False, )


# status code is stored in a variable  as d(decimal) to reuse step_impl
@then('Successful access and response code {status_code:d}')
def step_impl(context, status_code):
    print(context.response.status_code)
    assert context.response.status_code == status_code

