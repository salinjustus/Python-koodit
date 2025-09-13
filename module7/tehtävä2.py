names = set()
syöte = input("Give a name: ")
if syöte in names:
    print("Existing name")
else: print("New name")
names.add(syöte)
print(names)
