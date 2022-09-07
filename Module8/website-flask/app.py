from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")