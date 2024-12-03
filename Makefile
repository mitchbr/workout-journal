fulldeploy:
	git pull
	yarn
	yarn build
	sudo systemctl start workoutjournal.service