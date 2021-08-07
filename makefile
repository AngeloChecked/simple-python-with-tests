

test:
ifdef TESTFILE 
	@python -m unittest $(TESTFILE)
else
	@python -m unittest discover 
endif
