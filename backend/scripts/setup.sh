#!/bin/sh

alembic upgrade head

python -m app.scripts.create_admin

fastapi run app/main.py --port 80