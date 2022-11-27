from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "5#y2L_namka_09"

students = []


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/registrants")
def registrants():
    return render_template("registered.html", students=students)


@app.route("/register", methods=['POST', 'GET'])
def register():
    name = request.form("name")
    dorm = request.form("dorm")
    if not name or not dorm:
        return render_template("failure.html")
    students.append(f"{name} from {dorm}")
    return render_template("success.html")
