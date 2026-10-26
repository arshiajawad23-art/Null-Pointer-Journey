name = input("Enter your name: ")
with open("user_text.txt" ,"a") as file:
    file.write(f"{name}\n")
description = input("Enter your description: ")

with open("user_text.txt" ,"a") as file:
    file.write(f"{description}\n")

with open("user_text.txt" ,"r") as file:
    print(file.read())

print("Thank you!")



with open("my_dream.txt" ,"r", encoding = "utf-8") as f:
    file = f.read()
    print(f"--- look to your dream ---\n{file}")

print()
# improve
with open("my_dream.txt" ,"r", encoding = "utf-8") as f:
    dream = f.read()
    for drm in dream:
        print(f"_{drm}", end="")

# اون بالا نیز نتونست بهتر باشد الان میخوام دوباره بهترش کنم با نمایش زیبا
print("\n\n")
# improve
with open("my_dream.txt" ,"r", encoding = "utf-8") as f:
    dream = f.readlines()
    for drm in dream:
        print(f"**** {drm}" ,end="")

print() # این پرنت خالی را بخاطراینکه در خروجی با این قطعه دوم من قاطی میشه و فاصله را مراعت نمیکند

name = input("Enter your name: ")
message = input("Enter your message: ")

with open("message.txt" ,"a", encoding="utf-8") as file:
    message = file.write(f"{name} send a message:\n\t\t____ {message} ____\n")
    print(f"{name} sent a message")

# الان میخوام فایل سوم بسازم

with open("story3.txt" ,"r", encoding="utf-8") as file:
    story = file.read()
    print(story)

print("="*30)

with open("story3.txt" ,"r", encoding = "utf-8") as sty:
    my_look = sty.read()
    words = my_look.split()
    # lines = sty.readlines()
    print(f"all character in this file is : {len(my_look)}")
    print(f"quantity of words : {len(words)}")
    # print(f" and have  line {len(lines)}")
# نمی فهمم چرا اینجا الن ها را برم 0 نمایش میدهد یک راهنمایی


# اینگونه توانستم ببینمش ولی آیا همینگونه درشت است یا خیر
with open("story3.txt" ,"r", encoding = "utf-8") as file:
    story = file.readlines()
    print(f"we have {len(story)} lines is story file")
# میروم اون بالا و اون دوخط را کومن میکنم تا در خروجی باعس نشود کسی دیگر اشتباه ببیند



# الان جستجوگر:
search = input("enter any word to look for: ")

with open("story3.txt" ,"r", encoding = "utf-8") as file:
    story = file.read()
    if search in story:
        print(f"we have {search} in story file")
    else:
        print(f"sorry!..., we do not have {search} in story file..!!!")



with open("story3.txt" ,"r", encoding = "utf-8") as file:
    story = file.read()
    story.lower()
    with open("new_story", "a", encoding="utf-8") as f:
        f.write(story)









