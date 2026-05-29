from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    total = 2500
    return render_template("index.html", total=total)

if __name__ == "__main__":
    app.run(debug=True)