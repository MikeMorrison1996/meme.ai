# Meme.AI 🚀 – Developer Setup Guide (Visual + Easy Mode)

Welcome to the Meme.AI team! Here's your plug-and-play guide to spin up our app and get coding like a beast. No guesswork. No excuses. Just follow the steps.👇

---

## 💻 Prerequisites

Make sure you have these installed first:

| Tool         | Why You Need It         | Download Link                            |
|--------------|--------------------------|------------------------------------------|
| Git          | Version control          | https://git-scm.com                      |
| Docker       | Run containers           | https://www.docker.com/products/docker-desktop |
| PyCharm      | Our main IDE             | https://www.jetbrains.com/pycharm/      |

---

## 🧱 Project Setup (One-Time)

### 1. Clone the Repo
```bash
git clone https://github.com/MikeMorrison1996/meme.ai.git
cd meme.ai
```

### 2. Run It All with Docker 🐳
```bash
docker compose up --build
```

If you moved Docker files to `/docker`, use:
```bash
docker compose -f docker/docker-compose.yml up --build
```

### 3. Open in Browser
Once it's running, visit:
```
http://localhost:5000
```
> You should see: "Meme.AI is running inside Docker!"

---

## 👨‍💻 Start Coding

### File Structure
```
meme.ai/
├── app/
│   ├── scraper/                # Python logic (Pump.fun scraper, bot, etc.)
│   ├── templates/              # HTML (Flask views)
│   ├── static/                 # JS/CSS assets
│   ├── routes.py               # Flask routes
│   └── __init__.py             # Flask app entry
│
├── docker/                    # Dockerfile + compose config (optional move)
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── run.py                     # App launcher
├── requirements.txt           # Python packages
├── README.md                  # This file
```

---

## 🧠 Common Commands

| Task                 | Command                                      |
|----------------------|----------------------------------------------|
| Rebuild container    | `docker compose up --build`                  |
| Stop everything      | `CTRL + C` in the terminal                   |
| View logs            | `docker compose logs`                        |

---

## 🏁 You're Ready!
If you see the app on [http://localhost:5000](http://localhost:5000), you’re golden. Time to build the future of meme trading.

Have fun & ship it! 💸

