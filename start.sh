#!/bin/bash
python create_secret_key.py

cd frontend
npm run build

cd ../backend
python manage.py runserver
