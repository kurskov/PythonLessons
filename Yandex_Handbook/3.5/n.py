# import json

# users_file_name = input()
# updates_file_name = input()

# with open(users_file_name, encoding="UTF-8") as file_input:
#     users = json.load(file_input)

# with open(updates_file_name, encoding="UTF-8") as file_input:
#     updates = json.load(file_input)


users = [
    {
        "name": "Ann",
        "address": "Flower st."
    },
    {
        "name": "Bob",
        "address": "Summer st.",
        "phone": "+7 (123) 456-78-90"
    }
]

updates = [
    {
        "name": "Ann",
        "address": "Awesome st.",
        "phone": "+7 (098) 765-43-21"
    },
    {
        "name": "Bob",
        "address": "Winter st."
    }
]

result = dict()
for user in users:
    name = user["name"]
    del user["name"]
    result[name] = user

print(result)
