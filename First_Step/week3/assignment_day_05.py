def calcultor(num1,num2,operation):
    if operation == '+':
        return num1+num2
    elif operation == '-':
        return num1-num2
    elif operation == '*':
        return num1*num2
print(calcultor(1,3,'+'))
print(calcultor(5,3,'+'))
print(calcultor(-1,3,'+'))
print(calcultor(5,2,'-'))
print(calcultor(-1,2,'*'))
print(calcultor(4,2,'*'))

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
operate = input("enter the operation you want to perform with this function [+/-/*]: ")
result = calcultor(num1,num2,operate)
if operate == "+":
    print(f"addition of {num1} + {num2} = {result}")
elif operate == "-":
    print(f"subtraction of {num1} - {num2} = {result}")
elif operate == "*":
    print(f"multiply of {num1} * {num2} = {result}")
