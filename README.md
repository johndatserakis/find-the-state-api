# find-the-state-api

## Docker

```bash
# Run
docker-compose up -d --build

# Stop
docker-compose down

# Docker cleanup commands https://gist.github.com/johndatserakis/0002d9aded5778f9d0589a23ce1e08d4

# Run tests
docker-compose exec api pytest .

# Run a specific file. Make sure the container is running
docker-compose exec api python ./scripts/get_state_data.py

# Add a dependency
docker-compose exec api poetry add pymediawiki
```

- http://localhost:8002/ping
- http://localhost:8002/docs
- http://localhost:8002/states

## Python

First time using Python

### Links

- [Learn X in Y minutes](https://learnxinyminutes.com/docs/python/)
