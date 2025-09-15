import random
def roll_dice():
    return random.randint(1, 6)
heitot = []
while True:
    heitto=roll_dice()
    print(heitto)
    heitot.append(heitto)
    if heitto == 6:
        break




