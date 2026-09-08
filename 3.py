#make an api call

import requests

url = "https://jsonplaceholder.typicode.com/users"

try:
    data = requests.get(url)
    print('status: ', data.status_code)
    if data.status_code == 200:
        response = data.json()

    for res in response:
        print(res)

except requests.exceptions as e:
    print("Request failed:", e)