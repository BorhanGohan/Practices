import random

def guess(x):
    random_number=random.randint(1,x)
    print(random_number)
    guess=0
    while guess!=random_number:
        guess=int(input('Guess a number between 1 and 10:'))
        if guess>random_number:
            print('Keep going lower')
        elif guess<random_number:
            print('Keep going higher')
    print('The number is found!')
guess(10)