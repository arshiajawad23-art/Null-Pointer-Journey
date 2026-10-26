def calculator(num1,num2,operation):
    if operation == '+':
        return num1+num2
    elif operation == '-':
        return num1-num2
    elif operation == '*':
        return num1*num2
    elif operation == '/':
        if num2 == 0:
            print("impossible")
        else:
            return num1/num2


print(calculator(1,3,'+'))
print(calculator(5,3,'+'))
print(calculator(-1,3,'+'))
print(calculator(5,2,'-'))
print(calculator(-1,2,'*'))
print(calculator(4,2,'*'))

while True:
    try:
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
        break
    except ValueError:
        print('Please enter numbers only')


operate = input("enter the operation you want to perform with this function [+ | - | * | /]: ")
result = calculator(num1,num2,operate)
if operate == "+":
    print(f"addition of {num1} + {num2} = {result}")
elif operate == "-":
    print(f"subtraction of {num1} - {num2} = {result}")
elif operate == "*":
    print(f"multiply of {num1} * {num2} = {result}")
elif operate == "/":
    if num2 == 0:
        print('امکان ندارد تقسیم بر صفر تعریف نشده')
    else:
        print(f"division of {num1} / {num2} = {result}")



# چالش خواندن فایل

file = input("enter the name of the file you want to read: ")

try:
    with open(file.txt, 'r', encoding= "utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("File Not Found")


# چالش محدودیت سنی
# بگذار اینجا دوباره یک انتقاد کنم
try:
    age = int(input("enter your age: "))
    if age < 18:
        raise ValueError ("You are too young to enter this site")
    print("Welcome!")
except ValueError as e:
    print(f"Error: {e}")

