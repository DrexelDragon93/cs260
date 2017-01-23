//Matthew DiGiacomo
//CS 260 PA2
//February 21st, 2015

#include <cstdio>
#include <cstdlib>
#include <iostream>
using namespace std; 

struct node { //the constructor for our node pointers
	int number;
	node* next;
};


bool EMPTY(node *head);
void MAKENULL(node *&head, node *&last);


void MAKENULL(node *current)
{
	if(EMPTY(current))
	{
		cout << "The Queue is empty";
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

void FRONT(node *head)
{
	if(EMPTY(head))
	{
		cout << "Queue is Empty" << endl;
	}
	else
	{
		cout << "Front of the Queue is: " << endl;
		cout << head->number <<endl;
	}
	
	
}

void ENQUEUE(node *&head, node *&last, int number)
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
	    temp2->next = NULL;
		last->next = temp2;
		last = temp2;
	}
	
}

node* DEQUEUE(node *head, node *last)
{
	if(EMPTY(head))
	{
		cout << "Queue is Empty" << endl;
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
		return head;
	}
	
	
}

bool EMPTY(node *head)
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

void showList(node *current) 
{
	if(EMPTY(current))
	{
		cout << "The queue is empty";
	}
	else
	{
		cout << "The queue contains:" << endl;
		while(current != NULL)
		{
			cout << current->number << endl;
			current = current->next;
		}
	}
}

int main(int nNumberofArgs, char* pszArgs[])
{
	node *head = NULL;
	node *last = NULL;
	
	ENQUEUE(head, last, 2);
	ENQUEUE(head, last, 11);
	ENQUEUE(head, last, 3);
	ENQUEUE(head, last, 66);
	ENQUEUE(head, last, 7);
	ENQUEUE(head, last, 65);
	ENQUEUE(head, last, 222);
	ENQUEUE(head, last, 13);
	ENQUEUE(head, last, 444);
    ENQUEUE(head, last, 16);
	
	head = DEQUEUE(head,last);	
	head = DEQUEUE(head,last);
	
	FRONT(head);
	showList(head);
	
	MAKENULL(head);
	showList(head);
	
	
}
