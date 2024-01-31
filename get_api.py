import requests
from utilities.configurations import *
from utilities.endpoints import *
from payload import *

#get has 3 params url, params(should be passed as dict), additional params(like headers)

url_getBook = getConfig()['API']['base_url']+ApiResources.getBookByAuthor
response = requests.get(url_getBook,params=getBookByAuthorParams(),)

response_data = response.json() #can be of type dict or list
print(response_data)
#assert 'John foe' == response_data[0].get('author')
assert response.status_code == 200
assert response.headers.get('Content-Type') == 'application/json;charset=UTF-8'

#retrieve data with isbn as JH877
expected_book = {'book_name': 'Postman Testing', 'isbn': 'JH877', 'aisle': '1234'}
for actual_book in response_data:
    if actual_book.get('isbn') == 'JH877':
        print(actual_book)
        break
assert actual_book == expected_book

