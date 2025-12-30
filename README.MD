# 📁 DocDrop

DocDrop is a simple Django-based file sharing web app that lets users upload and download files easily.

## 🚀 Features
- User registration and login (custom authentication + Google login)
- Secure file upload and download
- Role-based access control for files
- Form validation and error handling
- Minimal, modern UI design
- Organized file storage for each user

## 🛠️ Tech Stack
- Django
- Django Allauth (for social login)
- HTML, Tailwind CSS
- SQLite (default)

## ⚙️ Installation
```bash
git clone https://github.com/tshering10/DocDrop.git
cd DocDrop
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
