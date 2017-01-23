//Matthew DiGiacomo
//CS 260 PA2
//February 21st, 2015

#include<iostream>
#include<vector>
#include<string>
using namespace std;

struct node
{
 node * leftChild;
 node * rightChild;
 double frequency;
    string content;
 string code;
};

vector<node> nodeArray;// Use nodeArray to record all the nodes that may be created in the whole process

node  extractMin()
{ 
 double temp = (double) INT_MAX;
    vector<node>::iterator i1,pos;
    for(i1 = nodeArray.begin();i1!=nodeArray.end();i1++)
 {
  
  if(temp>(*i1).frequency)
  {
     pos = i1;
     temp = (*i1).frequency;
  }
 }
 
 node tempNode = (*pos);
 nodeArray.erase(pos);
 
 
 
 return tempNode;
}
                     


node getHuffmanTree()
{

 while(!nodeArray.empty())
 {
      
  
   node * tempNode = new node;   
      node * tempNode1 = new node;
   node * tempNode2 = new node;
      *tempNode1 = extractMin();
   *tempNode2 = extractMin();
   
  
   tempNode->leftChild = tempNode1;
   tempNode->rightChild = tempNode2;
   tempNode->frequency = tempNode1->frequency+tempNode2->frequency;
   nodeArray.push_back(*tempNode);
   if(nodeArray.size() == 1)//only the root node exsits
   {
    break;
   }
 }
    return nodeArray[0];
}


void BFS(node * temproot,string s)
{
   node * root1 = new node;
   root1 = temproot;
  
   root1->code = s;
   if(root1 == NULL)
   {
    
   }
   else if(root1->leftChild == NULL && root1->rightChild == NULL)
   {
    
    cout<<"Character: "<<root1->content<<endl;
    cout<<"Code is: "<<root1->code<<endl;
   }
   else
   {
   
      root1->leftChild->code = s.append("0");
   s.erase(s.end()-1);
   root1->rightChild->code = s.append("1");
   s.erase(s.end()-1);


      BFS(root1->leftChild,s.append("0"));
   s.erase(s.end()-1);
      BFS(root1->rightChild,s.append("1"));
   s.erase(s.end()-1);
 }
   
}




void getHuffmanCode()
{
 int size,i;
 double tempDouble;
 string tempString = "";
 
 //Get input size from user on cmd line
 cout<<"Input How many Things you want to encode:"<<endl;
 cin>>size;
 
 //Get input from user on characters and freq's from cmd line
 for(i = 0;i<size;i++)
 {
  cout<<"Input Characters and Their Frequencies: "<<endl;
  node tempNode;
  cin>>tempString;
  cin>>tempDouble;


  tempNode.frequency = tempDouble;
  tempNode.content = tempString;
  tempNode.leftChild = NULL;
  tempNode.rightChild = NULL;
  nodeArray.push_back(tempNode);
 }

 node root = getHuffmanTree(); //run huffman tree function

 BFS(&root,"");
 
}


int main()
{
 
 vector<int> test;
 test.push_back(1);
 test.push_back(2);
 test.push_back(3);
 test.push_back(4);
 vector<int>::iterator i1 = test.begin();
 test.erase(i1);
    
    
 getHuffmanCode(); //run huffman code function to get user input
 return 0;
}

