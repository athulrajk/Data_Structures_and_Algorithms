#for generating a random list
import random

#Node class
class Node:
  #parameterized constructor that takes value of node as parameter  
  def __init__(self,key=None):
    #initializing instance varibles  
    self.left=None
    self.right=None
    self.val=key

#function to insert into binary search tree
def insert(root,val):
    #if the tree is empty return root
    if root is None:
        return Node(val)
    #tree is non empty    
    else:
        #ensuring tree does not have duplicate values
        if root.val==val:
            return root
        #if the value to be inserted is greater than current value
        # move right    
        elif root.val < val:
            root.right=insert(root.right,val)
        #if the value to be inserted is less than current value
        # move left 
        else:
            root.left=insert(root.left,val)
    #return the original root node
    return root

#inorder traversal
def in_order(node):
  #if node is None return
  if node==None:
    return
  #move left  
  if node.left!=None:
    in_order(node.left)
  #print value
  print(node.val,end=' -> ')
  #move right
  if node.right!=None:
    in_order(node.right)

#preorder traversal
def pre_order(node):
  #return if node is None  
  if node==None:
    return
  #print value  
  print(node.val,end=' -> ')
  #move left
  if node.left!=None:
    pre_order(node.left)
  #move right
  if node.right!=None:
    pre_order(node.right)

#post order 
def post_order(node):
  #if node is None return
  if node==None:
    return
  # move left  
  if node.left!=None:
    post_order(node.left)
  #move right
  if node.right!=None:
    post_order(node.right)
  #print value
  print(node.val,end=' -> ')

#Level order Using Breadth First Search
def level_order(start):
  if start==None: 
    return
  queue=[]
  queue.append(start)
  while len(queue)!=0:
    cur=queue[0]
    print(cur.data)
    queue.pop(0)
    if(cur.left!=None):
      queue.append(cur.left)
    if(cur.right!=None):
      queue.append(cur.right)

#search function
def search(node,key):
    #node is None then key is not present
    #or key is equal to node.val
    if node is None or node.val==key:
        #return node
        return node
    #if node.val is less than key 
    # move right    
    if node.val<key:
        return search(node.right,key)
    #else move left
    elif node.val>key:
        return search(node.left,key)

#function to calculate depth
def depth(node):
    #if node is None return 0
    if node is None:
        return 0
    #return max of depth of left subtree and right subtree    
    return 1+max(depth(node.left),depth(node.right))
    

#main
if __name__=='__main__':
    #replace 'LAST_NAME' with last name
    list=random.sample(range(1,100),20)
    #creating root and initializing it to None
    root=None
    #iterate through the last name string
    for i in list:
        #convert each character to ASCII no 
        #and insert into BST
        root=insert(root,i)
    #the function returns 1+depth(tree)    
    print('\nDEPTH/HEIGHT OF THE TREE = ',depth(root)-1)
    #Traversals
    print('\ninorder')
    in_order(root)    
    print('\n\npreorder')
    pre_order(root)
    print('\n\npostorder')
    post_order(root)
    #search for 67 in BST
    if search(root,67)==None:
        print('\nNot Found\n')
    else:
        print('\nFound\n')
