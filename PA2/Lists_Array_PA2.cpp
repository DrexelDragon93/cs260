//Matthew DiGiacomo
//CS 260 PA2
//February 21st, 2015

#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <list>
using namespace std; 

//declare as a global so it can be modified and tracked

int arrayinit = 100;

int MAKENULL(int myArray[]){ //this function sets each spot in the list(array) to NULL, or 0
	
	int arraySize = sizeof(myArray)/4;
	
	for(int i=0; i<arraySize; i++)
	{
		myArray[i]=0;
	}
	
}

int DELETE(int pos, int myArray[]){ //this function deletes a given position (and value) from the list
	int arraySize = sizeof(myArray)/4;
	
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
	int arraySize = sizeof(myArray)/4;
	
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
	int arraySize = sizeof(myArray)/4;
	
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
	int arraySize = sizeof(myArray)/4;
	
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
	
	int arraySize = sizeof(myArray)/4;
	
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
	int arraySize = sizeof(myArray)/4;
	
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
int arraySize = sizeof(myArray)/4;

	if(arraySize<=0){
		return 0;
	}
	else
	{
	return myArray[0];
	}
}

int END(int myArray[]){ //this function returns the last element in the list (array)
	int arraySize = sizeof(myArray)/4;
	
	int lastelement = myArray[arraySize-1];
	return lastelement;
}

void PRINTARRAY(int myArray[]) //this function prints out the values in the list (array)
{
	int arraySize = sizeof(myArray);
	cout <<arraySize;
	cout<<endl;
	for(int i = 0; i<arraySize; i++)
	{
		cout << myArray[i] << endl;
	}
}

void CONCATLISTS(int myArray[][100], int xd, int yd) //function to concat a list of lists
{
	int p=0;
	int newd = xd*yd;
	int newArray[xd*yd];

	
	for(int i =0; i<xd; i++)
	{
		for(int j=0; j<yd; j++)
		{
			newArray[p] = myArray[i][j];
			p++;
		}
		
	}
	
	for(int z = 0; z<newd; z++)
	{
		cout << newArray[z] << endl;
	}
	
}

int MERGELISTS(int m, int n, int A[], int B[], int C[])
{
      int i, j, k;
      i = 0;
      j = 0;
      k = 0;
      while(i<m &&j<n){
      	if(A[i] <= B[j]){
      		C[k] = A[i];
      		i++;
		  }
		else{
		  	C[k] = B[j];
		  	j++;
		  }
		  k++;
	  }
	  if(i<m){
	  	for(int p = i; p<m; p++){
	  		C[k] = A[p];
	  		k++;
		  }
	  }
	  else{
	  	for(int p =j; p<n; p++){
	  		C[k] = B[p];
	  		k++;
		  }
	  }
	for(int z = 0; z<k; z++)
	{
		cout << C[z] << endl;
	}
  cout<< endl;
}

int main(int nNumberofArgs, char* pszArgs[])
{
	
    
    
////Programming Assignment Operations

///Problem 2.3, Merge N Sorted Lists
//To run on N lists, assign the output of the call to 
//MERGELISTS to an Array and continue calling MERGELISTS on any new arrays
	int m = 10; //define array1 size
	int n = 10; //define array2 size
    int myArray0[10] = {1,3,5,7,9,11,13,15,17,19}; //init array1, sorted
    int myArray1[10] = {0,2,4,6,8,10,12,14,16,18}; //init array2, sorted
    int newArray[20] = {}; //create empty array of double size
    MERGELISTS(m, n, myArray0, myArray1, newArray); //call the function to merge them into newArray and prints it

///Problem 2.4, Concatenate a List of Lists 
	int xd = 3;    //specifies x dimension
	int yd = 4;    //specifies y dimension
    int arr[3][100] ={{1,3,5,7},{2,4,6,8},{0,9,10,11}}; //creates a list of list
    CONCATLISTS(arr,xd,yd); //calls the function on our list of lists and prints it
    
    
    

    
 
  
  

}


