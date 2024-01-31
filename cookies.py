# sending cookies(shud be send as dict) in api call

import requests
from utilities.configurations import *
from payload import *

url = getConfig()['API']['cookies_url']
cookie_data = {'visit-year':'2023'}
response = requests.get(url,cookies=cookie_data)
print(response.content)

# keep the cookie in the session,

session_cookie = requests.session()
session_cookie.cookies.update(get_session_cookie()) # added cookie in session

res = session_cookie.get(url,cookies=cookie_data)

print(res.text) # we get both cookie passed explicitly and also  cookie in session
