import time
for i in range(1,21):
    if i==4 or i==13:
        print(f'{i} is an Unlucky Number.')
    if i%2 == 0:
        print(f'{i} is an Even Number.')
    else:
        print(f'{i} is an Odd Number.')
    time.sleep(1)