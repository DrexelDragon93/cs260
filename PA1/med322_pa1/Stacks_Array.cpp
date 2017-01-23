//Matthew DiGiacomo
//CS 260 PA1
//February 8th, 2015

#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <stack>
using namespace std; 

//declare as a global so it can be modified and tracked
int arraySize;

//declare function so it can be used be others
bool EMPTY(int myArray[]);


bool EMPTY(int myArray[]) //checks to see if array is NULL, or 0
{
	for(int i=0; i<arraySize;i++)
	{
		if(myArray[i]==0)
		{
			
		}
		else
		{
			return false;
		}
	}
	return true;
	
}

int TOP(int myArray[]) //returns the top of the stack if it exists
{
	if(EMPTY(myArray))
	{
		cout << "Stack is empty";
	}
	else
	{
	cout << "Top of Stack is: " <<endl;
	return myArray[0];
	}
}

int POP(int myArray[]) //removes the top element of the stack
{
	if(EMPTY(myArray))
	{
		cout << "Stack is empty";
	}
	else
	{
		for(int i=0; i<arraySize; i++)
		{
			myArray[i] = myArray[i+1];
		}
		arraySize--; //arraySize is decremented to account for the deleted value
	}
	
}

int PUSH(int x, int myArray[]) //pushes a new element to the top of the stack
{
	if(EMPTY(myArray))
	{
		myArray[0]=x;
	}
	else
	{
		for(int i=arraySize; i>0;i--)
		{
			myArray[i] = myArray[i-1];
			
		}
	arraySize++;
	 myArray[0] = x;
	}
	
}

int MAKENULL(int myArray[]) //makes the stack (array) null
{
	for(int i=0; i<arraySize; i++)
	{
		myArray[i]=0;
	}
}

void PRINTARRAY(int myArray[]) //prints out the stack (array)
{
	cout<<endl;
	for(int i = 0; i<arraySize; i++)
	{
		cout << myArray[i] << endl;
	}
}

int main(int nNumberofArgs, char* pszArgs[])
{
////Programming Assignment Operations
//Set the size of the stack, automatically modified later when inserting or deleting elements
	arraySize = 10;
    //Stack initiliazation with 10 values
   int myStack[10] = {77777,1,213,4,325,46,4,44,3,6};

//Iterated Insertion (PUSH) of 2 values using my ADT implementation
   /* PUSH(47, myStack);
    PUSH(50, myStack);
    //PRINTARRAY(myStack);*/
    
//Iterated Deletion (POP) of 5 ten values using my ADT implementation
/*    POP(myStack);
	POP(myStack);
	POP(myStack);
	POP(myStack);
	POP(myStack);
//	PRINTARRAY(myStack);*/

//Iterated Insertion and Deletion (PUSH/POP) of 2 values using the libraries
/*	stack<int> myStackInt;
	myStackInt.push(47);
	myStackInt.push(50);
	myStackInt.pop();
	myStackInt.pop();*/
	
	
}


