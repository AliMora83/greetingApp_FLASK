from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "5#y2L_namka_09"


@app.route("/")
def index():
    flash("Hello 🏆 What's your name?")
    return render_template("index.html")


@app.route("/greet", methods=['POST', 'GET'])
def greeter():
    name = request.form["name_input"]
    flash("🏆 Hi " + str(name) + ", great to see you! 🥳")
    if not name:
        return "failure"

    return render_template("success.html")
