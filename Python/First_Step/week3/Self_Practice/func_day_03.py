def argument(a,b,c):
    return a+b+c

print(argument(1,2,3))

def default_parameter(a,b=10,c=2):
    return a+b+c

print(default_parameter(1,2,3))
print(default_parameter(1,2,))
print(default_parameter(1,))
print(default_parameter(a = 5))

def say_hello(name):
    return f"Hello {name}"

name = input("What is your name? ")
print(say_hello(name))



# return type 1. return 2. yield 3. pass


def hello_world():
    print("Hello, World!")
    pass
hello_world()

def _my_word():
    return "Hello, World!"
print(_my_word())
a = 20
def hello_world():
    global a
    a = 10

    if a == 20:
        print("Hello, World!")
        pass
    print(f"global a is {a}, and local a is {a}")

hello_world()

def my_world(a):
    if a == 1:
        return "Hello, World!"

    return "My  World!"
print(my_world(1))




def iterable():
    yield 1
    yield 2
    yield 3
    yield 4
for i in iterable():
    print(i)

def square_nums(a):
    a =1
    while True:
        yield a * a
        a += 1
for i in square_nums(10):
    if i > 100:
        break
    print(i)

def tuple_return():
    name = "Jawad"
    id = 1234
    return (name, id)

tup = tuple_return()
print(tup)

def tuple_return():
    name = "Jawad"
    id = 1234
    return (name, id)
name, id = tuple_return()
print(name)
print(id)
print(name, id)
print(type(name))

def list_return():
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = a + b
    print(c)
    return c
print(list_return())

def list_return():
    number = 12
    _class = 'A'
    return [_class, number]
print(list_return())
number , _class = list_return()
print(number)
print(_class)
print(type(number))
print(type(_class))
print(type(list_return()))

print("="*40)
def dict_return():
    name = "Jawad"
    budget = 200
    lead = dict()
    lead["name"] = name
    lead["budget"] = budget
    return lead

print(dict_return())

def secont_time_dict_return():

    leads = dict()
    leads["name"] = "Jawad"
    leads["budget"] = 200
    return leads
second = secont_time_dict_return()
print(second)


