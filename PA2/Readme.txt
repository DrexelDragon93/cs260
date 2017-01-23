Matthew DiGiacomo
CS 260 PA2
February 22nd, 2015

This assignment submission contains 7 executables and 7 .cpp files for modifying the program to see different results:

	-Lists_Array_PA2.cpp
	-Queue_Pointer.cpp
	-Problem310_PA2.cpp
	-Problem34_Huffman_PA2.cpp
	-Problem313_PA2.cpp
	-Problem314_PreOrder_PA2.cpp
	-Problem314_PostOrder_PA2.cpp

I chose to do Problems 1,4,5,6,7,8, and 9 for a total of 10+10+10+20+15+15+30=110points. No timing measurements were done, so no PDF file is needed.

For problem 1, the file "Queue_Pointer" contains the solution. The main function contains calls to test each of the five implemented functions - enqueue, dequeue, front, makenull and empty (empty is tested within other portions of the code).

For problem 4 and 5, the solution is contained in the file "Lists_Array_PA2". Problem 4 was merging N sorted lists and is tested in the main function. The function called MERGELISTS accomplishes the solution. In order to run on N lists, assign the output of the call to MERGELISTS and continue calling MERGELISTS on any new arrays you would like. Problem 5 was to concatenate a list of lists and is testing again in the main function. The function called CONCATLISTS accomplishes the solution. A test list of lists is created in the main function and has CONCATLISTS called on it. The output is printed to the screen.

For problem 6, the solution is contained in the File "Problem310_PA2". This problem was to print the tree in level order. This problem uses several ADT functions like DEQUEUE and ENQUEUE. The tree is intialized through pointers. The root is created and then you call node->left or node->right to create new children nodes. You can continue this to create as big of a tree as you'd like. An example of this is created in the main function and the level order is printed to the screen.

For problem 7, the solution is contained in the file "Problem313_PA2". I have initialized a tree as shown in the comments above the main function. There are three helper functions in this file, PREtoPOST, POSTtoPRE and PREtoIN. The tree is created with the 5 nodes in the main function and each is assigned a value and whether it is a leaf or an internal node. Preorder and Postorder arrays are created with the correct traversals of the tree. These can then be passed to the three functions to get the conversiosn. The code is set up to test the PREtoPOST, POSTtoPRE and PREtoIN functions on the given tree.

For problem 8, the solution was split into two files - "Problem314_PreOrder_PA2" and "Problem314_PostOrder_PA2". For the preorder solution, input the string of characters you wish to test the solution on in the main function on the "expression []" variable, line 53. The code then computes the expression and prints it to the screen. For the postorder solution, the code waits for the user to input the postorder expression from the command line ie - "82*"- (no quotes) and then computes it and prints to the screen, in this case the result would be 16.

For problem 9, the solution is contained in the file "Problem34_Huffman_PA2". The program takes input from the command line from the user. It first asks how many items you would like to encode with huffman algorithm. After it takes this input, it then asks for the input characters and their respecitive frequencies. Press enter after entering each pair, ie enter "a .07" press enter, then enter "b .09" then enter, etc... Once you have entered all items, it will print out the character and its corresponding code.

If there are any questions, please contact Matthew DiGiacomo at med322@drexel.edu or 6096058816.
