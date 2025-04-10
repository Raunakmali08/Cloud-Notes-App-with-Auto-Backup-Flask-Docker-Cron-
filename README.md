# 📝 Cloud Notes App with Auto Backup (Flask + Docker + Cron)

A simple yet powerful web-based note-taking app built with Flask, Dockerized for easy deployment, and equipped with automated database backups via cron jobs.

---

## 🚀 Features

- ✨ Add and view notes using a clean web interface
- 💾 Notes stored in an SQLite database (`notes.db`)
- 🐳 Dockerized for simple deployment
- 🔁 Automated backups via `cron` inside the container
- 💣 Manual backups with `backup.sh`
- 🔒 Secure and isolated runtime

---

## 📁 Project Structure

cloud-notes-app/ ├── app.py ├── templates/ │ └── index.html ├── notes.db ├── backup.sh ├── cron.log ├── crontab.txt └── Dockerfile


---

## 🔧 Setup & Run

### 1. Clone the Repo

```bash
git clone https://github.com/Raunakmali08/Cloud-Notes-App-with-Auto-Backup-Flask-Docker-Cron-.git
cd Cloud-Notes-App-with-Auto-Backup-Flask-Docker-Cron-

###2. Build the Docker Image
bash:
docker build -t cloud-notes .

###3. Run the Container
bash:
docker run -p 5000:5000 --name cloud-notes-app cloud-notes

Open your browser and visit: http://localhost:5000

###4. Manual Backup
bash:
docker exec cloud-notes-app /app/backup.sh
Backups will be stored in /app/backups inside the container.


---


Author
👤 Raunak Mali


---

License
This project is licensed under the MIT License - see the LICENSE file for details.

---
