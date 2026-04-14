from flask import Flask, render_template, request, redirect
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/deploy', methods=['POST'])
def deploy():
    version = request.form['version']
    subprocess.run(["python", "deploy.py"], input=version, text=True)
    return redirect('/')

@app.route('/start_monitor')
def start_monitor():
    subprocess.Popen(["python", "monitor.py"])
    return redirect('/')

@app.route('/rollback')
def rollback():
    subprocess.run(["python", "rollback.py"])
    return redirect('/')

@app.route('/logs', methods=['POST'])
def logs():
    log = request.form['log']
    content = ""
    if os.path.exists(f"{log}.log"):
        with open(f"{log}.log") as f:
            content = f.read()
    return render_template("logviewer.html", content=content)

if __name__ == "__main__":
    app.run(port=7000)