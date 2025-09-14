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

def hae_lentokentät_icao(icao):
    kursori = yhteys.cursor()
    kursori.execute(f"SELECT name, municipality, iso_country FROM airport WHERE ident = '{icao}'")
    airport = kursori.fetchone()
    if airport:
        name, municipality, iso_country = airport
    print(f"Airport name: {name}")
    print(f"Municipality: {municipality}")
    print(f"Country: {iso_country}")

haku = input("Enter the ICAO code of an airport: ")
hae_lentokentät_icao(f'{haku}')