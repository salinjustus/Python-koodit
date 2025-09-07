luku = int(input("Enter an integer: "))

alkuluku = True
for i in range(2, int(luku ** 0.5) + 1):
        if luku % i == 0:
            alkuluku = False
            break
if luku == 1:
    alkuluku = False
if luku == 0:
    alkuluku = False

if alkuluku:
        print(f"{luku} is a prime number.")
else:
        print(f"{luku} is not a prime number.")