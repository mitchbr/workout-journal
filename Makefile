pull:
	git pull

deploy:
	docker-compose up -d --force-recreate --build
	docker-compose exec web python3 manage.py migrate

fulldeploy: pull deploy
