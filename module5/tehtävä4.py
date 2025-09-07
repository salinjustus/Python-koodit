kaupungit = []
kerrat = 0
for kerrat in range(0,5):
    kaupunki = input("Enter the name of a city: ")
    kaupungit.append(kaupunki)
    kerrat = kerrat+1
print("")
print("")
print("The cities you entered: ")
for kaupunki in kaupungit:
    print(kaupunki)



