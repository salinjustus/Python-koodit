import random
def roll_dice(maksimi):
    return random.randint(1, maksimi)


heitot = []
maksimi = int(input())
while True:
    heitto = roll_dice(maksimi)
    print(heitto)
    heitot.append(heitto)
    if heitto == maksimi:
        break
