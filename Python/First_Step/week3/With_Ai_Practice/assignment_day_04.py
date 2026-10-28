def creat_email(first_name, domain = "google.com"):
    return f"{first_name}@{domain}"

name = input("Enter your first name: ")
print(creat_email(name))
print(creat_email("Arshia"))
print(creat_email("Jawad","yahoo.com"))