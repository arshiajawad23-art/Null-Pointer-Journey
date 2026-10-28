def hello():
    print("Hello World")

hello()

def add():
    print(2+3)
add()

def say_hello(name):
    print(f"Hello {name}")

say_hello("David")

def _say_hello(name):
    return f"Hello {name}"

hello = _say_hello("David")
print(hello)