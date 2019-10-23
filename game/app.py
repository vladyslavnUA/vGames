from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/game1")
def game1():
    return render_template('game1.html')

@app.route("/game2")
def game2():
    return render_template('game2.html')

@app.route("/game3")
def game3():
    return render_template('game3.html')

@app.route("/game4")
def game4():
    return render_template('game4.html')

if __name__ == "__main__":
	app.run(debug=True)
