.PHONY : view problem1 problem2 run

run : problem1 problem2 problem3 view
		python problem3.py

problem1 : 
		python problem1.py

problem2 :
		python problem2.py

problem3 : problem1 problem2
		python problem3.py
		
view : 
		less problem1.py
		less problem2.py

clean : 
		rm *.pyc
