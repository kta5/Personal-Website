from flask import Flask, render_template, request
app= Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/process", methods=['GET', 'POST'])
def process():
    return "Hello " + request.form['student_name'] + " and your ID number is " + request.form['id']


if __name__ == "__main__":
    app.run(host="localhost", port=5000,
    debug=True)