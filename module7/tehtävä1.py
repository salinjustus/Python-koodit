def get_season(num):
    if num == 1 or num == 2 or num == 12:
        season = "winter"
    elif 2 < num < 6:
        season = "spring"
    elif 5 < num < 9:
        season = "summer"
    elif 8 < num < 12:
        season = "autumn"
    else:
        season = "invalid"
    return season
numero = int(input("Enter the number of a month (1-12): "))

if  numero > 12:
    print(f"You entered: {numero}")
    print("Please enter a number between 1 and 12.")
elif numero<=0:
    print(f"You entered: {numero}")
    print("Please enter a number between 1 and 12.")
else:
    print(f"You entered: {numero}")
    print(f"The season is {get_season(numero)}.")


