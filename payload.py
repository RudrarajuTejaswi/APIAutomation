from utilities.configurations import *
#request json for add book API - isbn is made dynamic, taking input from user
def addBookParams(isbn,aisle):
    add_data = {
        "name": "Learn API testing",
        "isbn": isbn,
        "aisle": aisle,
        "author": "Gahan"
    }
    # getting data from db
    # add_data = {} #created a empty dict
    # db_data = get_data_for_addBook(query)
    # add_data["name"] = db_data[0]
    # add_data["isbn"] = db_data[1]
    # add_data["aisle"] = db_data[2]
    # add_data["author"] = db_data[3]
    return add_data

# request param for getBookByAuthor
def getBookByAuthorParams():
    get_book_author = {'AuthorName':'Rahul Shetty'}
    return get_book_author

#auth params for git login, used token for password from git
def git_login():
    credentials = ('RudrarajuTejaswi','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')
    return credentials

# to keep cookie in session
def get_session_cookie():
    cookie_data = {'visit-month':'october'}
    return cookie_data

