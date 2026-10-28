
def hsk_status(name,score):
    if score >= 180:
        print(f"{name} you Done it, {name} pass hsk5")
    elif score < 180 and score >= 120:
        print(f"{name} yoy Just pass Hsk 4")
    else:
        print(f"sory, {name} didn't pass \"the Hsk4 or 5\" more try for next year..!")

name = input("What is your name? ")
score = int(input("What is your score? "))
hsk_status(name,score)

第二挑战
这个函数用为了三个人

def hsk_calculate(name, score):
# ازینگونه چندین بار نوشتم و چندین نوع تست کردم اینها درست به حل نمی رساند و از همین در حلقه for نیز استفاده کردم نشد
    i = 0
    while i <= 3:
        name = input("Enter your name: ")
        score = input("Enter your score: ")
        i += 1
    if score >= 180:
        print(f"{name} pass the hsk5 exam")
    elif score >= 120:
        print(f"{name} pass the hsk4 exam")
    else:
        print(f"{name} didn't pass the hsk4 or hsk5  exam")


hsk_calculate("name",'score')

اینبار میخواهم دوباریه فکر کنم چند لحضه توقف کنم و برای روش جدید فکر کنم
def hsk_calculate(name,score):
    for i in range(3):
        if score >= 180:
            print(f"{name} pass the hsk5")
        elif score >= 120:
            print(f"{name} pass the hsk4")
        else:
            print(f"{name} didn't pass the hsk")

name = input("What is your name? ")
score = int(input("What is your score? "))
hsk_calculate(name,score)
# 这个办法也不行， 这个函数print我的名字三次

# 再找新办法新做法

def hsk_calculate(name, score):
    if score >= 200:
        print(f"{name} pass the hsk5")
    elif score >= 150:
        print(f"{name} pass the hsk4")
    else:
        print(f"{name} didn't pass the hsk4 or 5")


for i in range(3):
    name = input("What is your name? ")
    score = int(input("What is your score? "))
    hsk_calculate(name, score)

# 👌👌👌👏👏 🤣😁 این را خودم برای خود دادم
# 
# بعد از 10 بار فکر کردم نوشتن و چذف کردم و دوباره نوشتن توانستم به حل مسله برسم


