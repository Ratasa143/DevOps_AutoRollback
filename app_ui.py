from flask import Flask, render_template, request, redirect
import subprocess, shutil, os, signal
from monitor import monitor
from logger import log
import threading

app = Flask(__name__)
app_process = None

def start_app():
    global app_process
    app_process = subprocess.Popen(["python", "app/app.py"])
    log("App started")

def stop_app():
    global app_process
    if app_process:
        app_process.terminate()
        log("App stopped")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/deploy', methods=['POST'])
def deploy():
    version = request.form['version']
    stop_app()
    shutil.copy(f"versions/{version}/app.py", "app/app.py")
    start_app()
    log(f"{version} deployed and started")
    return redirect('/')

@app.route('/start_monitor')
def start_monitor():
    t = threading.Thread(target=monitor)
    t.start()
    return redirect('/')

@app.route('/logs')
def logs():
    content = ""
    if os.path.exists("system.log"):
        with open("system.log") as f:
            content = f.read()
    return f"<pre>{content}</pre><a href='/'>Back</a>"

if __name__ == "__main__":
    app.run(port=7000)