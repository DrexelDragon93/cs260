#/usr/bin/python

import problem1
import lexer

# This whild loop builds a tree then passes to the print fucntion and eval
# function
while lexer.get_expression():
	tmp = problem1.postTree()
	problem1.printList(problem1.pre(tmp), "pre:")
	problem1.printList(problem1.inForm(tmp), "in:")
	problem1.printList(problem1.post(tmp), "post:")
	print "sol:", problem1.evalExpression(problem1.post(tmp))
	print ""
