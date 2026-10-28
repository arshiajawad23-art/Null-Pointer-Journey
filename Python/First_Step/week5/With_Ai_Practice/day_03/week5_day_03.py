import json

my_dict = {"name": "Jawad", "age": 25}

with open("data.json", "w") as file:
    json.dump(my_dict, file)


with open("data.json", "r") as file:
    loaded_dict = json.load(file)
    print(loaded_dict)
with open("data.json", "r") as file:
    didan = json.load(file)
    print(didan)

# از این روش نیز امکان دارد
print(loaded_dict)
print(didan)


#
# try:
#     with open("ghost.txt", "r" , encoding="utf-8") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("not found but i try to make a new one")
#     with open("ghost.txt", "w", encoding="utf-8") as ghost_file:
#         _write = ghost_file.write("""ghost_dream = {
#     "名": "鬼",
#     "想要": "梦"
# }
# """)           # چرا نمیشه فایل ذخیره کرد از روش جسون هم استفاده کردم نشد
#         # ghost_dream = {"name":"Jawad, "dream": "Ghost"}
# #         with open("ghost.json", "w") as ghost_file
# #             json.dump(ghost_dream,ghost_file)
# # 我现在除了创造以外还要一项加在我创造的

try:
    with open("ghost.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("file not found")

try:
    print("we try to make new ghost file")
    with open("ghost.txt", "w") as f:
        f.write("hello welcome")
except FileNotFoundError:
    print("file not found")

try:
    age = int(input("Age: "))
    print(f"your {age} years old")
except ValueError:
    print("iinput only number ")
finally:
    print("this message will print finally")


try:
    result = 10/0
except ZeroDivisionError:
    print("division by zero is impossible or not defined")
    print('不可能。 分零不行')

