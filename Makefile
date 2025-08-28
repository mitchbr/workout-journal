pull:
	git pull

deploy:
	docker-compose up -d --build
	docker-compose exec web python3 manage.py migrate

fulldeploy: pull deploy
