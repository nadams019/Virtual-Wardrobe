LINTER = flake8
PYTESTFLAGS = -vv --verbose --tb=short


FORCE:

tests: lint unit

unit: FORCE
	pytest $(PYTESTFLAGS)

lint: FORCE
	$(LINTER) *.py

# test a python file:
%.py: FORCE
	pytest -s tests/test_$*.py

docs: FORCE
	pydoc3 -w ./*py
