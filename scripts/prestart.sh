#!/bin/bash

# Run migrations
poetry run alembic upgrade head
