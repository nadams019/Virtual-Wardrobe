
API_DIR = server
DB_DIR = db
REQ_DIR = .
PYTESTFLAGS = -vv --verbose --tb=short

FORCE:

prod: all_tests github

github: FORCE
	- git commit -a
	git push origin master


unit: FORCE
	cd $(API_DIR); pytest $(PYTESTFLAGS)


dev_env: FORCE
	pip install -r $(REQ_DIR)/requirements-dev.txt

docs: FORCE
	cd $(API_DIR); make docs
