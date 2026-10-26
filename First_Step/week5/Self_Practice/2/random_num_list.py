import random



rand_list2= []
random_list = [random.randint(1, 10) for i in range(10)]

print(random_list)


rand_list1 = []
for i in range(10):
    rand_list1.append(random.randint(1, 10))

print(rand_list1)

with open("random_num_list.txt" ,"w" ,encoding="utf-8") as f:
    for i in range(10):
        f.write(str(rand_list1[i]) + "\t-_-\t")

with open("random_num_list.txt" ,"r" ,encoding="utf-8") as f:
    sum = 0
    for i in range(len(rand_list1)):
        sum += i
        print(i,' ---- ',end='')
        print()
        print(sum," ---- " ,end='')
print('\n\n\n')

with open("random_num_list.txt" ,"r" ,encoding="utf-8") as f:
    sum = 0
    for i in rand_list1:
        sum += i
    print(sum)






