pull:
	git pull

deploy:
	docker-compose up -d --force-recreate --build

fulldeploy: pull deploy
