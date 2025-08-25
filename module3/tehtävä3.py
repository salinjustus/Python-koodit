gender = input("Enter biological gender (male/female): ").lower()

if gender=="male":
    hemoglobin = float(input("Enter hemoglobin value (g/l): "))
    if 134<=hemoglobin<=167:
        print("Your hemoglobin is normal.")
    elif hemoglobin<134:
        print("Your hemoglobin is low.")
    elif hemoglobin>167:
        print("Your hemoglobin is high.")
elif gender=="female":
    hemoglobin = float(input("Enter hemoglobin value (g/l): "))
    if 117 <= hemoglobin <= 155:
        print("Your hemoglobin is normal.")
    elif hemoglobin < 117:
        print("Your hemoglobin is low.")
    elif hemoglobin > 155:
        print("Your hemoglobin is high.")
else:
    input("Enter hemoglobin value (g/l): ")
    print("Invalid gender.")

