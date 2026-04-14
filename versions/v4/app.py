from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    x = 10/0
    return str(x)

app.run(port=5000)