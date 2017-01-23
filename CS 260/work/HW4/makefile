PYTHON = /usr/bin/env python
VIEWER = less

pre : lexer.py pre.py problem1.py
	$(PYTHON) pre.py < pre.input

in : lexer.py in.py problem1.py
	$(PYTHON) in.py < in.input

post : lexer.py post.py problem1.py
	$(PYTHON) post.py < post.input

eval : lexer.py eval.py problem1.py
	$(PYTHON) eval.py < post.input
	

view : lexer.py post.py
	$(VIEWER) pre.py
	$(VIEWER) in.py
	$(VIEWER) post.py
	$(VIEWER) eval.py
	
clean : 
	rm *.pyc


run : pre in post eval view clean
