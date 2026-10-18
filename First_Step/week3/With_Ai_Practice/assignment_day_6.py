import random

def play_game():
    print("=== Stat Game of guess_number ===")
    secret_number = random.randint(1, 50)
    attempts = 0

    while True:
        guess = int(input("Guess a number between 1 and 50: "))
        attempts += 1
        if guess == secret_number:
            print(f" wow! it is. after {attempts} you don it")
            option = input("你要再次继续下去 （Would you like to play again）? (y/n)：")
            if option == "y":
                play_game()
            elif option == "n":
                print("Thanks for playing!")
                break
            else:
                print("你的输入不对")
                break
        elif guess > secret_number:
            print("请问再低点儿")
        else:
            print("请问再高点儿")

def main():
    play_game()
    print("=== Game Ends ===")

main()



# الان تلاش برای بهبود و درست کردن چالش
def play_game():
    print("=== Stat Game of guess_number ===")
    secret_number = random.randint(1, 50)
    attempts = 0

    while True:
        guess = int(input("Guess a number between 1 and 50: "))
        attempts += 1
        if guess == secret_number:
            print(f" wow! it is. after {attempts} you don it")
            while True:
                option = input("would you like to play again? (y/n)")
                if option == "y":
                    play_game()
                elif option == "n":
                    return "thanks for playing!"
                else:
                    print("please enter valid input")
        elif guess > secret_number:
            print("请问再低点儿")
        else:
            print("请问再高点儿")

def main():
    play_game()
    print("=== Game Ends ===")

main()