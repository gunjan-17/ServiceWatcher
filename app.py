from flask import Flask, render_template, request, redirect, url_for
import subprocess

app = Flask(__name__)

def get_services():
    with open("services.txt", "r") as f:
        services = [line.strip() for line in f.readlines()]
    
    status = {}
    for service in services:
        result = subprocess.run(["systemctl", "is-active", service], capture_output=True, text=True)
        status[service] = result.stdout.strip()
    return status

@app.route("/")
def index():
    statuses = get_services()
    return render_template("index.html", statuses=statuses)

@app.route("/restart/<service>")
def restart_service(service):
    subprocess.run(["sudo", "systemctl", "restart", service])
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

