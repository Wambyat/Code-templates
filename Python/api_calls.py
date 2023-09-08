import requests

# GET
url = 'https://api.randowebsite.com'
response = requests.get(url)

# POST
data = {'key': 'value'}
response = requests.post(url, data=data)

# with headers
headers = {'Content-Type': 'application/json'}
response = requests.post(url, data=data, headers=headers)

# with authentication
auth = ('username', 'password')
response = requests.post(url, data=data, auth=auth)