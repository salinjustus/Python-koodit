pisteet = int(input())
import math
import random
n1=0
for i in range(pisteet):
    y = random.uniform(-1,1)
    x = random.uniform(-1,1)
    if x**2+y**2<1:
        n1 = n1+1

likiarvo = 4 * n1 / pisteet
toleranssi = 0.01
if abs(likiarvo-math.pi)<toleranssi:
    print("Your solution correctly calculates an approximation of pi!")
    print(likiarvo)













