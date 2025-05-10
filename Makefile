DOCKER_COMPOSE_FILE = docker compose --verbose -f docker-compose.yml

run:
	$(DOCKER_COMPOSE_FILE) down
	$(DOCKER_COMPOSE_FILE) up --build
