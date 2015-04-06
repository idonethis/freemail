.PHONY : test

default: test

test:
	PYTHONPATH=. python test/runtests.py
