import random

def coin_flip ():
    var = random.randint(0,1)
    if var==0:
        return "Heads"
    else:
        return "Tails"

print(coin_flip())