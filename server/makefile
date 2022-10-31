DOCFILES = $(shell ls db.py | sed 's/.py/.html/')

docs: $(DOCFILES)

%.html: %.py
	pydoc3 -w ./$<
	git add $@
