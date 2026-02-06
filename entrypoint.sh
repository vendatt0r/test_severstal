#!/bin/sh

set -e

: "${POSTGRES_HOST:?Need to set POSTGRES_HOST}"
: "${POSTGRES_PORT:?Need to set POSTGRES_PORT}"

echo "Waiting for PostgreSQL at $POSTGRES_HOST:$POSTGRES_PORT..."

while ! nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
  sleep 1
done

echo "PostgreSQL is up - applying migrations"

python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "Starting Django server on 0.0.0.0:8000"
exec python manage.py runserver 0.0.0.0:8000
