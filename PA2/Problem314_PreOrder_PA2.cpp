//Matthew DiGiacomo
//CS 260 PA2
//February 21st, 2015

#include <iostream>
#include <fstream>
#include <stack>

 
using namespace std;
 
void PRINTEX(char expression[]);
void ReverseArray (char arr []);
bool isNumber(char &exp);

void PRINTEX(char arr [])
{
    for(int i = 0; i < 7; i++)
    {
        cout<<arr[i];
    }
    cout << endl;
    
}
void ReverseArray(char arr [])
{
    int end = 6;
    int start = 0;
    char temp;
    while(start < end)
    {
        temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        start++;
        end--;
    }
}
bool isNumber(char &n)//pass in a char reference
{
 
    if(!isdigit(n))//check if the char is a number...
    {
        return false;
    }
    else
        return true;
}
 
int main()
{
    stack<int> s;
    char expression [] = "+*572"; //result is (5*7)+2 = 37
 
    PRINTEX(expression); //display input expression
 
    int n;//a number to push onto the stack
    int result;//result after operation
    ReverseArray(expression);
 
    for(unsigned int i = 0; i < 7; i++)
    {
 
        if(isNumber(expression[i])==true)
        {
            char c = expression[i];
            n = c-'0';
            s.push(n);
        }
        if(expression[i]=='+')
        {
            int x = s.top();
            s.pop();
            int y = s.top();
            s.pop();
            result = x+y;
            s.push(result);
        }
        if(expression[i]=='-')
        {
            int x = s.top();
            s.pop();
            int y = s.top();
            s.pop();
            result = y-x;
            s.push(result);
        }
        if(expression[i]=='*')
        {
            int x = s.top();
            s.pop();
            int y = s.top();
            s.pop();
            result = x*y;
            s.push(result);
        }
        if(expression[i]=='/')
        {
            int x = s.top();
            s.pop();
            int y = s.top();
            s.pop();
            result = y/x;
            s.push(result);
        }
    }
    cout<<"result of expression: "<<s.top();//result should be 17...
 
    return 0;
}

