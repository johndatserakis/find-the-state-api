# Find The State API

Find all the States in the contiguous USA on a map. Simple enough.

- [Live URL](https://jolly-murdock-43b71d.netlify.app/)
- [Frontend UI GitHub](https://github.com/johndatserakis/find-the-state-ui)
- [Backend API GitHub](https://github.com/johndatserakis/find-the-state-api)

## Run

```bash
# Start
docker-compose up -d --build

# Stop
docker-compose down

# Docker cleanup commands https://gist.github.com/johndatserakis/0002d9aded5778f9d0589a23ce1e08d4
```

## Commands While Running

```bash
# Below are commands to be run when the containers are running

# Run tests
docker-compose exec api pytest .

# Run a specific script
docker-compose exec api python ./scripts/get_state_data.py

# Add a dependency
docker-compose exec api poetry add alembic
```

## Alembic

```bash
# Create migration (called a "revision")
poetry run alembic revision -m "Create state table"

# Run migrations
poetry run alembic upgrade head
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
