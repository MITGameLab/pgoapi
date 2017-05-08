from flask import abort, Flask, jsonify, request
from math import pow

app = Flask(__name__)
forts = {"Alchemist" : {"id":1, "owned_by_team": 1,
                        "latitude": 42.359092,
                        "longitude": -71.093987,
                        "is_in_battle": False},
         "Stata Center": {"id":2, "owned_by_team":2,
                        "latitude": 42.362172,
                        "longitude": -71.090021,
                        }}
@app.route("/")
def index():
    lat = request.args.get("lat","")
    lng = request.args.get("lng","")
    print (lat,lng)
    loc= (lat,lng)
    results = []
    for fort in forts.values():
        if almost_equal(fort["latitude"],lat) and almost_equal(fort["longitude"],lng):
            results.append(fort)
    return jsonify(data = results)

def almost_equal(a,b,precision = 3):
    print abs(a-float(b))
    print pow(10, -precision)
    return (abs(a-float(b)) < (pow(10, -precision)))

if __name__ == "__main__":
    app.run(port=8000, debug = False)

    
