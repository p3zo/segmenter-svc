define run_docker_cmd
	docker compose run --rm \
		--use-aliases \
		app \
		"$(1)"
endef

.PHONY: build build_zip clean dev prod shell stop

build:
	@echo "Building image:"
	docker compose build

build_zip: clean
	@echo "Building Lambda zip:"
	./aws_lambda/scripts/build_lambda.sh segmenter_lambda aws_lambda/segmentation_handler.py

clean:
	@echo "Cleaning up artifacts:"
	rm -rf aws_lambda/dist

dev:
	@echo "Starting container(s) in dev mode:"
	docker compose -f docker-compose.yml \
	  -f docker-compose.dev.yml up -d && \
	  docker compose logs --follow

dev_server:
	@echo "Starting app server in dev mode:"
	docker compose --profile dev exec app ./deploy/tools/dev_server

prod:
	@echo "Starting containers in prod mode:"
	docker compose up -d

prod_server: prod
	@echo "Starting app server in prod mode:"
	docker compose --profile prod exec app ./deploy/tools/server

shell:
	@echo "Getting a shell inside the container:"
	docker compose exec app bash

stop:
	@echo "Stopping containers:"
	docker compose down
