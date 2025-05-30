DOCKER_COMPOSE_FILE = docker compose --verbose -f docker-compose.yml
MANAGE = cd src && python manage.py

run-docker:
	$(DOCKER_COMPOSE_FILE) down
	$(DOCKER_COMPOSE_FILE) up --build

run-server:
	$(MANAGE) runserver

makemigrations:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate
