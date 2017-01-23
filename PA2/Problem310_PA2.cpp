//Matthew DiGiacomo
//CS 260 PA2
//February 21st, 2015

#include <stdio.h>
#include <stdlib.h>
#define MAX_Q_SIZE 500

struct node
{
    int data;
    struct node* left;
    struct node* right;
    struct node* middle;
};
 
struct node** createQueue(int *, int *);
void ENQUEUE(struct node **, int *, struct node *);
struct node *deQueue(struct node **, int *);
 
/* Given a tree, print its nodes in level order
   using array for implementing queue */
void printLevelOrder(struct node* root)
{
  int rear, front;
  struct node **queue = createQueue(&front, &rear);  
  struct node *temp_node = root; 
 
  while(temp_node)
  {
    printf("%d ", temp_node->data);
 
   
    if(temp_node->left)
      ENQUEUE(queue, &rear, temp_node->left);
 
 	if(temp_node->middle)
      ENQUEUE(queue, &rear, temp_node->middle);
   
    if(temp_node->right)
      ENQUEUE(queue, &rear, temp_node->right);
 
    temp_node = deQueue(queue, &front);
  }
}
 

struct node** createQueue(int *front, int *rear)
{
  struct node **queue =
   (struct node **)malloc(sizeof(struct node*)*MAX_Q_SIZE);  
 
  *front = *rear = 0;
  return queue;
} 
 
void ENQUEUE(struct node **queue, int *rear, struct node *new_node)
{
  queue[*rear] = new_node;
  (*rear)++;
}     
 
struct node *deQueue(struct node **queue, int *front)
{
  (*front)++;
  return queue[*front - 1];
}     
 

struct node* newNode(int data)
{
  struct node* node = (struct node*)
                       malloc(sizeof(struct node));
  node->data = data;
  node->left = NULL;
  node->right = NULL;
  node->middle = NULL;
 
  return(node);
}
 
int main()
{
  //construct tree from Figure 3.31
  struct node *root = newNode(1); //A
  root->left        = newNode(2); //B
  root->right       = newNode(3); //C
  root->left->left  = newNode(4); //D
  root->left->right = newNode(5);  //E
  root->right->left = newNode(6); //F
  root->right->middle = newNode(7); //G
  root->right->right = newNode(8); //H
  root->left->right->middle = newNode(9); //I
  root->right->middle->left = newNode(10); //J
  root->right->middle->right = newNode(11); //K
  root->right->right->middle = newNode(12); //L
  root->left->right->middle->left = newNode(13); //M
  root->left->right->middle->right = newNode(14); //N
  
  printf("Level Order traversal of tree is \n");
  printLevelOrder(root);
 
  getchar();
  return 0;
}
