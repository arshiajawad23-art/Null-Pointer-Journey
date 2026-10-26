with open ("notes.txt", "w") as file:
    file.write("This is an empty note")

with open("notes.txt", "a") as file:
    file.write("This is another note")

with open("user_text.txt", "r") as file:
    print(file.read())

with open("log.txt", "w") as file:
    file.write("start program\n")

with open("log.txt", "a") as file:
    file.write("user entered\n")
    file.write("end program\n")

my_list = ["Jawad", "Fawad","Sajad"]
with open("names.txt", "w") as file:
    for skill in my_list:
        file.write(f"- {skill}\n")
#
#

# write and add and management a little bit good quality


with open("log.txt", "w") as f:
    f.write("Program Started\n")

with open("log.txt", "a") as f:
    f.write("Enter User\n")
    f.write('Program Ends.\n')

my_list =["html", "Css", "python"]
with open("skills.txt", "w") as f:
    for skill in my_list:
        f.write(f"- {skill}\n")
