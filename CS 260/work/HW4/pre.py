#!/usr/bin/python

import problem1
import lexer

# This while loop gets in the expression and passes it to the build tree
# function, then the print function, then the eval funtion
while lexer.get_expression():
	tmp = problem1.preTree()
	problem1.printList(problem1.pre(tmp), "pre:")
	problem1.printList(problem1.inForm(tmp), "in:")
	problem1.printList(problem1.post(tmp), "post:")
	print "sol:", problem1.evalExpression(problem1.post(tmp))
	print ""
