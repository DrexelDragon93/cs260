//Matthew DiGiacomo
//CS 260 PA2
//February 21st, 2015

#include <cstdio>
#include <cstdlib>
#include <iostream>
using namespace std; 

int treesize = 5;


struct node
{
	char const* id;
    int node;
};


void PREtoPOST(node* myArray[], node* outputArray[])
{
	outputArray[treesize-1] = myArray[0]; //last value of postorder is 1st value of preorder
	int i = 1;
	int count = 0;
	node* temp;
	
	while(myArray[i]->id != "i"){
		outputArray[i-1] = myArray[i];
		i++;
		count++;
	}
	
	temp = myArray[i];
	i++; //i=3
	count++;
	outputArray[i-count] = myArray[i];
	i++;
	
	while(i<treesize){
		if(myArray[i]->id != "i"){
		outputArray[i-count] = myArray[i];
		i++;
		}
		else{
			break;
		}
	}
	outputArray[i-count] = temp;
	
	

	
	cout<< outputArray[0]->node <<endl;
	cout<< outputArray[1]->node <<endl;
	cout<< outputArray[2]->node <<endl;
	cout<< outputArray[3]->node <<endl;
	cout<< outputArray[4]->node <<endl;

	
}

void POSTtoPRE(node* myArray[], node* outputArray[])
{
	outputArray[0] = myArray[treesize-1];
	int i, j;
	i = 0;
	j = 1;
	//handle left tree
	outputArray[j] = myArray[0]; 
	if(outputArray[j]->id =="l"){
		while(myArray[i]->id != "i"){
			i++;
		}
		j++;
		
		outputArray[j] = myArray[i];
		i = 1;
	}
	//handle right tree
	j++;
	while(i<treesize){
		if(myArray[i]->id =="l")
		{
			outputArray[j] = myArray[i];
			j++;
		}
		i++;
	}
	
	cout<< outputArray[0]->node <<endl;
	cout<< outputArray[1]->node <<endl;
	cout<< outputArray[2]->node <<endl;
	cout<< outputArray[3]->node <<endl;
	cout<< outputArray[4]->node <<endl;
}

void PREtoIN(node* myArray[], node* outputArray[])
{
	int i = 1;
	int j = 0;
	//handle left tree
	while(myArray[i]->id != "i")
	{
		outputArray[j] = myArray[i];
		i++;
		j++;
	}
	outputArray[j] = myArray[0]; // assign root node in middle of two trees
	j++;
	i++;
	
	//handle right tree;
	outputArray[j] = myArray[i];
	j++;
	
	while(myArray[i]->id !="i"){
		i--;
	}
	outputArray[j] = myArray[i];
	i++; //i=3
	j++;
	
	while(i <treesize)
	{
		if(myArray[i]->id != "i"){
		outputArray[j] = myArray[i];
		i++;
		}
		else
		{
		 break;
		}
	}

	cout<< outputArray[0]->node <<endl;
	cout<< outputArray[1]->node <<endl;
	cout<< outputArray[2]->node <<endl;
	cout<< outputArray[3]->node <<endl;
	cout<< outputArray[4]->node <<endl;
}

/* All operations done on the tree shown below

			n1
		n2	     n3
			  n4	n5	

preorder - n1,n2,n3,n4,n5
postoder - n2,n4,n5,n3,n1
inorder -  n2,n1,n4,n3,n5
*/

int main(int nNumberofArgs, char* pszArgs[])
{
	//create the nodes shown above
	node *n1 = new node;
		n1->id="i";
		n1->node=1;
	node *n2 = new node;
		n2->id="l";
		n2->node=2;
	node *n3 = new node;
		n3->id="i";
		n3->node=3;
	node *n4 = new node;
		n4->id="l";
		n4->node=4;
	node *n5 = new node;
		n5->id="l";
		n5->node=5;
	
	node* outputArray[5];	//output array
	node* PreArray[5] = {n1,n2,n3,n4,n5}; //pre order
	node* PostArray[5] = {n2,n4,n5,n3,n1}; //post order
	
	//Call the various functions on the arrays
	PREtoPOST(PreArray,outputArray);
	cout<<endl;
	POSTtoPRE(PostArray,outputArray);
	cout<<endl;
	PREtoIN(PreArray,outputArray);
	
	
	
	
}
