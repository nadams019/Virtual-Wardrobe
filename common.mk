LINTER = flake8
PYTESTFLAGS = -vv --verbose --tbshort --cov=$(PKG) --cov-report term-missing

FORCE:


tests: lint unit

unit: FORCE
        $(LINTER) *.py

# test a python file:
%.py: FORCE
        pytest -s tests/test_$*.py

docs: FORCE
        pydoc3 -w ./*py
        git add *html
