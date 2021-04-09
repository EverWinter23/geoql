.PHONY: dev-server
dev_server:
	DB_NAME=geoql DB_PASS=geoqlDB DB_USER=postgis DB_HOST=localhost DB_PORT=5432 python manage.py runserver

.PHONY: migrate
migrate:
	DB_NAME=geoql DB_PASS=geoqlDB DB_USER=postgis DB_HOST=localhost DB_PORT=5432 python manage.py migrate

.PHONY: migrations
migrations:
	DB_NAME=geoql DB_PASS=geoqlDB DB_USER=postgis DB_HOST=localhost DB_PORT=5432 python manage.py makemigrations
