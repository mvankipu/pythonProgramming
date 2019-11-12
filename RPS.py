import time
import random
import math

print('\n--------- Rock, Paper or Scissors ---------')

print('Let\'s play ROCK, PAPER, SCISSORS!')

#Trials Input
print('Best of 3 or 5?')
trials = input()

if trials:
    try:
        trials = int(round(float(trials)))
        if trials != 3 and trials != 5:
            print('...........')
            time.sleep(1)
            trials = 3
            print('Uh...Let\'s assume best of 3')
            time.sleep(1)
    except ValueError:
        trials = str(trials)
        if trials.lower() == 'three':
            trials = 3
        elif trials.lower() == 'five':
            trials = 5
        else:
            print('...........')
            time.sleep(1)
            trials = 3
            print('Uh...Let\'s assume best of 3')
            time.sleep(1)
else:
    print('...........')
    time.sleep(1)
    trials = 3
    print('Uh...Let\'s assume best of 3')
    time.sleep(1)

#Countdown
print(f'\nAll right! Best of {trials} match commencing in...')
countdown = 3
for i in range(0,countdown):
    time.sleep(1)
    print(countdown-i)
time.sleep(2)
print('GO!')
time.sleep(1)

#Game
win = False
player_score = 0
ai_score = 0
winner = None

while win == False:

    rps_choice = random.choice(['rock','paper', 'scissors'])
    print(f'\nTrials {i+1} Type (1) for ROCK, (2) for PAPER or (3) for SCISSORS:')
    user_choice = input()    

    #Check if user entered any input
    if user_choice:

        #Check if user followed instructions
        try:
            user_choice = int(round(float(user_choice)))
            
            #They put in a number but it was a stupid one
            if user_choice < 1 or user_choice > 3:
                print('...........')
                time.sleep(1)
                print('Uh...I don\'t accept garbage. Because I am nice, I\'ll pick something at random <eyeroll>')
                user_choice = random.choice(['rock','paper', 'scissors'])
                time.sleep(1)
            
            #They put in the right number and followed instructions
            else:
                if user_choice == 1:
                    user_choice = 'rock'
                elif user_choice == 2:
                    user_choice = 'paper'
                else:
                    user_choice = 'scissors'

        #User didn't follow instructions
        except ValueError:
            #Did user do something intelligent
            user_choice = str(user_choice)
            
            #Checking to see if they were smart or stupid
            if user_choice.lower() != 'rock' and user_choice.lower() != 'paper' and user_choice.lower() != 'scissors':
                #Somewhat stupid user - maybe typo?
                if user_choice[0].lower() == 'r':
                    user_choice = 'rock'
                elif user_choice[0].lower() == 'p':
                    user_choice = 'paper'
                elif user_choice[0].lower() == 's':
                    user_choice = 'scissors'
                else:
                    #User is really, REALLY stupid
                    print('...........')
                    time.sleep(1)
                    print('Uh...Maybe you shouldn\'t be playing this game?... I should take over and pick something for you <pity>')
                    user_choice = random.choice(['rock','paper', 'scissors'])
                    time.sleep(1)
    #No input
    else:
        print('...........')
        time.sleep(1)
        print('Uh...I\'ll pick something at random. GEEZ!')
        user_choice = random.choice(['rock','paper', 'scissors'])
        time.sleep(1)
    
    #The Reveal!!!
    time.sleep(1)
    print(f'\nYou chose...{user_choice.title()}')
    time.sleep(1)
    print(f'RANDO AI chose...{rps_choice.title()}')
    time.sleep(1)

    #GameLogic
    if (user_choice == 'rock' and rps_choice == 'paper') or (user_choice == 'paper' and rps_choice == 'scissors') or (user_choice == 'scissors' and rps_choice == 'rock'):
        ai_score = ai_score + 1
        print(f'{rps_choice.title()} beats {user_choice.title()} - RANDO AI wins.')
    
    elif (user_choice == 'rock' and rps_choice == 'scissors') or (user_choice == 'paper' and rps_choice == 'rock') or (user_choice == 'scissors' and rps_choice == 'paper'):
        player_score = player_score + 1
        print(f'{user_choice.title()} beats {rps_choice.title()} - You win!')
    else:
        print('It\'s a ................................... DRAW')

    if trials == 3 and (player_score>1 or ai_score>1):
        diff = player_score - ai_score
        if diff >= 1:
            win = True
            winner = 1
        elif diff <= -1:
            win = True
            winner = 2
    elif player_score>2 or ai_score>2:
        diff = player_score - ai_score
        if diff >= 1:
            win = True
            winner = 1
        elif diff <= -1:
            win = True
            winner = 2
    print(f'Player Score: {player_score} ---------- RANDO AI Score: {ai_score}')

#Results
#time.sleep(2)
print('\n<<<GAME OVER>>>')
if winner == 1:
    print(f'{player_score} to {ai_score} - Congratulations! You WIN!!!')
elif winner == 2:
    print(f'{player_score} to {ai_score} - Sorry! AI Wins.')
else:
    print('ERROR - This should not be happening')

                



