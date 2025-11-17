import json

from flask import Flask, request, jsonify, Response


app = Flask(__name__)
@app.route('/alkuluku/<int:luku1>')
def alkuluku(luku1):
    if luku1 < 2:
        is_prime = False
    else:
        is_prime = True
        for i in range(2, int(luku1 ** 0.5) + 1):
            if luku1 % i == 0:
                is_prime = False
                break
    return jsonify({
        "Number": luku1,
        "isPrime": is_prime
    })

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