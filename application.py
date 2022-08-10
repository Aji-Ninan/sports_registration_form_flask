from flask import Flask,redirect, render_template, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('sport_registration.db')
    conn.row_factory = sqlite3.Row
    return conn


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


    db = get_db_connection()
    db.execute("INSERT INTO registrants (name, sport) VALUES(?, ?)", (name, sport))
    db.commit()
    db.close()

    return redirect("/registrants")



@app.route("/registrants")
def registrants():
        db = get_db_connection()
        registrants = db.execute("SELECT * FROM registrants")
        return render_template("registrants.html", registrants=registrants)
