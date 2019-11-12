import time
import random
import math

print('\n--------- 1. Basic Test ---------')
name = 'Mithra'
print('Hello World! My name is ' + name + '.') 

print('\n--------- 2. Show me the MONEY! ---------')
cash = 19867324678987.99 
take_home = cash/5
op = 'Each robber takes home a WHOPPING ${:.2f}'.format(take_home)
print(op)

print('\n--------- 3. Formatting Them Strings ---------')
first = 'Mithra'
last = 'Vankipuram'
op = 'First Name: {}, Last Name: {}'.format(first,last)
print(op)

print('\n--------- 4. String Indices ---------')
#num_str = 1234 ### This won't work becaue only strings can be indexed this way
#print (num_str[-2])
test_str = 'YOLO'
for letter in range(0, len(test_str)):
    #time.sleep(1)    
    print('Give me an {}'.format(test_str[letter]))
#time.sleep(1)
print('That gives us {}'.format(test_str))
print('\n--------- 5. Mileage Convertor ---------')
print('How many kms did you run today? ')
#kms = float(input())
kms = 10
miles = kms/1.60934
print(f'Awesome! You ran {kms} kms. That is %.2f miles!!!' % miles)

print('\n--------- 5. Boolean and Conditional ---------')
print('\nChoosing a number for you!')
#for i in range(0,5):
#    time.sleep(1)
#    print('.')
choice = random.randint(1,10)
if choice == 7:
    print(f'The choice is {choice}. You are Lucky!!!')
else:
    print(f'The choice is {choice}. BOOO! You are Unlucky!!!')

print('\nChoosing a food for you!')
#for i in range(0,5):
#    time.sleep(1)
#    print('.')
food = random.choice(['apple','grape', 'bacon', 'steak', 'worm', 'dirt'])
if food == 'apple' or food == 'grape':
    print(f'Your choice is {food}. It is a fruit.')
else:
    if food == 'bacon' or food == 'steak':
        print(f'Your choice is {food}. It is a meat.')
    else:
        if food == 'worm' or food == 'dirt':
            print(f'Your choice is {food}. It is YUCK.')

print('\nLet\'s see whether you can enter is COOL party! Wait here.')
for i in range(0,3):
    #time.sleep(1)
    print('.')
print('How old are you?')
#age = input()
age = 35

if age:
    try:
        age = int(round(float(age)))
        if age < 0 or age > 120:
            print('You are a liar or a VAMPIRE! Either way, GET OUTTA here you whanker!')
        elif age < 18:
            print('Sorry, we don\'t allow babies in here')
        elif age >= 18 and age < 21:
            print('You can enjoy the party, but NO drinking ;)')
        else:
            print('Here is your wristband. Enjoy the party and remember, well drinks are $3 off!')
    except ValueError:
        print('No BLUBBERRING! Get OUTTA here!')
else:
    print('SILENCE is not going to get you anywhere. Get OUTTA here!')