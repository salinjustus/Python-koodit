import random
code_3 = ""
for _ in range(3):
    digit = random.randint(0, 9)
    code_3 += str(digit)
code_4 = ""
for _ in range(4):
    digit = random.randint(1, 6)
    code_4 += str(digit)
print("3-digit code:", code_3)
print("4-digit code:", code_4)