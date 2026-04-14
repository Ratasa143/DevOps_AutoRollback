from flask import Flask
import time
app = Flask(__name__)

@app.route("/")
def home():
    time.sleep(6)
    return "<h1>Menu v3 - Slow Response</h1>"

app.run(port=5000)