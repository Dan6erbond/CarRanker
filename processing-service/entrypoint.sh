#!/bin/sh

pip install -e .

alembic upgrade head

python runner.py
