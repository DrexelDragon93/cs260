# Timothy Cheeseman
# CS 260 Assignment 2
# Sample Solution

PYTHON = /usr/bin/env python
VIEWER = less

all: run

problem1 : cell.py listconcat.py problem1.py
	$(PYTHON) problem1.py

problem2 : cell.py listconcat.py problem2.py
	$(PYTHON) problem2.py

problem3 : cell.py listconcat.py problem3.py
	$(PYTHON) problem3.py > mydata.txt
	gnuplot < plot-instructions

view : listconcat.py problem1.py problem2.py problem3.py
	$(VIEWER) listconcat.py
	$(VIEWER) problem1.py
	$(VIEWER) problem2.py
	$(VIEWER) problem3.py

run : problem1 problem2 problem3 view

