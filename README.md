# Healthcare Backend

A simple healthcare backend built with **Django**, **Django REST Framework (DRF)**, and **PostgreSQL**.

## Features
- User registration & login (JWT authentication using SimpleJWT).
- Patient management (CRUD, per-user access).
- Doctor management (CRUD).
- Patient–Doctor mapping.

## APIs
- **Auth**: `/api/auth/register/`, `/api/auth/login/`
- **Patients**: `/api/patients/`
- **Doctors**: `/api/doctors/`
- **Mappings**: `/api/mappings/`

## Setup
```bash
git clone <your-repo-link>
cd healthcare
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
