heitot = int(input("How many dice to roll: "))
import random
summa = 0
for i in range(heitot):
    heitto = random.randint(1,6)
    summa += heitto
print(f"Sum of the dice: {summa}")
















