from flask import abort, Flask, jsonify, request

app = Flask(__name__)
forts = {"Alchemist" : {"id":1, "owned_by_team": 1,
                        "latitude": 42.359092,
                        "longitude": -71.093987,
                        "is_in_battle": False},
         "Stata Center": {"id":2, "owned_by_team":2,
                        "latitude": 42.362172,
                        "longitude": -71.090021,
                        "is_in_battle": False}}
@app.route("/")
def index():
    loc = request.args.get("loc","")
    results = []
    if str(loc) in forts:
        results.append(forts[str(loc)])
    elif len(str(loc))==0:
        results = forts.values()
    return jsonify(data = results)

if __name__ == "__main__":
    app.run(port=8000, debug = True)
    
