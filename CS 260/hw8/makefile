# Sample makefile

PYTHON = /usr/bin/env python
VIEWER = less

floyd : graph.py floyd.py input
	$(PYTHON) floyd.py < input

view : graph.py floyd.py input
	$(VIEWER) floyd.py input

run : floyd view

