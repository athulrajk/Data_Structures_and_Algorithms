#include <stdio.h>
#include <stdlib.h>

struct node {
        int data;
        struct node *left, *right;
};

// create a new node
struct node* n_node(int data)
{
        struct node* tmp = (struct node*)malloc(sizeof(struct node));
        tmp->data = data;
        tmp->left = tmp->right = NULL;
        return tmp;
}

// function for inorder traversal
// prints the tree in acending order
void inorder(struct node* root)
{
        if (root != NULL) {
                inorder(root->left);
                printf("%d ",root->data);
                inorder(root->right);
        }
}

// insert node function
//
struct node* insert(struct node* node, int data)
{
        /* If the tree is empty, return a new node */
        if (node == NULL)
                return n_node(data);

        /* Otherwise, recur down the tree */
        if (data < node->data)
                node->left = insert(node->left, data);
        else if (data > node->data)
                node->right = insert(node->right, data);

        /* return the (unchanged) node pointer */
        return node;
}

//max function to calculate max of two values
int max(int a,int b)
{
        if(a>b) return a;
        return b;
}

//get height function
//root node is passed as argument to the function
int get_height(struct node* node)

{
        //if there are no more nodes to traverse
        if(node==NULL) return 0;
        //depth of the tree is max of the depth of left and right subtrees
        //recurse left and right
        return 1+ max(get_height(node->left),get_height(node->right));
}

//count the no of nodes
int cnt_nodes(struct node* node)
{
        //if there are no more nodes to be traversed
        if(node==NULL) return 0;
        //recurse to left and right subtree and add the values
        return 1+ cnt_nodes(node->left) + cnt_nodes(node->right);
}

// main
int main()
{
        int array[]={4,6,2,7,9,8,3};
        int array_size=7;
        struct node* root = NULL;
        root = insert(root, array[0]);
        for(int i=1;i<7;i++)
           {
                insert(root,array[i]);
           }
        
        //PRINT THE TREE
        // print inoder traversal of the BST
        inorder(root);

        //get the height
        int h=get_height(root)-1;
        printf("\nheight = %d\n",h);

        //count the nodes
        int cnt=cnt_nodes(root);
        printf("\nno of nodes = %d\n",cnt);
        return 0;
}
