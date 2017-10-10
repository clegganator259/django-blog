APP_NAME=django-blog
APP_PORT=8000
BASE_SETTINGS_FILE=./base-settings.env
SECRET_SETTINGS_FILE=./secrets.env
build:
	pip freeze > requirements.txt
	docker build -t $(APP_NAME) .

run:
	docker run -d --rm -p=$(APP_PORT):$(APP_PORT) --env-file=$(BASE_SETTINGS_FILE) --env-file=$(SECRET_SETTINGS_FILE) --name="$(APP_NAME)" $(APP_NAME)

debug:
	docker run -p=$(APP_PORT):$(APP_PORT) --env-file=$(BASE_SETTINGS_FILE) --env-file=$(SECRET_SETTINGS_FILE) --name="$(APP_NAME)" $(APP_NAME)
