inches = float(input("Enter length in inches (negative value to quit): "))
centimetres = inches * 2.54
while centimetres>=0:
    print(f"{inches} inches is {centimetres:.2f} centimeters")
    inches = float(input("Enter length in inches (negative value to quit): "))
    centimetres = inches * 2.54
print("Program ended.")


