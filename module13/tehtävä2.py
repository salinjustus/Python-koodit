import json
from flask import Flask, request, jsonify, Response
import mariadb

app = Flask(__name__)
@app.route('/kenttä/<string:icao>')
def alkuluku(icao):

    try:
        yhteys = mariadb.connect(
            user="python",
            password="huihai",
            host="localhost",
            database="flight_game"
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")


    kursori = yhteys.cursor()
    kursori.execute(f"SELECT name, municipality, iso_country FROM airport WHERE ident = '{icao}'")
    airport = kursori.fetchone()

    if airport:
        name,municipality,iso_country =airport
        result= {
        "ICAO": icao,
        "Name": name,
        "Municipality": municipality
    }
    else:
        result = {"ERROR" : "Airport could not be found"}

    return jsonify(result)

@app.errorhandler(404)
def page_not_found(errorcode):
    response = {
        "status" : "404",
        "text" : "Invalid endpoint"
    }
    json_response= json.dumps(response)
    return Response(response=json_response, status = 404, mimetype = "application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
