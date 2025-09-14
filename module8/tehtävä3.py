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

def get_airport_coordinates(icao_code):
    kursori = yhteys.cursor()
    kursori.execute(f"SELECT latitude_deg, longitude_deg  FROM airport WHERE ident = '{icao_code}'")
    kaikki = kursori.fetchall()
    return kaikki
from geopy import distance
def run_airport_distance():
    coordinates1 = input("Enter the ICAO code of the first airport: ")
    airport1 = get_airport_coordinates(f"{coordinates1}")
    coordinates2 = input("Enter the ICAO code of the second airport: ")
    airport2 = get_airport_coordinates(f"{coordinates2}")
    tulos = distance.distance(airport1, airport2).km
    print(f"Distance between {coordinates1} and {coordinates2}: {tulos:.2f} kilometres")

run_airport_distance()

