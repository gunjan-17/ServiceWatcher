# ServiceWatcher 🛠️

**ServiceWatcher** is a real-time Linux service monitoring and control dashboard built with **Flask**, **Bash**, and **systemd**. It allows you to keep track of critical system services like `nginx`, `ssh`, and others via a simple web interface. The dashboard supports auto-refreshing service status, manual restart buttons, and automatic recovery of failed services.

---

## 🔧 Features

- 🔍 **Live Monitoring**: View real-time status of system services.
- 🔁 **Manual Control**: Restart services from the web dashboard with one click.
- ⚙️ **Auto-Recovery**: Detect and restart failed services using a Bash script.
- 🔐 **Secure Execution**: Uses `sudoers` configuration for passwordless but restricted command execution.
- 🛠️ **Runs as a Background Service**: Managed via `systemd`.

---

## 📁 Project Structure

servicewatcher-dashboard/ ├── app.py # Flask app to serve the dashboard ├── services.txt # List of services to monitor ├── service_watcher.sh # Bash script to auto-restart failed services ├── requirements.txt # Python dependencies ├── templates/ │ └── index.html # HTML template for dashboard UI ├── static/ │ └── style.css # CSS styling for dashboard └── README.md # This file
