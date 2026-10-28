show = "===== phone contact book =====".upper()
print(show)
contacts = {

}

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
        print(f"{phone} has been added to {name}")

    elif task in ("l", "2"):
        for name, contact in contacts.items():
            print(f"{name}: {contact}")

    elif task in ("e", "3"):
        break
    else:
        print("Invalid input")

print(contacts)

