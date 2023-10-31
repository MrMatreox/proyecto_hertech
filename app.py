from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/landing_page")
def landing_page():
    return render_template("landing_page.html")

if __name__ == '__main__':
    app.run (debug=True)