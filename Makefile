install:
	poetry install

migrate:
	poetry run python manage.py migrate

setup:
	cp -n .env.example .env || true
	make install
	make migrate

start:
	poetry run python manage.py runserver 0.0.0.0:8080

check:
	poetry check

lint:
	poetry run flake8 .

test:
	poetry run python manage.py test

test-coverage:
	poetry run coverage run manage.py test python_django_blog
	poetry run coverage html
	poetry run coverage report

deploy:
	git push main

requirements:
	poetry export -f requirements.txt --output requirements.txt

