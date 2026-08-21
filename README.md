# GitHub Snap - GitHub Profile Viewer

A Django 5 web app that fetches and displays public GitHub user data in real time via the GitHub REST API.

![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python)
![Django](https://img.shields.io/badge/Django-5.2-green?logo=django)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?logo=bootstrap)

---

## Features

- Search any GitHub username and view their public profile instantly
- Displays name, bio, location, blog, repos, gists, followers, and avatar
- CSRF-protected POST form with graceful error handling
- Optional GitHub token support for higher API rate limits

## Tech Stack

| Layer | Tool |
|---|---|
| Backend | Django 5.2, Python 3.12 |
| HTTP Client | `requests` |
| Frontend | Bootstrap 5 (CDN) |
| Database | SQLite3 (default) |
| Config | `python-dotenv` |

## Getting Started

```bash
# 1. Clone the repo
git clone https://github.com/hiCXK/github_snap.git
cd github_snap

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install django requests python-dotenv

# 4. (Optional) Add a GitHub token for higher rate limits
echo "GITHUB_TOKEN=your_token_here" > .env

# 5. Apply migrations and run
python manage.py migrate
python manage.py runserver
```

Visit `http://127.0.0.1:8000/app/profile/` and search any GitHub username.

## Project Structure

```
├── app/
│   ├── views.py        # Profile fetch logic
│   ├── urls.py         # App-level URL routing
│   └── ...
└── github_snap/
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    └── urls.py
    └── wsgi.py
├── templates/
│   └── app/
│       └── profile.html
├── manage.py

```

## Notes

- Unauthenticated GitHub API requests are limited to **60/hour**. Add a token in `.env` to raise this to 5,000/hour.

## License

GNU General Public License v3.0
