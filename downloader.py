import requests

url = 'https://'

r = requests.get(url, allow_redirects=True)
open('filename.png','wb').write(r.content)
