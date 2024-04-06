#!/bin/bash

alembic upgrade head

uvicorn src.main:app  --bind=0.0.0.0:8000
