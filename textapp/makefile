export RUN_ENV = test
REPO = text_menu
PYLINTER = flake8

FORCE:

prod: tests
	-git commit -a
	git push origin main

tests: lint pytests

lint: FORCE
	flake8 *.py

pytests: FORCE
	# want to get an option for --nocapture here!
	nosetests --exe --verbose --with-coverage --cover-package=.