# Run without docker

* `cd pygraz-server`
* `poetry install`
* `poetry run ./run.py`
* visit <http://localhost:8080>

# Build and run with Docker-Composer

* `docker-compose up`
* visit <http://api.localhost>

# Build and run for production with Docker-Composer

* `docker-compose -f docker-compose.prod.yml up`
* visit <https://pygraz.duckdns.org>