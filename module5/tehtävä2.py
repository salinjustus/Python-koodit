luvut = []
luku_str = input("Enter a number: ")
while luku_str!="":
    luku = float(luku_str)
    luvut.append(luku)
    luku_str = input("Enter a number: ")
luvut.sort(reverse=True)
luku5 = luvut[:5]
print(f"The greatest numbers in descending order: ")
for luku in luku5:
    print(f"{luku:.1f}")



