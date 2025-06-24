from flask import Flask, request

app = Flask(__name__)

populations = {
    "China":{
        "Shanghai":"24,256,800",
        "Beijing":"21,516,000"
    },
    "India":{
        "Delhi":"16,349,831"
    }
}

@app.route("/population", methods=['GET'])
def get_population():
    args = request.args.to_dict()
    city = None
    country = None
    for argname in args:
        if argname.lower() == "city":
            city = args[argname]
        if argname.lower() == "country":
            country = args[argname]
    if (city is None) or (country is None) or (country not in populations) or (city not in populations[country]):
        return "#N/A#", 404

    return "<b>{}</b>".format(populations[country][city])

if __name__ == "__main__":
    app.run()