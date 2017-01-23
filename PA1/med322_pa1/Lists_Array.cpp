//Matthew DiGiacomo
//CS 260 PA1
//February 8th, 2015

#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <list>
using namespace std; 

//declare as a global so it can be modified and tracked
int arraySize;

int MAKENULL(int myArray[]){ //this function sets each spot in the list(array) to NULL, or 0
	
	for(int i=0; i<arraySize; i++)
	{
		myArray[i]=0;
	}
	
}

int DELETE(int pos, int myArray[]){ //this function deletes a given position (and value) from the list
	
		if(pos > arraySize || pos<0) 
		{
			cout << "Out of bounds" << endl;
			return 0;
		}
	
		for(int i=pos; i<arraySize; i++)
		{
			myArray[i] = myArray[i+1];
		}
		arraySize--; //arraySize is decremented to account for the deleted value
	 
}

int INSERT(int x, int pos, int myArray[]){ //this function inserts a given value into the given position
	int arraySizeTest = arraySize -1;
	if(pos>arraySizeTest && pos <0){
		cout << "Out of bounds" << endl;
	}
	else if(pos >0)
	{
		for(int i=arraySize; i>pos;i--)
		{
			myArray[i] = myArray[i-1];
			
		}
		arraySize++; //arraySize is incremented to account for the new value
		myArray[pos] = x;
		
	}
	else if(pos == 0)
	{
		for(int j=arraySize; j>=0; j--)
		{
			myArray[j+1]=myArray[j];
		}
		myArray[0]=x;
		arraySize++;
	}
}

int PREVIOUS(int pos, int myArray[]){ //this function returns the previous position after the input (if it exists)
	int arraySizeTest = arraySize -1;
	if(pos == 0)
	{
		return pos;
	}
	else if(pos > arraySizeTest){
		
		cout << "Out of bounds" << endl;
	}
	else if(pos < arraySizeTest)
	{
		pos = pos-1;
		return pos;
	}
}

int NEXT(int pos, int myArray[]){ //this function returns the next position after the input (if it exists)
	int arraySizeTest = arraySize -1;
	if(pos == arraySizeTest)
	{
		return pos;
	}
	else if(pos > arraySizeTest){
		cout << "Out of bounds" << endl;
	}
	else if(pos < arraySizeTest)
	{
		pos = pos+1;
		return pos;
	}
}

int LOCATE(int x, int myArray[]){ //this function locates the position of a given value
	
		for(int i = 0; i<arraySize;)
		{
			if(myArray[i]==x)
			{
				return i;
			}
			else
			{
				i++;
			}
		}
		cout << "Element doesn't exist";

}


int RETRIEVE(int loc, int myArray[]){ //this function retrieves the value at the input location 
	
		for(int i = 0; i<arraySize;)
		{
			if(myArray[i]==myArray[loc])
			{
				return myArray[i];
			}
			else
			{
				i++;
			}
		}
		cout << "Element doesn't exist";

}

int FIRST(int myArray[]){ //this function returns the first element in the list(array)
	if(arraySize<=0){
		return 0;
	}
	else
	{
	return myArray[0];
	}
}

int END(int myArray[]){ //this function returns the last element in the list (array)
	int lastelement = myArray[arraySize-1];
	return lastelement;
}

void PRINTARRAY(int myArray[]) //this function prints out the values in the list (array)
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

//Set the size of the List, automatically modified later when inserting or deleting elements
	arraySize = 10;
	//List initiliazation with 10 values
    int myArray[10] = {77777,1,213,477,325,46,4,44,3,6};
    
//Iterated Insertion (front) of 10 values (using my array ADT implementations)
/*	INSERT(1000,0,myArray);
	INSERT(2,0,myArray);
	INSERT(34,0,myArray);
	INSERT(333,0,myArray);
	INSERT(7,0,myArray);
	INSERT(45,0,myArray);
	INSERT(578,0,myArray);
	INSERT(45,0,myArray);
	INSERT(8,0,myArray);
	INSERT(11,0,myArray);
	cout << arraySize;
	PRINTARRAY(myArray);*/
	
//Iterated Insertion (back) of 10 values (using my array ADT implementations)
/*	INSERT(1000,arraySize,myArray);
	INSERT(2,arraySize,myArray);
	INSERT(34,arraySize,myArray);
	INSERT(333,arraySize,myArray);
	INSERT(7,arraySize,myArray);
	INSERT(45,arraySize,myArray);
	INSERT(578,arraySize,myArray);
    INSERT(45,arraySize,myArray);
	INSERT(8,arraySize,myArray);
	INSERT(11,arraySize,myArray);
	PRINTARRAY(myArray);*/
	
//Traversal (print the list)
//	PRINTARRAY(myArray);

//Iterated Deletion (front) of 5 values (using my array ADT implementations)
/*	DELETE(0,myArray);
	DELETE(0,myArray);
	DELETE(0,myArray);
	DELETE(0,myArray);
	DELETE(0,myArray);
	PRINTARRAY(myArray);*/
	
//Iterated Deletion (back) of 5 values (using my array ADT implementations)
/*	DELETE(arraySize,myArray);
	DELETE(arraySize,myArray);
	DELETE(arraySize,myArray);
	DELETE(arraySize,myArray);
	DELETE(arraySize,myArray);
	PRINTARRAY(myArray);*/
	
///Operations using libraries on lists
//list<int> L;
//initalize list
/*L.push_back(77777);
L.push_back(1);
L.push_back(213);
L.push_back(477);
L.push_back(325);
L.push_back(46);
L.push_back(4);
L.push_back(44);
L.push_back(3);
L.push_back(6);

list<int>::iterator i;*/

//Iterated insertion (front) of 10 values
/*	L.push_front(1000);
	L.push_front(2);
	L.push_front(34);
	L.push_front(333);
	L.push_front(7);
	L.push_front(45);
	L.push_front(578);
	L.push_front(45);
	L.push_front(8);
	L.push_front(11);
for(i=L.begin(); i != L.end(); ++i)
{
 	cout << *i << " ";
   cout << endl;
}*/

//Iterated insertion (back) of 10 values
/*    L.push_back(1000);
	L.push_back(2);
	L.push_back(34);
	L.push_back(333);
	L.push_back(7);
	L.push_back(45);
	L.push_back(578);
	L.push_back(45);
	L.push_back(8);
	L.push_back(11);
for(i=L.begin(); i != L.end(); ++i)
{
 	cout << *i << " ";
   cout << endl;
}*/

//Traversal
/*for(i=L.begin(); i != L.end(); ++i)
{
 	cout << *i << " ";
   cout << endl;
}*/

//Iterated deletion (front) of 5 values
/*	L.pop_front();
	L.pop_front();
	L.pop_front();
	L.pop_front();
	L.pop_front();
for(i=L.begin(); i != L.end(); ++i)
{
 	cout << *i << " ";
   cout << endl;
}*/

//Iterated deletion (back) of 5 values
/*  L.pop_back();
	L.pop_back();
	L.pop_back();
	L.pop_back();
	L.pop_back();
for(i=L.begin(); i != L.end(); ++i)
{
 	cout << *i << " ";
   cout << endl;
}*/

}


