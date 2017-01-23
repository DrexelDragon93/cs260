# Sample makefile

PYTHON = /usr/bin/env python
VIEWER = less

pre : lexer.py tree.py pre.py
	$(PYTHON) pre.py < pre.input

in : lexer.py tree.py in.py
	$(PYTHON) in.py < in.input

post : lexer.py tree.py post.py
	$(PYTHON) post.py < post.input

view : lexer.py tree.py post.py
	$(VIEWER) tree.py
	$(VIEWER) pre.py
	$(VIEWER) pre.input
	$(VIEWER) in.py
	$(VIEWER) in.input
	$(VIEWER) post.py
	$(VIEWER) post.input

run : pre in post view

