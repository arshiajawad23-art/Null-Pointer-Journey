def add_print(a,b):
    print(a+b)

def add_return(a,b):
    return a+b

x = add_print(5,5)
print(x)
print('='*30)
y = add_return(5,5)
print("y *2 :", y * 2)


def is_even(number):
    if number % 2==0:
        return True
    else:
        return False
result = is_even(4)
if result:
    print(f"number is even: {result}")

