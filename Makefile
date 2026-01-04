pull:
	git config --global --add safe.directory /home/mitchbr/Repositories/workout-journal
	git pull

build:
	docker-compose up -d --build
	docker-compose exec -t web python3 manage.py migrate


deploy: pull build
