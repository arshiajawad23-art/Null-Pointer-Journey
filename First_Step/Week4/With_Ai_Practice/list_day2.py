my_scores = []
# برای راحتی کار نخواستم سه بار با سه اسم متقاوت input بگیرم
# با یک حلقه چلوگیری ازین تکرار ها با کردم
for i in range(3):
    score = int(input("Enter your score: "))
    my_scores.append(score)
print(my_scores)
my_scores.sort()
print(my_scores)
print(f"最高分数: {max(my_scores)}")
print(f"最低分数: {min(my_scores)}")