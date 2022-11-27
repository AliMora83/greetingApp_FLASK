from flask import Flask, render_template, request, flash
import csv

app = Flask(__name__)
app.secret_key = "5#y2L_namka_09"

students = []
name = request.form.get("name")
city = request.form.get("city")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=['POST'])
def register():

    if not name or not city:
        return render_template("failure.html")
    students.append(f"{name} from {city}")
    file = open("registered.csv", "a")
    writer = csv.writer(file)
    writer.writerow((request.form.get("name")), request.form.get("city"))
    file.close()

    return render_template("success.html")


@app.route("/registered")
def registered():
    with open("registered.csv", "r") as file:
        reader = csv.reader(file)
        students = list(reader)

    return render_template("registered.html", students=students)
