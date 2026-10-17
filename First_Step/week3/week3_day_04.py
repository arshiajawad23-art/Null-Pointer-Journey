def introduce(name, language="python"):
    print(f"我叫 {name} 在学习 {language}")

introduce("Jawad")

# 我要把这个函数再好一点
def introduce(name, language="python"):
    print(f"我叫 {name} 在学习 {language}")
name =input('enter name: ')
introduce(name)

def power(base, exponent=2):
    return base ** exponent

exp = power(2)
print(exp)
print(power(5))
