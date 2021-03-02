#!/bin/sh

set -e

timer="5"

until runuser -l postgres -c 'pg_isready' 2>/dev/null; do
  >&2 echo "Postgres is unavailable - sleeping for $timer seconds"
  sleep $timer
done

>&2 echo "Postgres is up - running migrations"

pip install -e .

alembic upgrade head

>&2 echo "Migrations complete - running Flask"

python runner.py
