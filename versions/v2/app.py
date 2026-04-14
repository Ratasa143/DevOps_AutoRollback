from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Menu v2 - Prices Updated</h1>"

app.run(port=5000)