# ServiceWatcher 🛠️

A lightweight Linux service monitoring and recovery tool with a web dashboard. Built using Bash and Flask to monitor and restart critical services like nginx, ssh, etc.

---

## 🔧 Features

- 🔍 **Live Monitoring**: View real-time status of system services.
- 🔁 **Manual Control**: Restart services from the web dashboard with one click.
- ⚙️ **Auto-Recovery**: Detect and restart failed services using a Bash script.
- 🔐 **Secure Execution**: Uses `sudoers` configuration for passwordless but restricted command execution.
- 🛠️ **Runs as a Background Service**: Managed via `systemd`.

---

## 🛠️ Technologies Used
- Python (Flask)
- Bash
- Linux systemd
- HTML/CSS

---

## 📁 Project Structure

```
servicewatcher/
├── app.py
├── services.txt
├── README.md    
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── style.css
```

---

## 🚀 Getting Started

### Clone this repository:
```
git clone https://github.com/YOUR_USERNAME/servicewatcher.git
cd servicewatcher
```

### Add your service names to services.txt

### Run the web dashboard
```
sudo python3 app.py
```
### Open your browser and visit:
[http://localhost:5000](http://localhost:5000)

### To run the auto-recovery script:
```
sudo bash service_watcher.sh
````
---

## 🔐 Permissions

Edit your sudoers file to allow passwordless service restarts:
```
sudo visudo
```
Add:
```
your_username ALL=NOPASSWD: /bin/systemctl restart *
```

---

## 📸 Demo
![image](https://github.com/user-attachments/assets/6eb64d14-cd25-4698-9e00-6ab2f5a64760)

---

## ✅ Future Improvements
- Add service history logging
- Integrate email/Telegram alerts
- Add user authentication for dashboard access

