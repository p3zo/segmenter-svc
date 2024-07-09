.PHONY: build dev dev_server prod prod_server shell stop

build:
	@echo "Building image:"
	docker compose build

dev:
	@echo "Starting container(s) in dev mode:"
	docker compose --profile dev -f docker-compose.yml -f docker-compose.dev.yml up -d

dev_server: dev
	@echo "Starting app server in dev mode:"
	docker compose --profile dev exec app ./deploy/tools/dev_server

prod:
	@echo "Starting containers in prod mode:"
	docker compose --profile prod up -d

prod_server: prod
	@echo "Starting app server in prod mode:"
	docker compose --profile prod exec app ./deploy/tools/server

prod_shell: prod
	@echo "Getting a shell inside the prod container:"
	docker compose --profile prod exec app bash

shell: dev
	@echo "Getting a shell inside the dev container:"
	docker compose --profile dev exec app bash

stop:
	@echo "Bringing Docker down:"
	docker compose --profile dev --profile prod down
