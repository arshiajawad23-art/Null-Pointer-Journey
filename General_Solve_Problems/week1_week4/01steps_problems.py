celsius = int(input("Enter Temprature: "))
farenhite = (celsius * 9/5) + 32
print(f"farenhite: {farenhite}")
list1 = [1,2,[12,34,[23,22,[11,00,23]]],23,44,51]
sub_list = [19,00,[12,11],2]

list1.insert(0,sub_list)
print(list1)
_list = [1,2,3]

new_list = sorted(_list, reverse=True)
print(new_list)
new_list2 = reversed(new_list)
print(new_lsit2)


names = ['ali', 'reza', 'ahmad', 'ghadir']
ages = [21, 18, 33, 25]
#

for i in range(len(names)):
    print(f"{names[i]}  :  {ages[i]}")

for i,j in zip(names, ages):
    print(i, " : ",j)

number2 = []

numbers = [12, 75, 150, 180, 145, 525, 50]
for number in numbers:
    if number % 5 ==0:
        if number > 500:
            break
        elif number > 150:
            continue
        number2.append(number)
print(number2)


list_number = []

for i in range(4):
    number = int(input("Enter a number: "))
    if number > 20 and number < 80:
        list_number.append(number)
    else:
        print("Sorry, the number is out of range")
        break
print(list_number)
print(f"max_of_list_number = {max(list_number)}")
print(f" min_of_list_number = { (max(list_number) ) *2}")


count =1

while count <= 5:
    number = int(input(">>>: "))
    if not (number > 20 and number <80):
        print("Number is out of range")
        break
    else:
        list_number.append(number)
        count = count + 1
print(list_number)

print(max(list_number))

print("در اول عدد که میخواهید توان اون را محاسبه کنید  در دوم تعداد را بنویسید ")
x = int(input("Enter X: "))
y = int(input(" Enter Y: "))

pow = 1
for i in range(0,y):
    pow = pow * x
print(pow)
st = input("Enter a string: ")

character = ""
for i in range(0,len(st)):
    character += st[i]+' _ '

print(character)



while True:
    num = int(input("Enter number: "))

    sum = 0
    for i in range(1,num):
        if num % i == 0:
            sum += i

    if num == sum:
        print("Yes it is perfect")
    else:
        print("it is not perfect")
fruits = ['banana','apple','orange']

for fruit in fruits:
    if fruit == 'orange':
        continue
    print(fruit)

print("=======================")

for fruit in fruits:
    if fruit =="aple":
        continue
    print(fruit)


for i in range(1,21):
    if i % 2 == 0:
        print(i)

n = 1
for i in range(1,20):
    n += 1
    if  i%2 != 0:
        continue
    print(i)

for i in range(1,21):
    if  i%2 != 0 :
        continue
    print(i)

secret = 'python'

for secure in secret:
    if secure == 'p':
        secret2 = secret.replace("p","j")
        # print(secret)
print(secret2)

user_input = input(">>>: ")

if user_input[:5].lower() == "hello":
    print("$0")
elif user_input.strip().lower()[:5] == "hello":
    print("$0")
elif user_input[:3].lower().strip() == 'key' \
or user_input[:3].lower().strip() == "how":
    print('$20')
else:
    print("$100")


user_input = input('Enter your file name: ')

if ".jpg" in user_input or ".png" in user_input:
    print("Image.jpg")
elif ".mp4" in user_input or ".3gp" in user_input or ".avi" in user_input:
    print("video.mp4")
else:
    print("I just know the images and videos files")