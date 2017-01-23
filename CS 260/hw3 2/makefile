# Timothy Cheeseman
# CS 260 Assignment 2
# Sample Solution

PYTHON = /usr/bin/env python
VIEWER = less

all: run

problem1 : fibonacci.py problem1.py
	for i in `seq 1 10`; do $(PYTHON) problem1.py $$i; done

problem2 : fibonacci.py problem2.py
	$(PYTHON) problem2.py

problem3 : fibonacci.py problem3-1.py problem3-2.py
	$(PYTHON) problem3-1.py
	$(PYTHON) problem3-2.py

view : fibonacci.py problem1.py problem2.py problem3-1.py problem3-2.py
	$(VIEWER) fibonacci.py
	$(VIEWER) problem1.py
	$(VIEWER) problem2.py
	$(VIEWER) problem3-1.py
	$(VIEWER) problem3-2.py

run : problem1 problem2 problem3 view

