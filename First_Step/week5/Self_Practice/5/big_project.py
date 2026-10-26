import json
print("==== shows expenses ====")

show_menu = """
        1. add expense ...          [a] or [1]
        2. show expense ...         [b] or [2]
        3. look All expenses ...    [c] or [3]
        4. exit ...          [d] or [e] or [4]
"""


try:
    with open("expense.json", 'r') as file:
        exp = file.read()
except FileNotFoundError:
    print("File not found, we try to creat an empty dict")
    with open("expense.json", 'w') as file:
        file.write("{}")


exp_dict = {}

while True:
    choice = input(f"{show_menu}\n select your choice: ").lower().strip()


    if choice in ["a","1"]:
        name = input("Enter your name: ")
        expense = input("Enter your expense: ")
        show = exp_dict[name] = expense
        with open("expense.json", 'w') as file:
            file.write(json.dumps(exp_dict))

    elif choice in ["b","2"]:
        try:
            print(f"{name} : {expense}")
        except NameError:
            print("contact phone haven't numbers please first add with choice 1")


    elif choice in ["c","3"]:
        with open("expense.json", 'r') as file:
            exp = json.load(file)
            print(exp)
    elif choice in ["d","e","4"]:
        break
    else:
        print(f"{choice} is not a valid option")

