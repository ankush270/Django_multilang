# Faq-multilang-api 🌍
 This project is a Django-based FAQ system with multilingual support using Google Translate and caching with Redis.

## 🔹Features
- ✅You can create your own Faq-multilang
- ✅Store and manage FAQs with automatic translations (English, Hindi, Bengali,Gujrati,Telegu,Tamil,Kannada).
- ✅WYSIWYG editor support (`django-ckeditor`).
- ✅REST API with language selection via `?lang=` query parameter.
- ✅Caching with Redis for optimized performance.
- ✅Unit testing with `pytest`
- ✅Admin panel for administrators so they can perform CRUD operations on FAQs.
- ✅PEP8 compliance using `flake8`.


### 📌Prerequisites
- Python 3.10+
- SQLite (default)
- Redis (for caching)
- Ckeditor 

## **Admin Panel**  

#### **🔑Superuser Credentials**
  ### Prerequisites
Before creating a superuser, make sure:
- You have Django installed.
- You have a Django project set up.
- Migrations have been applied.

## Steps to Create a Superuser

### 1. Open the Terminal
Navigate to your project directory where `manage.py` is located.

### 2. Run the Following Command

create a new superuser using:  
```bash
python manage.py createsuperuser
```
### 3. Enter User Details
You'll be prompted to enter the following:
- Username: (Choose a username)
- Email Address: (Enter a valid email)
- Password: (Enter a strong password)
- Confirm Password: (Re-enter the password)

### 4. Start the Server (If Not Running)
 
```bash
python manage.py runserver
```
### 5. Access the Admin Panel
 
```bash
http://127.0.0.1:8000/admin/
```

### 🚀Local Setup
 1. Clone the repository:
   ```bash
   git clone https://github.com/ankush270/Django_multilang.git
   cd BharatFD
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/scripts/activate  # On Windows: venv\Scripts\activate
   ```

3. Ensure Redis is installed and running locally:
   ```bash
   redis-server
   ```
4. Update settings.py to use local Redis:
   ```bash
   CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',  
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
    }
   ```
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

6. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. Run the server:
   ```bash
   python manage.py runserver
   ```

## 🌐API Usage

### Fetch all FAQs (and change faq language accroding to options  avaliablle in dropdown)
```bash
curl http://127.0.0.1:8000/
```

### For Create a new FAQ
```bash
curl http://127.0.0.1:8000/create/
```

### Pass any language code in param(in place of bn)
```bash
curl http://127.0.0.1:8000/?lang=bn
```

## 🧪Running Tests (works with local setup only)
```bash
pytest
```

## 🛠️Code Quality Check
```bash
flake8 faqs/
```
