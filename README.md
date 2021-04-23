# Find the State API

Find all the States in the contiguous USA on a map. Simple enough.

- [Live URL](https://jolly-murdock-43b71d.netlify.app/)
- [Frontend UI GitHub](https://github.com/johndatserakis/find-the-state-ui) - Built with TypeScript and React
- [Backend API GitHub](https://github.com/johndatserakis/find-the-state-api) - Built with Python and FastAPI

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
# Below are commands to be run when the containers are running locally with docker-comose

# Run migrations
docker-compose exec api poetry run alembic upgrade head

# Run tests
docker-compose exec api pytest .

# Run a specific script
docker-compose exec api python ./program_scripts/get_state_data.py

# Add a dependency
docker-compose exec api poetry add python-dotenv

# Create poetry.lock file
docker-compose exec api poetry lock
```

## Alembic

```bash
# Create migration (called a "revision")
docker-compose exec api poetry run alembic revision -m "Create score table"

# Run migrations
docker-compose exec api poetry run alembic upgrade head

# Downgrade 1 migration file
docker-compose exec api poetry run alembic downgrade -1

# View list of migration files
docker-compose exec api poetry run alembic history
docker-compose exec api poetry run alembic downgrade $Id
```

## View Running API

- http://localhost:8000/docs
- http://localhost:8000/api/v1/health

## Build for Production

In development I use `docker-compose` because it sets up the `PostgreSQL` dependency nicely. For the production build, I just use a regular Dockerfile, `./app/Dockerfile-production`, to build the API.

```bash
# Currently I'm using AWS ECR for the registry

# From root, build for production using `./app/Dockerfile-production` Dockerfile
docker build \
-t $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG \
-f ./app/Dockerfile-production ./app \
--build-arg POSTGRES_USER=$POSTGRES_USER \
--build-arg POSTGRES_PASSWORD=$POSTGRES_PASSWORD \
--build-arg POSTGRES_HOST=$POSTGRES_HOST \
--build-arg POSTGRES_DB=$POSTGRES_DB

# Run what you built locally to test
docker run -dit --publish 8000:8000 --restart unless-stopped $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG

# Lastly push to your container registry of choice
docker push $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG
```

## Built With

- Python 3.8
- FastAPI
- SQLAlchemy
- Alembic
- pymediawiki
- Poetry
- PostgreSQL

## Notes

- There is a very rudimentary auth token "check" on the `score` `post` request. Don't do something like this in a production app. Whenever I want to secure my API's I use a `JWT` token that a user receives after registering and logging in. That is out of scope for this project, but may be added in the future. I have another [open sourced API](https://github.com/johndatserakis/koa-vue-notes-api) that features this if you'd like to recreate [that flow](https://github.com/johndatserakis/koa-vue-notes-api#user-authentication-process). I'll probably get around to adding it to this app at some point - I just have to draw the line somewhere, ha.
- Below are some links I saved while learning Python.

## Python

- [Packages](https://docs.python.org/3/tutorial/modules.html#packages)
- [Learn X in Y minutes](https://learnxinyminutes.com/docs/python/)

## FastAPI

- [Folder Structure](https://fastapi.tiangolo.com/tutorial/bigger-applications/)

## [Pydantic](https://pydantic-docs.helpmanual.io/usage/types/)

## [encode/databases](https://github.com/encode/databases)

## [SQLAlchemy Core](https://docs.sqlalchemy.org/en/14/core/tutorial.html)
