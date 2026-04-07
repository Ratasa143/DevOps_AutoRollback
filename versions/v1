from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def home():
    # Simulate random failure
    if random.randint(1, 5) == 3:
        return "App Crashed!", 500
    return "App is Running Successfully!"

if __name__ == "__main__":
    app.run(port=5000)