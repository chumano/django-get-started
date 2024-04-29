.ONESHELL: # Applies to every targets in the file!

# Phony target for clarity, doesn't create a file
.PHONY: run

run:
	cd ./mysite 
	python manage.py runserver