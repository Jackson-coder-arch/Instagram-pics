serve :
	python manage.py runserver

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

admin:
	python manage.py createsuperuser

test: 
	coverage run manage.py test && coverage html
