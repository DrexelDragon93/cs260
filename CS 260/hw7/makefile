# Sample makefile

PYTHON = /usr/bin/env python
VIEWER = less

testset : set.py test-set.py
	$(PYTHON) test-set.py

view : set.py
	$(VIEWER) set.py

run : testset view

