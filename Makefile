run:
	@python django_workdays/manage.py runserver

setup:
	@pip install -U -e .\[tests\]

db:
	@python django_workdays/manage.py syncdb

automigrate:
	@python django_workdays/manage.py makemigrations
	@python django_workdays/manage.py migrate
