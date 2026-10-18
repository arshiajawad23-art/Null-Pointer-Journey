print("=== The null Pointer Game ===")
def print_seperator():
    print('='*30)
# 把这函我从week3_day_01复制了， 为了顺利写代码
def show():
    print("1. Start Game")
    print("2. Settings")
    print("3. Exit")
show()
print_seperator()

print()

null = "=== The null Pointer Game ==="
start = "Start Game"
set = "Settings"
ex = "Exit"
# 在这里我把它放在一个（variable 😁🤣 我不认识中文variable叫什么）
# و این کار را برای راحتی کار تا درچندین جای ازین متغیر من استفاده کنم
def null_pointer():
    print(null)
    print(f"1.{start}")
    print(f"2.{set}")
    print(f"3.{ex}")
null_pointer()
print_seperator()

print()

def game_show():
    print(null)
def _start():
    print(f"1.{start}")
def _settings():
    print(f"2.{set}")
def _ex():
    print(f"3.{ex}")
game_show()
_start()
_settings()
_ex()
print_seperator()