products = {
    "Laptop": 1000,
    "mobile": 500,
    "power_bank": 100
}

for name,cost in products.items():
    print(f"{name}: {cost}")
#  مجموع کل محصولات را با یک متغیر شمارنده حساب و چاپ کن
total_cost = 0
for name,cost in products.items():
    total_cost += int(cost)
print('_'*40)
print(f"total_price: {total_cost}")
print('_'*40)

