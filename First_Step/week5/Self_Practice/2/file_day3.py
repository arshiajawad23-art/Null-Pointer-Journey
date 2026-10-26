file_name = input("Enter file name: ")

try:
    with open("file_name.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")


# بهبود یافته :
while True:
    print("for exit write ...  ' exit ' ")
    file_name = input("Enter file name: ")
    if file_name == "exit":
        break
        
    try:
        with open("file_name.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("File not found")
