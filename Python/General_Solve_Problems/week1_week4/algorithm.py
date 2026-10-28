a = int(input("enter a: "))
b = int(input("enter b: "))
c = int(input("enter c: "))


if a > b:
    temp = b
    b = a
    a = temp
if a > c:
    temp = c
    c = b
    b = temp

if a > c:
    temp = c
    c = a
    a = temp

print(f"{a}  {a}  {a}")