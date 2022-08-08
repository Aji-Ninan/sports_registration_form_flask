from flask import Flask, render_template, request

app = Flask(__name__)

REGISTRANTS ={}
# {} is for dictonaries


SPORTS = [
    "Cricket",
    "Basketball",
    "Football",
    "Tennis",
    "Volleyball",
    "Kabadi"
]
# pass these into the template

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    if not name:
        return render_template("error.html", message="Missing Name")
    sport = request.form.get("sport")
    if not sport:
        return render_template("error.html", message="Missing sport")
    if sport not in SPORTS:
        return render_template("error.html", message = "Invalid sport")

    REGISTRANTS[name] = sport 
    # keys and values

    return render_template("registrants.html", registrants=REGISTRANTS)

