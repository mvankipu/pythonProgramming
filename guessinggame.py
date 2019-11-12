import random

while True:
    number = random.randint(1,10)
    match = False
    while match == False:
        user_guess = int(input('Guess the number I am thinking of: '))
        if(user_guess<number):
            print('Too Low.')
        elif(user_guess>number):
            print('Too High.')
        else:    
            print(f'You guessed right! I was thinking of {number}!')
            match = True
    var = input('Play again? (y/n): ')
    if var == 'n' or var == 'N':
        break

