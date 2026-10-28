phone_book ={
    "Ali" : "0700000000",
    "Sara": "0780000000"
}
print(phone_book.keys())
print(phone_book.values())
print(f"the keys of my dict is {phone_book.keys()}")
print(f"the values of my dict is {phone_book.values()}")

for name, number in phone_book.items():
    print(f"{name} : {number}")

print(f"{phone_book.get('Reza', 'Not Found')}")