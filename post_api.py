import requests
from payload import * #to sent request params from external file(payload.py)
from utilities.configurations import * #for url
from utilities.endpoints import * #for resources

#adding a book
# replaced http://216.10.245.166/ with getConfig()['API']['base_url']
#getConfig() - from configurations.py,this file has link to .ini file

url_addBook = getConfig()['API']['base_url']+ApiResources.addBook
headers = {'Content-Type':'application/json'}

# addBook_response = requests.post(url_addBook, json=addBookParams("atg"), headers=headers,)
#get json payload from DB
addBook_response = requests.post(url_addBook, json=addBookParams("select * from Books"), headers=headers,)

addBook_response_data = addBook_response.json()
book_id = addBook_response_data.get("ID")

#deleting the book added above
url_deleteBook = getConfig()['API']['base_url']+ApiResources.deleteBook

del_book_res = requests.post(url_deleteBook,json={"ID" : book_id},) #headers are optional

del_book_res_data = del_book_res.json()
print(del_book_res_data)
assert del_book_res_data.get('msg') == 'book is successfully deleted'
