.PHONY: init; deploy; coverage; flake;

ifeq (deploy,$(firstword $(MAKECMDGOALS)))
    RUN_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
    $(eval $(RUN_ARGS):;@:)
endif

deploy:
	bash deploy.sh $(RUN_ARGS)

init:
	docker-compose up -d --build
	docker-compose exec mini-beam-back make preparedata

coverage:
	docker-compose exec mini-beam-back python -m pytest --cov="."

flake:
	docker-compose exec mini-beam-back flake8 .

checkblack:
	docker-compose exec mini-beam-back black . --diff

checkisort:
	docker-compose exec mini-beam-back isort . --diff

isort:
	docker-compose exec mini-beam-back isort .

black:
	docker-compose exec mini-beam-back black .