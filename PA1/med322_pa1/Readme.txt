Matthew DiGiacomo
CS 260 PA1
February 8th, 2015

This assignment submission contains four executables and for .cpp files for modifying the program to see different results:
	-Lists_Array.cpp
	-Lists_Pointer.cpp
	-Stacks_Array.cpp
	-Stacks_Pointer.cpp

For testing the lists implemenation open up either Lists_Array.cpp or Lists_Pointer.cpp and scroll down to the main class. All the code for the testing of the five given operations on lists - iterated insertion (in front, at the back), traversal, iterated deletion (in front, at the back) - is all included and commented out. The only code this is not commented out is for the initialization of an array (list implemenation) and a linked list (pointer implementation). To test one, just un-comment the section, compile and run the program. Everything works correctly with the exception of special cases for doing iterated insertion on Lists* in Lists_Array.cpp.

For testin the stacks implementation, open up either Stacks_Array.cpp or Stacks_Pointer.cpp and scorll down to the main class. All the code for the testing of the five given operations on lists - iterated insertion (PUSH operation), iterated deletion (POP operation) - is all included and commented out. The only code not commented out is for initialization of a stack. To test an operation, just un-comment the section, compile and run the program. Everything works correctly here.

Code for testing the C++ libraries for stacks and lists are also included. For testing lists, go into the Lists_Array.cpp file and find the code with the comment header "Operations using libraries on lists". Un comment what you want to test and compile and run. Similary, for testing stacks go into the 
Stacks_Array.cpp file and find the code with the comment header "Iterated Insertion and Deletion (PUSH/POP) of 2 values using the libraries". Uncomment what you want to test and compile and run. All of this code works as intended.


If there are any questions, please contact Matthew DiGiacomo at med322@drexel.edu or 6096058816.


*Only thing not working correctly is for iterated insertion on my Array ADT implementation. 
It inserts and prints out the array correctly, but the program crashes (when you start inserting more than 3 values) and I cannot figure out the cause. But it does insert the values into the array at the front and back.