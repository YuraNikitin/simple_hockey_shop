SHELL=/bin/sh

DIR=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
VERSION=$(shell grep -o '^[0-9]\+\.[0-9]\+\.[0-9]\+' CHANGELOG.rst | head -n1)

# Colors
Color_Off=\033[0m
Cyan=\033[1;36m
Red=\033[1;31m


version:  ## Версия проекта
	@echo $(VERSION)

help:  ## Помощь
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

build:  ## Сборка проекта
	@echo -e 'Сборка проекта'
	@docker-compose build

start:  ## Запуск проекта
	@echo -e 'Сборка проекта'
	docker-compose up backend frontend

migration:  ## Создание новой миграции
	@[ -z "$(msg)" ] && \
		echo '${Red}Добавьте msg${Color_Off}' || \
	  docker-compose run \
			-v $(DIR)/backend/migrations:/usr/src/app/migrations \
			-v $(DIR)/backend/alembic.ini:/usr/src/app/alembic.ini \
		  api sh -c "alembic revision --autogenerate -m '$(msg)'"
	@sudo chown $$USER:$$USER -R $(DIR)/backend/migrations/versions

migrate:  ## Обновление БД проекта
	@docker-compose run \
	  -v $(DIR)/backend/migrations:/usr/src/app/migrations \
	  -v $(DIR)/backend/alembic.ini:/usr/src/app/alembic.ini \
	  backend sh -c "alembic `([ ! -z "$(downgrade)" ] && echo "downgrade -$(downgrade)") || \
	                      ([ ! -z "$(upgrade)" ] && echo "upgrade $(upgrade)") || \
	                      echo "upgrade head"`"

pgadmin:  # pgadmin
	@docker-compose up pgadmin

.PHONY: version help build
.DEFAULT_GOAL := help
