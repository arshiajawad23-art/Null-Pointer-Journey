import datetime

with open("app_log.txt", "a" ,encoding="utf-8") as log:
    log.write(f"Hello World")
    log.write(f"   ----  added in f {datetime.date.today()} \n")

with open("app_log.txt", "r" ,encoding="utf-8") as log:
    quantity = log.readlines()
    print(f"program run {len(quantity)}times ")
