lint:
	black .

migrations:
	python manage.py makemigrations
	python manage.py migrate

shell:
	python manage.py shell_plus

tests:
	pytest -vv

tests-coverage:
	coverage run manage.py test -v 2 --keepdb
	coverage report -m
	coverage html
