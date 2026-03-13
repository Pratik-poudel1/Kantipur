# Kantipur News Portal

A full-featured news website built with **Django 5.2**, inspired by the Kantipur media brand. Supports multiple news categories, user authentication, comments, search, and password reset via email.

## Features

- 📰 News articles organized by categories (National, International, Business, Sports, Entertainment, Technology, Health, Education, Travel, Music)
- 🔍 Search functionality
- 💬 User comments on articles
- 🔐 User registration, login, logout
- 📧 Password reset via email
- 🛡️ Django Admin panel for managing news and categories

## Tech Stack

- Python 3.x
- Django 5.2.4
- SQLite (development)
- Pillow (image handling)

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Kantipur.git
cd Kantipur
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory:

```
SECRET_KEY=your-secret-key-here
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

## Project Structure

```
Kantipur/
├── Kantipur/        # Project config (settings, urls)
├── news/            # Main app (models, views, templates)
├── static/          # CSS and static assets
├── media/           # Uploaded images (not tracked in git)
├── manage.py
└── requirements.txt
```

## Admin Panel

Visit `/admin/` and log in with your superuser credentials to manage news articles and categories.
