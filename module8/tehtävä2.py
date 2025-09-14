import mariadb

try:
    yhteys = mariadb.connect(
            user="python",
            password="huihai",
            host="localhost",
            database="flight_game"
            )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")

def get_airports_by_country(country_code):
    kursori = yhteys.cursor()
    kursori.execute(f"SELECT type FROM airport WHERE iso_country = '{country_code}'")
    types_calc = {}
    for (types,) in kursori.fetchall():
        if types in types_calc:
            types_calc[types]+=1
        else:
            types_calc[types]=1
    print(f"Airports in {country_code}:")
    for types, amount in types_calc.items():
        print(f"{amount} {types} airports")

def run_country_program():
    maa = input("Enter the country code (e.g., FI for Finland): ")
    get_airports_by_country(f"{maa}")

run_country_program()