import json

show = "===== phone contact book =====".upper()
print(show)
contacts = {

}

try:
    with open('contacts.json', 'r',encoding="utf-8") as json_file:
        contacts = json.load(json_file)
except FileNotFoundError:
    print("No contacts file found , we creat an empty dict")
    with open('contacts.json', 'w', encoding="utf-8") as json_file:
        json.dump(contacts, json_file)
except json.JSONDecodeError:
    print("File is empty or corrupted, Resetting ...")
    with open('contacts.json', 'w', encoding="utf-8") as json_file:
        json.dump(contacts, json_file)

while True:
    print("""\n\t1.add write -- [a] or -- [1]
    2.look audience write -- [l] or -- [2]
    3.exit write -- [e] or -- [3]\n""")
    task = input("""what task do you want:\n""").strip().lower()

    if task in ('a', '1'):
        name = input("Enter name: ")
        if not name:
            print("Name cannot be empty")
            continue
        phone = input("Enter phone number: ")
        contacts[name] = phone
        with open('contacts.json', 'w') as json_file:
            json.dump(contacts, json_file)
        print(f"{phone} has been added to {name}")

    elif task in ("l", "2"):
        for name, contact in contacts.items():
            print(f"{name}: {contact}")

    elif task in ("e", "3"):
        break
    else:
        print("Invalid input")

print(contacts)