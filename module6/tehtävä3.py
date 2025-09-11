def gallons_to_liters(gallon):
        lasku = gallon * 3.785
        return lasku
while True:
    input2 = float(input("Enter a volume in American gallons (negative value to quit): "))
    tulos = gallons_to_liters(input2)
    if input2 < 0:
        break
    print(f"{input2} American gallons is {tulos:.2f} liters.")
print("Program finished.")

