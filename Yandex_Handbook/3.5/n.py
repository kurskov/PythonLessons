import json

users_file_name = input()
updates_file_name = input()

with open(users_file_name, encoding="UTF-8") as file_input:
    users = json.load(file_input)

with open(updates_file_name, encoding="UTF-8") as file_input:
    updates = json.load(file_input)

updated_users = dict()
for user in users:
    pass
