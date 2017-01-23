Matthew DiGiacomo, Dylan Jervis, Yashwanth Dahanayake
CS 260 PA3
March 16th, 2015

------------------
PROBLEM ASSIGNMENT
------------------
The problems were assigned as follows:

Matthew - 1,2 (3,4,7,8) -- All run correctly
Dylan - 5,9 --5 working somewhat, 9 not working
Yashwanth - 4,7,8 -- Did not submit

Yashwanth did not complete his problems on time because of confusion regarding the due date. 
Instead, I (Matthew) completed extra problems - 3,4,7 and 8 in order to make up for him.

----------
HOW TO RUN
----------
For problems 1 and 2, a report was included that details the results of the code for open 
and close hashing. This report is titled "Problems1and2_Report.pdf". Please refer to this 
when grading. Problems 1 and 2 is ran be executing the makefile, simply by typing "make" 
while the makefile, problem1.py and problem2.py are all located in the same directory. 
The two problems output the data that is also captured in the pdf document as stated above. 

For problems 3,4,7,8 - to run all you need to do is call make qX.py For instance 
to run problem 7, you would call "make q7". All code runs correctly without errors.

For problem 5, The function accepts a dictionary representation of an adjacency matrix for a directed graph.  It also 
accepts the starting node.  From there it goes through and iterates through the nodes connected to the 
starting node, and then the nodes connected to that and so on. 

The code has issues going through all of the nodes.  Somewhere within the logic for the algorithm there
is a flaw. I was not able to locate it and tried multiple ways with the current setup being the closest 
to correct. It outputs 2 dictionaries, the first one is the shortest paths, and the second one is the 
calculated distances for those paths. 


If there are any questions please contact Matthew DiGiacomo at med322@drexel.edu or 609-605-8816.

*Please note that problems 1 and 2 take a small amount of time to run and are not instant. 
*Please give it time to complete.