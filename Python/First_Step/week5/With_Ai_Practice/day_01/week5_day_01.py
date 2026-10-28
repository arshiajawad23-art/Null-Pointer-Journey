file = open("text.txt", "r")
content = file.read()
print(content)
file.close()


with open("text.txt", "r") as file:
    content = file.read()
    print(content)

with open("text.txt", "r") as file:
    lines = file.readlines()
    print(f"\n--- line quantity: {len(lines)} ---")
    for line in lines:
        print(f"line: {line.strip()}")

with open("text.txt", "r") as f:
    text = f.read()
    words = text.split(" ")
    print(f"\nword quantity : {len(words)}")


with open("test.txt" ,"r") as file:
    print('--- read the content ---')
    print(file.read())

# result : when I don't have this file the error show : No such file or directory

# I think this part is OK
with open("test.txt" ,"a" ) as file:
    print('--- write the content ---')
    test = file.write('Hello world\n')
    print(test)
with open("test.txt" ,"r") as file:
    print('--- Read the content ---')
    print(file.read())


with open("test.txt" ,"r") as f:
    lines = f.readlines()
    print(f"\nnumbers of line : {len(lines)}")
    for line in lines:
        print(f"line : {line.strip()}")

#再好一点
with open("test.txt" ,"r") as f:
    lines = f.readlines()
    print(f"\nnumbers of line : {len(lines)}")
    i = 0
    for line in lines:
        i += 1
        print(f"line{i} : {line.strip()}")

print('='*30)

with open("test.txt" ,"r") as f:
    lines = f.readlines()
    print(f"\nnumbers of line : {len(lines)}")
    i = 0
    for index,line in enumerate(lines):
        print(f"line{index} : {line.strip()}")
# f.write()  write content / f.read()  read the content / f.readlines()  read the line of content
# "r" read mode  / "w"  write mode  / "a" add a content in my text



with open("test.txt" ,"r") as f:
    test = f.read()
    words = test.split()
    print(f"quantity of words: {words}") # result in the list data type
    print(f"quantity of words: {len(words)}")