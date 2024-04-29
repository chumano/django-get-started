PRJECT_DIR = ./mysite

.ONESHELL: # Applies to every targets in the file!

# Phony target for clarity, doesn't create a file
.PHONY: run

gomysite:
	cd $(PRJECT_DIR)

run:
	cd $(PRJECT_DIR)
	python manage.py runserver

collectstatic:
	cd $(PRJECT_DIR)
	python manage.py collectstatic