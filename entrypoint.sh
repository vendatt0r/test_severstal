#!/bin/sh

echo "Waiting for PostgreSQL..."

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  sleep 1
done

echo "PostgreSQL is up - applying migrations"

python manage.py makemigrations --noinput

python manage.py migrate --noinput

echo "Starting Django server"
python manage.py runserver 0.0.0.0:8000
