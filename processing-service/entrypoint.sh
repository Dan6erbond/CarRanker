#!/bin/sh

cd app

pip install -e .

alembic upgrade head

python runner.py
