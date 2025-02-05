# Zillow MLS

A Django REST Framework (DRF) project that provides API endpoints for Zillow listings.

## Prerequisites
- Python 3.7+
- PostgreSQL
- Pipenv (for dependency management)

## Setup Instructions

### 1. Install Dependencies Using Pipenv
```bash
pip install pipenv
pipenv install
pipenv shell
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

