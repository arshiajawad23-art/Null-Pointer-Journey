import random

pc_guess = random.randint(1,100)
guess = int(input("enter your guess: "))

while guess != pc_guess:
    if guess > pc_guess:
        print('mine is less than',guess)
    elif guess < pc_guess:
        print("mine is more than",guess)
    
    guess = int(input("enter your guess: "))
print("Wow you done it")


Pc_Guess = random.randint(1,20)
_guess = ''
while _guess != Pc_Guess:
    _guess = int(input('enter guess: '))
    if _guess > Pc_Guess:
        print('no, mine is less')
    elif _guess < Pc_Guess:
        print("no mine is bigger")
    else:
        print('Ok you done it mine is ',Pc_Guess)



secret_number = random.randint(1,100)
attempts = 0
guess = 0
print("==== game of number guessing ====")

while secret_number != guess:
    guess = int(input('enter guess number: '))
    attempts += 1
    if guess > secret_number:
        print(f'mine is lesser than your write this {guess}')
    if guess < secret_number:
        print(f'mine is bigger than your write this {guess}')
    else:
        print(f"========= OK mine is {guess} ==========")
    
print(f"after {attempts} time finally you succeed to find the secret_number ")