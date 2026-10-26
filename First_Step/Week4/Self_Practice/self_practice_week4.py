import random

# random_nums

= [random.randint(1,10) for _ in range(10)]
print(f"Random lists: {random_nums}")

for i in range(1,10):
    print(i)

all_tools = ["nmap","sqlmap","msfconsole","netcat","john","pychat", "pypreter", "pymap"]
python_tools =[]
for tool in all_tools:
    if "py" in tool.lower():
        python_tools.append(tool)
print(f"Python-based tools: {python_tools}")
while True:

    words = ["firewall","eccryption","exploit","payload"]
    print(words,"alwas you can exit write 'exit'")
    secret = random.choice(words)
    guess = input("Guess the word: ")
    if guess.lower() == "exit" :
        break

    elif guess.lower() == secret.lower():
        print("Correct!")
    else:
        print(f"Wrong! It was {secret}")
i = 1
log = "192.168.1.1 - - [01/Jan/2025] 'GET /' 200 0.232\n192.168.1.2 - - [01/Jan/2025] 'POST /login' 403 0.122\n192.168.1.1 - - [01/Jan/2025] 'GET /' 200 0.211"
ips = []
for lin in log.split("\n"):
    ip = lin.split()[0]
    ips.append(ip)
    #print(f"{i}th line: **** {lin} ****")
    #i += 1

unique_ips = set(ip)
print(ips)
print(f"Unique IPs: {len(unique_ips)}")



list = ["jawad","fawad","sajad","hamad"]
print(list.pop(2))
emails = [
    "dwva90@gmial.com",
    "bottlenec24@yahoo.com",
    'movieborad@outlook.com',
    "nullskat@goole.com"
    ,"dvwawow90@gmial.com",
]
i=1
for item in set(emails):

    print(f"{i}item: {item}")
    i += 1

n = [random.randint(1, 10) for i in range(10)]
for _ in n:
    pass

print(n)


if max(n) in n:
    print(max(n))
empty_list =[]
words = input("Enter email: ")
if words.split("@"):
    empty_list.append(words)
print(empty_list)


