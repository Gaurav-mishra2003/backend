# 🧠 Resume Upload API (Django + DRF + JWT)

A simple RESTful API that allows users to upload resumes (PDF or TXT) and receive AI-generated suggestions (dummy logic).

---

## 🚀 Features

- Upload `.pdf` or `.txt` resume files
- Returns dummy "AI suggestions" 
- JWT Authentication with `djangorestframework-simplejwt`
- View all resumes or fetch by ID
- Resume metadata includes `title`, `created_at`, 
- Built using Django REST Framework
- SQLite/PostgreSQL supported

---

## 🧱 Tech Stack

- Python 3.10+
- Django 4.x
- Django REST Framework
- Simple JWT (`djangorestframework-simplejwt`)
- SQLite (default) or PostgreSQL
- Postman for testing APIs

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/resume-api.git
cd resume-api



2. Create Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
If requirements.txt is not present, install manually:


pip install django djangorestframework djangorestframework-simplejwt
4. Migrate the Database

python manage.py migrate
5. Create Superuser (Optional)

python manage.py createsuperuser
6. Run the Development Server

python manage.py runserver
🔐 Authentication
Obtain JWT Token:
POST /api/token/


{
  "username": "your_username",
  "password": "your_password"
}
Refresh Token:
POST /api/token/refresh/

{
  "refresh": "your_refresh_token"
}
