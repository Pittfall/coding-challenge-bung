# Zillow MLS API

A Django REST Framework (DRF) project that provides API endpoints for Zillow listings.


## Prerequisites
- Python 3.7+
- PostgreSQL
- Virtualenv (optional but recommended)

## Setup Instructions

### 1. Create Virtual Environment & Install Dependencies
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure Database
Ensure PostgreSQL is running and update the `DATABASES` setting in `challenge/settings.py` if needed:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'zillow_mls_db',
        'USER': 'postgres',
        'PASSWORD': 'postgres123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 3. Run Migrations
```bash
python manage.py migrate
```

### 4. Create Superuser
```bash
python manage.py createsuperuser
```

### 5. Start the Server
```bash
python manage.py runserver
```

