import json


user = {
    "name": "Arshia", "age": 26, "goal":"Billionaire"
}

with open("user.json", "w") as f:
    json.dump(user, f, indent=4)

with open("user.json", "r") as f:
    loaded_user = json.load(f)
    print(loaded_user["name"])
    print(loaded_user["age"])

users = [
    {"id": 1, "name": "Ali"},
    {"id": 2, "name": "Sara"}
]

with open("users.json", "w") as file:
    json.dump(user, file, indent=4)


my_dict = {"name": "Jawad", "age": 25}

with open("data.json", "w") as file:
    json.dump(my_dict, file)

with open("data.json", "r") as file:
    loaded_dict = json.load(file)
    print(loaded_dict)
    print(type(loaded_dict))


print("="*40)
print("\n\n")
# این دو پرنت فقط برای اینکه در خروجی به راحتی بتوانم ببینم خروجی هارا

user  = {
    "name": "Jawad",
    "age": 25,
    "goal" : "Billionaire"
}

with open("user.json", "w") as f:
    json.dump(user,f,indent=4)
# indent = 4 is for good redable codes
with open("user.json", "r") as file:
    loaded_user = json.load(file)
    print(loaded_user)
    print(type(loaded_user))
    print(loaded_user["name"])
    print(loaded_user["age"])
    print(loaded_user["goal"])




users = [
    {"id": 1,"name":"Ali"},
    {"id": 2,"name":"Sara"}
]

with open("_users.json", "w") as f:
    json.dump(users,f,indent=4)


with open("_users.json", "r") as file:
    cur_users = json.load(file)
    print(cur_users)



print('='*40)
print('\n\n')

users.append({"id":3, "name":"Jawad"})
cur_users = users
with open("__users.json", "w") as file:
    json.dump(cur_users,file,indent=4)

