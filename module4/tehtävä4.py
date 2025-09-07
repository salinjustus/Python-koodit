import random
oikealuku = random.randint(1, 10)
while True:
    arvaus = input("Guess a number between(1-10):")
    oikeaarvaus = float(arvaus)
    if oikeaarvaus==oikealuku:
        break
    elif oikeaarvaus>oikealuku:
        print("Too high")
    elif oikeaarvaus<oikealuku:
        print ("Too Low")
print("Correct")
