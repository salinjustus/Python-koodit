luvut = []
luku1 = input("Enter a number (or press Enter to quit):")
while luku1!="":
    luku=float(luku1)
    luvut.append(luku)
    luku1 = input(" Enter a number (or press Enter to quit):")
print(f" Smallest number: {min(luvut):.1f}")
print(f"Largest number: {max(luvut):.1f}")






