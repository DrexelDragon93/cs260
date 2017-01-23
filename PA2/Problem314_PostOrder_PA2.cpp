//Matthew DiGiacomo
//CS 260 PA2
//February 21st, 2015

#include<iostream>
#include<conio.h>
#include<ctype.h>

using namespace std;
 
//The class performing the evaluation
class Evaluation 
{
	
	public:
		int st[50];
		int top;
		char str[50];
		Evaluation() {
			top = -1;
}
 
//function to push the item
void push(int item) 
{
	top++;
	st[top] = item;
}
 
//function to pop an item
int pop() 
{
	int item = st[top];
	top--;
		return item;
}
 
//function to perform the operation depending on the operator
int operation(int a,int b,char opr) 
{
	switch(opr) 
	{
		case '+':return a+b;
		case '-':return a-b;
		case '*':return a*b;
		case '/':return a/b;
	}
}
 
		int calculatePostfix();
};
 
//This is the function that calculates the result of postfix expression
int Evaluation::calculatePostfix() 
{
	int index = 0;
	while(str[index]!=NULL) {
		if(isdigit(str[index])) {
			push(str[index]-'0');
		}
		else {
			int x = pop();
			int y = pop();
			int result = operation(x,y,str[index]);
			push(result);
		}
		index++;
	}
	return pop();
}
 
//	main function that reads the postfix expression and	that prints the result
// takes user input for the postfix expression, ie - "26/"

int main() {
	
	Evaluation eval;
	cout << "Enter the postfix: ";
	cin >> eval.str;
	
	int result = eval.calculatePostfix();
	cout << "the result is " << result;
	
}
