import math

def calculate_unit_price(sentit, eurot):
    säde = sentit / 2 / 100
    alue = (math.pi * säde ** 2)
    summa = eurot / alue
    return summa
ekacm = float(input("Enter the diameter of the first pizza (cm): "))
ekae = float(input("Enter the price of the first pizza (euros): "))
tokacm= float(input("Enter the diameter of the second pizza (cm): "))
tokae= float(input("Enter the price of the second pizza (euros): "))
ekapizza = calculate_unit_price(ekacm,ekae)
tokapizza = calculate_unit_price(tokacm,tokae)
print(f"Unit price of the first pizza: {ekapizza:.2f} euros/m²")
print(f"Unit price of the second pizza: {tokapizza:.2f} euros/m²")
if ekapizza<tokapizza:
    print("The first pizza provides better value for money.")
else:
    print("The second pizza provides better value for money.")

