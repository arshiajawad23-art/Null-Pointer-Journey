print("==== perfect number analyzer ====")
while True:
    num = int(input("Enter numbers: "))
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += num
    if sum == num:
        print("perfect")
        break
    else:
        print("not perfect")