#read json file, output active users in json

import json

with open('users.json', 'r') as file:
    users = json.load(file) 

active_users = []
for user in users:
    if user['active']:
        active_users.append(user)

with open('output.json','w') as file:
    json.dump(active_users, file, indent=4)