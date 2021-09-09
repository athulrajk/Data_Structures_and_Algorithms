#include<iostream>
using namespace std;
//node struct
struct node{
	//data part in node
	int data;
	//left child
	node* left;
	//right child
	node* right;
	//constructor for node
	node(int data){
		//initializes data to argument
		this->data=data;
		//initializes left and right child to NULL
		this->left=NULL;
		this->right=NULL;
		}	
	};
//int_max and int_min must be initialized with large value greater than any other
//element in the Binary tree and int_min with very small value less than any other 
//value in Binary tree
int int_max=1e9;
int int_min=-1e9;

//check if the Binary tree is Binary Search tree
//it is a binary search tree if left subtree of a node contain only values less
//than that of the node and right child of the node contains only nodes whose value
//is greater than node

//the algorithm recurses down the tree keeping track of the max and min value 
//a node can take,if it is not in the range return false

//the algorithm assumes the BST does not contain duplicate values
bool is_BinarySearchTree(node* nnode,int min_=int_min,int max_=int_max){
	//base case ,if nnode is null return true
	if(nnode==NULL) return true;
	//if the value is not in the range
	if((nnode->data<=min_)||(nnode->data>= max_)) return false;
	//recurse down to left and right subtree
	//when we recurse down to the right subtree we make the min value equal to
	//current node value
	//when we recurse down to the left subtree we make the max value equal to
	//current node value
	return (is_BinarySearchTree(nnode->left,min_,nnode->data))&&
		   (is_BinarySearchTree(nnode->right,nnode->data,max_));
}

int main(){
	//create a root and using it create a binary tree
    node *root = new node(22);
    root->left = new node(16);
    root->right = new node(51);
    root->left->left = new node(7);
    root->left->right = new node(19);
    root->right->left= new node(43);
    root->right->right= new node(57);
    //check if the binary tree is BST
    //prints 1 if BST else prints 0
    cout<<is_BinarySearchTree(root);
}	

