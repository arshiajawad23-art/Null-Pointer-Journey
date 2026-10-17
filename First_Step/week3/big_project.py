# guess_number_game

import random

def play_game():
    print("=== Stat Game of guess_number ===")
    secret_number = random.randint(1, 50)
    attempts = 0

    while True:
        guess = int(input("Guess a number between 1 and 50: "))
        attempts += 1
        # این روش را من کار گرفتم
        # تا یک چیزی جدید شود
        if guess == secret_number:
            print(f" wow! it is. after {attempts} you don it")
            break
        elif guess > secret_number:
            print("请问再低点儿")
        else:
            print("请问再高点儿")

def main():
    play_game()
    print("=== Game Ends ===")

main()