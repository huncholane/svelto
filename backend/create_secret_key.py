from django.core.management.utils import get_random_secret_key
import os


FILE = os.path.join(os.path.dirname(__file__), 'backend/secret_key.py')
with open(FILE, 'w') as f:
    f.write(f"SECRET_KEY = '{get_random_secret_key()}'")
