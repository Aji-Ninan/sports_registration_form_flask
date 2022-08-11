from email import message
import os
from flask import Flask,redirect, render_template, request
from flask_mail import Mail, Message
import sqlite3
from dotenv import load_dotenv


app = Flask(__name__)
load_dotenv()
app.config["MAIL_DEFAULT_SENDER"] = os.getenv("MAIL_DEFAULT_SENDER")
# print (os.getenv("MAIL_DEFAULT_SENDER"))
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")
# print (os.getenv("MAIL_PASSWORD"))
app.config["MAIL_PORT"] = 587
# We're gonna use gmail. Gmail let's you send email on TCP port 587
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_USE_TLS"] = True
# Type of encryption
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
# Private information like email_id and password are stored in environment variables
mail = Mail(app)
# Passing flask application to a function called mail


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
    email = request.form.get("email")
    if not email:
        return render_template("error.html", message="Missing email")
    sport = request.form.get("sport")
    if not sport:
        return render_template("error.html", message="Missing sport")
    if sport not in SPORTS:
        return render_template("error.html", message = "Invalid sport")


    db = get_db_connection()
    db.execute("INSERT INTO registrants (email, sport) VALUES(?, ?)", (email, sport))
    db.commit()
    db.close()

    message = Message("You are registered!", recipients=[email])
    mail.send(message)

    return render_template("/success.html", email=email, sport=sport)



@app.route("/registrants")
def registrants():
        db = get_db_connection()
        registrants = db.execute("SELECT * FROM registrants")
        return render_template("registrants.html", registrants=registrants)
