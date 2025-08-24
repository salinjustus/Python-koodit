import math
talents_str = input("Enter talents: ")
talents = float(talents_str)
pounds_str = input("Enter pounds: ")
pounds = float(pounds_str)
lots_str = input("Enter lots: ")
lots = float(lots_str)
talent = (talents * 20 * 32 * 13.3)
pound = (pounds * 32 * 13.3)
lot = (lots * 13.3)
total_grams = pound + lot + talent
kilograms = int(total_grams // 1000)
remaining_grams = total_grams - (kilograms * 1000)
factor = 10 ** 2
remaining_grams = math.floor(remaining_grams * factor) / factor
print("The weight in modern units:")
print(f"{kilograms} kilograms and {remaining_grams:.2f} grams.")