# find-the-state-api

## Docker

```bash
# Run
docker-compose up -d --build

# Stop
docker-compose down

# Docker cleanup commands https://gist.github.com/johndatserakis/0002d9aded5778f9d0589a23ce1e08d4

# Below are commands to be run when the containers are running

# Run tests
docker-compose exec api pytest .

# Run a specific file. Make sure the container is running
docker-compose exec api python ./program_scripts/get_state_data.py

# Add a dependency
docker-compose exec api poetry add email-validator
```

- http://localhost:8002/ping
- http://localhost:8002/docs
- http://localhost:8002/states

## Python

### [Packages](https://docs.python.org/3/tutorial/modules.html#packages)

### Links

- [Learn X in Y minutes](https://learnxinyminutes.com/docs/python/)

## FastAPI

### [Folder Structure](https://fastapi.tiangolo.com/tutorial/bigger-applications/)

## [Pydantic](https://pydantic-docs.helpmanual.io/usage/types/)

## [encode/databases](https://github.com/encode/databases)

## [SQLAlchemy Core](https://docs.sqlalchemy.org/en/14/core/tutorial.html)
