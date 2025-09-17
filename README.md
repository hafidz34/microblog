# Microblog
A simple Flask microblog application with PostgreSQL backend, user authentication, and CRUD posts.

## Features
- User registration & login
- Create, edit, and delete posts
- PostgreSQL as database backend

## Requirements
- Python 3.12+
- PostgreSQL
- Virtualenv (`.venv`)

## Getting Started

### 1. Clone & setup venv
```bash
git clone https://github.com/hafidz34/microblog.git
cd microblog
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
# source .venv/bin/activate
pip install -r requirements.txt

### 2. Create .env
Create a file named .env in the project root (do not commit this file):
```bash
SECRET_KEY=change-this
# Replace <password>/host as needed; if your password contains @ : # & ? you must URL-encode it
DATABASE_URL=postgresql+psycopg2://postgres:<password>@127.0.0.1:5432/microblog
FLASK_APP=app:create_app
FLASK_ENV=development

### 3. Create the database (once)
```bash
# Windows (psql)
psql -U postgres -h 127.0.0.1 -c "CREATE DATABASE microblog;"
# macOS/Linux (example)
# createdb microblog

### 4. Apply migrations (create tables)
```bash
flask db init
flask db migrate -m "init schema"
flask db upgrade

### 5. Run the app
```bash
flask run
