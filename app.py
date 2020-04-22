from flask import Flask, render_template, request



app = Flask(__name__)

@app.route('/index')
def home():
    return render_template("index.html")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/archive')
def archive():
    return render_template("archive.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/single')
def single():
    return render_template("single.html")

@app.route('/static')
def stat():
    return render_template("static.html")


if __name__ == "__main__":
    app.run(debug=True)