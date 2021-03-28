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
	docker-compose up backend

.PHONY: version help build
.DEFAULT_GOAL := help
