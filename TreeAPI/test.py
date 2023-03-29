


import requests
import json






attributes = json.dumps({'f': 'fff',})

url = 'http://92.255.79.72/api/add_root/'
url2 = 'http://92.255.79.72/api/get_descendants/'

data = {'project_id': '23', 'item_type': 'sdfsdf', 'item': 'ewrwer',}


# result = requests.post(url, data)
result = requests.post(url, data)


# full_page = requests.get(url, data=data)
print(result.content)

