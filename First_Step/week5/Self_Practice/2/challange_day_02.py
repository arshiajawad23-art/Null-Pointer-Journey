import datetime

# #
felling = input("Please enter your felling [ good / bad ]: ")
if felling == "good":
    date = datetime.date.today()
    print(f"your felling at {date} is {felling}")
elif felling == "bad":
    date = datetime.date.today()
    print(f"your felling at {date} is {felling}")
else:
    print("invalid")
#
# # الان یک کمی بهبود می دهیم
#
while True:
    print("for exit always just write ... -- [exit or e] -- !!")
    felling = input("Please enter your felling [ good / bad ]: ").strip().lower()
    if felling in ['exit', 'e']:
        break
    elif felling == "good":
        date = datetime.date.today()
        with open("mode.txt", "a") as file:
            file.write(f"your mode is {felling} at this date {str(date)}\n")
        print(f"your felling at {date} is {felling}")
    elif felling == "bad":
        date = datetime.date.today()
        with open("mode.txt", "a") as file:
            file.write(f"your mode is {felling} at this date {str(date)}\n")
        print(f"your felling at {date} is {felling}")
    else:
        print("invalid")



