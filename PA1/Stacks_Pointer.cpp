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
//declare function so it can be used be others

bool EMPTY(node *head);
int TOP(node *&head, node *&last);
void PUSH(node *&head, node *&last, int number);
void POP(node *&head, node *&last);
void MAKENULL(node *&head, node *&last);

bool EMPTY(node *head) //checks to see if linked list is NULL, or 0
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

void PUSH(node *&head, node *&last, int number) //pushes a new element to the top of the stack
{
	int numbertemp; 
	
	if(EMPTY(head))
	{
		node *temp = new node;
		temp->number = number;
		temp->next = NULL;
		head = temp;
		last = temp;
	}
	else
	{
		node *temp2 = new node;
		temp2->number = number;
		temp2->next = head;
	    head = temp2;
		
	}
	
}

int TOP(node *&head, node *&last)  //returns the head of the stack(linked list) if it exists
{
	if(EMPTY(head))
	{
		cout << "Stack is Empty" << endl;
	}
	else
	{
		cout << "Top of the Stack is: " << endl;
		cout << head->number <<endl;
	}
	
}

void POP(node *&head, node *&last) //removes the head of the stack (linked list)
{
    if(EMPTY(head))
	{
		cout << "Stack is Empty" << endl;
	}
	else if(head == last)
	{
		delete head;
		head == NULL;
		last == NULL;
	}
	else
	{
		node *temp = head;
		head = head->next;
		delete temp;
	}
	
}

void showList(node *current) //prints out the stack (linkedlist)
{
	if(EMPTY(current))
	{
		cout << "The stack is empty";
	}
	else
	{
		cout << "The stack contains:" << endl;
		while(current != NULL)
		{
			cout << current->number << endl;
			current = current->next;
		}
	}
}

void MAKENULLS(node *current) //makes the stack (linked list) null
{
	if(EMPTY(current))
	{
		cout << "The stack is empty";
	}
	else
	{
		while(current != NULL)
		{
			current->number = NULL;
			current = current->next;
		}
		
	}
	
}

int main(int nNumberofArgs, char* pszArgs[])
{
	//initialize head and last to NULL
	node* head = NULL;
	node* last = NULL;
	
	//initialize the stack by pushing values to it
	PUSH(head,last,77777);
	PUSH(head,last,21);
	PUSH(head,last,213);
	PUSH(head,last,4);
	PUSH(head,last,325);
	PUSH(head,last,46);
	PUSH(head,last,4);
	PUSH(head,last,44);
	PUSH(head,last,3);
	PUSH(head,last,6);

////Programming Assignment Operations

//Iterated Insertion (PUSH) of 2 values using my ADT implementation
 /*   PUSH(head,last,47);
    PUSH(head,last,50);
    showList(head); */
    
//Iterated Deletion (POP) of 5 ten values using my ADT implementation
  /*  POP(head,last);
    POP(head,last);
    POP(head,last);
    POP(head,last);
    POP(head,last);
	showList(head);*/

	
	
	
	
}
