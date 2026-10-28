# in week 3 set is more challangable for me because i did not learn this type in week3

tools = ["nmap","burp","sqlmap"]
tools.append("wireshak")
print(tools)

tools.remove("burp")
print(tools)
tools.pop()
print(tools.pop())
print(tools)
# 2:
# the problems : that i couldn't see good results 
nums = [21,1, 2, 3, 4,11, 5, 6,15, 7, 8, 9, 10]
nums.sort()
print(nums)
print(nums.sort(reverse=True))
print(nums)
print(nums.sort(reverse=True))
print(nums.sort())
print(nums.reverse())

nums = [3,1,4,1,5,9]
nums.sort()
print(nums)
nums.reverse()
# reverse() it just do the action of reverse
print(nums)


# tuples: ports =(21, 22, 80, 443)
# sets = majmoa az anasor yakta
emails = ["a@x.com","b@x.com","a@x.com"]
unique_emails = set(emails)
print(unique_emails)

I


fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[1])
fruits[1] = "orange"
print(fruits)
fruits.append("kiwi")
print(fruits)
fruits.remove('apple')
print(fruits)
last = fruits.pop()
print(last)
print(fruits)
print(len(fruits))
count_of_orange = fruits.count("orange")
count_of_kiwi = fruits.count("kiwi")
print(count_of_orange, count_of_kiwi)
fruits.clear()
print(fruits)

my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(my_set)

nums = [1, 2, 2, 3, 2, 3, 3, 3, 4, 5, 6, 7, 8, 9]
unique_nums = set(nums)
print(unique_nums)
i = 0
tools = ["nmap", "burp", "sqlmap"]
for t in tools:
    i = i + 1
    print(f"{i}th Tool : {t}")

scores = [45,78,12,90,34]
scores.sort()
print(scores)
scores.reverse()
print(scores)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
print(colors.index('yellow'))
print(colors.index('violet'))
print(colors.index('red'))
print(colors.index('violet'),colors.index('red'),colors.index('violet'),colors.index('yellow'),colors.index('green'),colors.index('blue'))


colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
colors.insert(0, 'white')
print(colors)
colors.insert(1,"yellow")
print(colors)
a = [1, 2]
b = [3, 4]
print(a & b)
a = 3
b = 5
print(a & b)

a = {1,2,3}
b = {3,4,5}
print(a | b)
print(a & b)
# zamanika 2 set dashta basheem set1= {a,b,c} ,set2 ={d,a,f}  set! U set2 = a
# oon "U" ra bakhatir een gozashtam dar comment yani itihad uite


a = {"A","B","C","D","E","F","G"}
b = {"D","E","F","G","H","I","J"}
print(f"Itihad a wa b : {a & b}")
print(f"\nset a wa b : {a | b}")
print(a - b)
set_A = {12,13,15}
set_B = {10,12,13}
print(set_A - set_B)
print(set_A)
print(set_B)

found_emails = ["a@x.com","b@x.com","c@x.com","a@x.com","e@x.com"]
unique = set(found_emails)
# print(unique)
target = input("Enter a email: ")
if target in found_emails:
    print("Unique targers: ",found_emails.index(target) + 1)
else:
    print(f"all emails: {found_emails}")

users = ["admin","user1","guest"]
passwords = {"1234","pass","guest"}
user_input = input("username: ")

if user_input in users:
    idx = users.index(user_input)
    # print(f"password is :", passwords[idx])
    print(users[idx])
else:

    print("User not found")

tasks = []
while True:
    print("\n1. Add task\n2. Show tasks\n3. Remove last task\n4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        task = input("Task: ")
        tasks.append(task)
        print("Task added")
    elif choice == "2":
        print(f"Tasks: {tasks}")
        # print("Task removed")
    elif choice == "3":
        if tasks:
            removed = tasks.pop()
            print(f"Tasks: {removed}")
        else:
            print("No tasks")
    elif choice == "4":
        break






# now i can see good results
# understand 




