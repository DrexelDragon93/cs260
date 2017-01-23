//Matthew DiGiacomo
//CS 260 PA1
//February 8th, 2015

#include <cstdio>
#include <cstdlib>
#include <iostream>
using namespace std; 

struct node { //the constructor for our node pointers
	int number;
	node* next;
};

//declare head and last as globals so we can use them in other functions
node* head; 
node* last;

//function declarations so they can be used within others 
bool isEmpty(node *head);
char menu();
void insertAsFirstElement(node *&head, node *&last, int number);
void INSERTP(node *&head, node *&last, int number);
void DELETEP(node *&head, node *&last);
int LOCATE(node *current, int x);

bool isEmpty(node *head) //checks to see if the head is NULL
{
	if(head==NULL)
	{
		return true;
	}
	else
	{
		return false;
	}
}

void insertAsFirstElement(node *&head, node *&last, int number) //insert as first element function if the head is NULL
{
	node *temp = new node;
	temp->number = number;
	temp->next = NULL;
	head = temp;
	last = temp;
}

void INSERTP(node *&head, node *&last, int number) //this function is used to create the linked list sequentially
{
	if(isEmpty(head))
	{
		insertAsFirstElement(head,last,number);
	}
	else
	{
	    node *temp = new node;
	    temp->number = number;
	    temp->next = NULL;
		last->next = temp;
		last = temp;
	}
}

void showList(node *current) //this function is used to print out the list 
{
	if(isEmpty(current))
	{
		cout << "The list is empty";
	}
	else
	{
		cout << "The list contains:" << endl;
		while(current != NULL)
		{
			cout << current->number << endl;
			current = current->next;
		}
	}
}

int FIRST(node *current) //returns the position of the first element of the linked list
{
	if(isEmpty(current))
	{
		cout << "The list is empty";
	}
	else
	{
	int number = current->number;
		return LOCATE(current, number)+1;
	}
}

int END(node *current)  //returns the position of the last element of the linked list
{
	int number;
	if(isEmpty(current))
	{
		cout << "The list is empty";
	}
	else
	{
		while(current != NULL)
		{
			number = current->number;
			current = current->next;
		}
		return LOCATE(head,number)+2;
	}
}

int RETRIEVE(node *current, int pos) //retrieves the value at the input position on the list
{
	if(isEmpty(current))
	{
		cout << "The list is empty";
	}
	else
	{
	 for(int i=0; i<pos; i++)
	 {
	 	current = current->next;
	 }	
	 cout << "Element Retreived: " << endl;
	 cout << current->number << endl;
	 return current->number;
	}
}

int LOCATE(node *current, int x) //returns the position of the given value on the list
{
	int pos=0;
	if(isEmpty(current))
	{
		cout << "The list is empty";
	}
	else
	{
		while(current != NULL)
		{
			if(current->number==x)
			{
				return pos;
			}
			else
			{
				current = current->next;
				pos=pos+1;
			}
		}
	}
}

int NEXT(node *current, int pos) //returns the position of the next position after the input on the list
{
	if(isEmpty(current))
	{
		cout << "The list is empty";
	}
	else
	{
		cout << "The next position is: " <<endl;
		cout << pos+1 << endl;
	}
}

int PREVIOUS(node *current, int pos) //returns the position of the prev position after the input on the list
{
	if(isEmpty(current))
	{
		cout << "The list is empty";
	}
	else
	{
		cout << "The previous position is: " <<endl;
		cout << pos-1 << endl;
	}		
}

void DELETE(node *current, int pos) //deletes the node at the given position from the linked list
{
	node *temp = current;
	if(pos==1)
	{
		current->number = current->next->number;
		temp = current->next;
		current->next=current->next->next;
		free(temp);
		return;
	}
	int i;
	for(i=0; i<pos-2;i++)
	{
		temp = temp->next;
	}
	node *temp2 = temp->next;
	temp->next = temp2->next;
	free(temp2);
	
	
}

void INSERT(node *current, node* last, int pos, int num) //inserts a new node at the given position to the linked list
{
	node *temp = new node();
	temp->number=num;
	temp->next=NULL;
	
	if(pos==1)
	{
		node *temp3 = new node;
		temp3->number = num;
		temp3->next = head;
	    head = temp3;
	    return;
	}
	
	node* temp2 = current;
	for(int i=0; i<pos-2;i++)
	{
		temp2 = temp2->next;
	}
	temp->next = temp2->next;
	temp2->next=temp;
	
	
	
}

int main(int nNumberofArgs, char* pszArgs[])
{
	head=NULL;
	last=NULL;
	
	//List initiliazation with 10 values
	INSERTP(head,last,77777);
	INSERTP(head,last,1);
	INSERTP(head,last,213);
	INSERTP(head,last,477);
	INSERTP(head,last,325);
	INSERTP(head,last,46);
	INSERTP(head,last,4);
	INSERTP(head,last,44);
	INSERTP(head,last,3);
	INSERTP(head,last,6);
	

////Programming Assignment Operations

//Iteration Insertion (front) of 10 values (using my pointer ADT implementations)
/*	INSERT(head,last,FIRST(head),1000); 
	INSERT(head,last,FIRST(head),2); 
	INSERT(head,last,FIRST(head),34); 
	INSERT(head,last,FIRST(head),333); 
	INSERT(head,last,FIRST(head),7); 
	INSERT(head,last,FIRST(head),45); 
	INSERT(head,last,FIRST(head),578); 
	INSERT(head,last,FIRST(head),45); 
	INSERT(head,last,FIRST(head),8); 
	INSERT(head,last,FIRST(head),11); 
	showList(head);*/
	
//Iteration Insertion (back) of 10 values (using my pointer ADT implementations)
/*	INSERT(head,last,END(head),1000); 
	INSERT(head,last,END(head),2); 
	INSERT(head,last,END(head),34); 
	INSERT(head,last,END(head),333); 
	INSERT(head,last,END(head),7); 
	INSERT(head,last,END(head),45); 
	INSERT(head,last,END(head),578); 
	INSERT(head,last,END(head),45); 
	INSERT(head,last,END(head),8); 
	INSERT(head,last,END(head),11); 
	showList(head);*/
	
//Traversal (print the list)
//showList(head);

//Iteration Deletion (Front) of 5 values (using my pointer ADT implementations)
/*DELETE(head,FIRST(head)); 
DELETE(head,FIRST(head)); 
DELETE(head,FIRST(head));
DELETE(head,FIRST(head)); 
DELETE(head,FIRST(head)); 
showList(head);*/

//Iteration Deletion (Back) of 5 values (using my pointer ADT implementations)
/*DELETE(head,END(head)-1); 
DELETE(head,END(head)-1); 
DELETE(head,END(head)-1);
DELETE(head,END(head)-1); 
DELETE(head,END(head)-1); 
showList(head);*/

	
}


	
	
	
