import requests
from utilities.configurations import *
from payload import *
from utilities.endpoints import *

#session is used, to keep the auth variables in session so auth need not be passed everytime a url is hit
git_session =requests.session()
git_session.auth = auth = git_login() #auth is given here in session

url = getConfig()['API']['git_url']
#verify=False is to avoid SSL errors
#res = requests.get(url, verify=False, auth=git_login())
res = git_session.get(url, verify=False,)
print(res.status_code)

url2 = url+ApiResources.git_rep_auth_user
res = git_session.get(url2,)
print(res.status_code)

#instead of requests.get, git_session.get is used to maintain the session
#session is maintained so that auth need not be given everytime

#for files upload
#https://requests.readthedocs.io/en/latest/user/quickstart/?highlight=Multipart%20File%20Uploads#post-a-multipart-encoded-file