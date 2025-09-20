# Healthcare Backend

A simple healthcare backend built with **Django**, **Django REST Framework (DRF)**, and **PostgreSQL**.

## Features
- User registration & login (JWT authentication using SimpleJWT)
- Patient management (CRUD, per-user access)
- Doctor management (CRUD)
- Patient–Doctor mapping

## APIs
- **Auth**: `/api/auth/register/`, `/api/auth/login/`
- **Patients**: `/api/patients/`
- **Doctors**: `/api/doctors/`
- **Mappings**: `/api/mappings/`

## Setup
```bash
git clone https://github.com/AditiGoyal07/healthcare-backend.git
cd healthcare-backend
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Environment Variables
Create a .env file in the project root:
```bash
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=your_secret_key
```

## Testing
Use Postman with the header:
```bash
Authorization: Bearer <access_token>
```
The included healthcare_postman_collection.json can be imported directly to test all APIs.

## Author
**Aditi Goyal**
