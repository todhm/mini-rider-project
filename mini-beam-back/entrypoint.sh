#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z $DB_HOST 5432; do
  sleep 0.1
done
alembic upgrade head
echo "PostgreSQL started"

exec "$@"