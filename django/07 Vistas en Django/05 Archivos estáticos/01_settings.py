# settings.py
INSTALLED_APPS = [
    'django.contrib.staticfiles'
]

# sirve archivos para vistas app/static
STATIC_URL = 'static/'

# sirve el directorio /static
# app/static/arches.jpg
# app/static/styles.css
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]