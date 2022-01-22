from flask import Flask
app = Flask(__name__)

@app.route("/")
def index(name):
    return "Hello "+ name



app.run(debug=True)