# Matthew DiGiacomo, Dylan Jervis, Yashwanth Dahanayake
# for python binary!
PI=python

default: q1 q2 q3 q4 q5 q7 q8

report:
		pdflatex --output-directory=report/ report/report.tex

permissions:
		chmod u+x problem1.py
		chmod u+x problem2.py
		chmod u+x problem3.py
		chmod u+x problem4.py
		chmod u+x problem7.py
		chmod u+x problem8.py
		
q1: problem1.py alice30.txt
	@echo "======== Executing Q1 ========"
	@echo "    Open Hashing:"
	$(PI) problem1.py < alice30.txt
	@echo "======== End of Q1 ========"
	@echo

q2: problem2.py alice30.txt
	@echo "======== Executing Q2 ========"
	@echo "    Closed Hashing:"
	$(PI) problem2.py < alice30.txt
	@echo "========= End of Q2 ========="
	@echo

q3: problem3.py
	@echo "======== Executing Q3 ========"
	@echo "    Binary Search Trees:"
	$(PI) problem3.py
	@echo "======== End of Q3 ========"
	@echo

q4: problem4.py alice30.txt
	@echo "======== Executing Q4 ========"
	@echo "    Tries:"
	$(PI) problem4.py < alice30.txt
	@echo "======== End of Q4 ========"
	@echo

q5: problem5.py
	@echo "======== Executing Q5 ========"
	@echo "    Dijkstra:"
	$(PI) problem5.py
	@echo "======== End of Q5 ========"
	@echo	
	
q7: problem7.py
	@echo "======== Executing Q7 ========"
	@echo "    Floyd's Algorithm"
	$(PI) problem7.py
	@echo "======== End of Q7 ========"
	@echo

q8: problem8.py
	@echo "======== Executing Q8 ========"
	@echo "    Depth-first Search"
	$(PI) problem8.py
	@echo "======== End of Q8 ========"
	@echo
