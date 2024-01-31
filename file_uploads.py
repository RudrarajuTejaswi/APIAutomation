import requests
from utilities.configurations import *
from utilities.endpoints import *

url = getConfig()['API']['files_upload_url'] + ApiResources.file_uploads
files  = {'file': open('image.png', 'rb')}

response = requests.post(url,files=files)
print(response.status_code)
print(response.text)
