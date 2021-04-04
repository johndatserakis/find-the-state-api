# Find The State API

Find all the States in the contiguous USA on a map. Simple enough.

- [Live URL](https://jolly-murdock-43b71d.netlify.app/)
- [Frontend UI GitHub](https://github.com/johndatserakis/find-the-state-ui)
- [Backend API GitHub](https://github.com/johndatserakis/find-the-state-api)

## Run

```bash
# If your running this for the first time, make sure to run the migrations

# Start
docker-compose up -d --build

# Stop
docker-compose down

# Docker cleanup commands https://gist.github.com/johndatserakis/0002d9aded5778f9d0589a23ce1e08d4
```

## Commands While Running

```bash
# Below are commands to be run when the containers are running.

# Run migrations
docker-compose exec api poetry run alembic upgrade head

# Run tests
docker-compose exec api pytest .

# Run a specific script
docker-compose exec api python ./program_scripts/get_state_data.py

# Add a dependency
docker-compose exec api poetry add alembic
```

## Alembic

```bash
# Create migration (called a "revision")
docker-compose exec api poetry run alembic revision -m "Create state table"

# Run migrations
docker-compose exec api poetry run alembic upgrade head

# Downgrade 1 migration file
docker-compose exec api poetry run alembic downgrade -1

# View list of migration files
docker-compose exec api poetry run alembic history
docker-compose exec api poetry run alembic downgrade $Id
```

## View Running API

- http://localhost:8002/ping
- http://localhost:8002/docs
- http://localhost:8002/states

## Built With

- Python 3.8
- FastAPI
- SQLAlchemy
- Alembic
- pymediawiki
- Poetry
- PostgreSQL

## Notes

Below are some links I saved while learning Python.

## Python

- [Packages](https://docs.python.org/3/tutorial/modules.html#packages)
- [Learn X in Y minutes](https://learnxinyminutes.com/docs/python/)

## FastAPI

- [Folder Structure](https://fastapi.tiangolo.com/tutorial/bigger-applications/)

## [Pydantic](https://pydantic-docs.helpmanual.io/usage/types/)

## [encode/databases](https://github.com/encode/databases)

## [SQLAlchemy Core](https://docs.sqlalchemy.org/en/14/core/tutorial.html)
