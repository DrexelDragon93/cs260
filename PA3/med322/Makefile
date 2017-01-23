# for python binary!
PI=python

default: q1 q2

report:
		pdflatex --output-directory=report/ report/report.tex

permissions:
		chmod u+x problem1.py
		chmod u+x problem2.py
		
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

#Matthew DiGiacomo, Dylan Jervis, Yashwanth Dahanayake