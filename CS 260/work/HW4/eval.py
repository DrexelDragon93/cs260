#!/usr/bin/python

import problem1
import lexer


while lexer.get_expression():
	print "sol:", problem1.evalExpression(problem1.post(problem1.postTree()))
print ""
