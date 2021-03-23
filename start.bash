#!/usr/bin/env bash

for i in {60..1}; do
    echo waiting db connection... ${i}
    sleep 1
done

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --no-input
python manage.py runserver 0.0.0.0:8000
