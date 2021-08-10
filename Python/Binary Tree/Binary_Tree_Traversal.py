#          1
#         / \
#        2   3
#       / \
#      4   6
#     /
#    5


class Node:
  def __init__(self,key):
    self.left=None
    self.right=None
    self.data=key

def level_order(start):#Using Breadth First Search
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

def in_order(node):
  if node==None:
    return
  if node.left!=None:
    in_order(node.left)
  print(node.data)
  if node.right!=None:
    in_order(node.right)

def pre_order(node):
  if node==None:
    return
  print(node.data)
  if node.left!=None:
    pre_order(node.left)
  if node.right!=None:
    pre_order(node.right)

def post_order(node):
  if node==None:
    return
  if node.left!=None:
    post_order(node.left)
  if node.right!=None:
    post_order(node.right)
  print(node.data)

if __name__=='__main__':
  root=Node(1)
  root.left=Node(2)
  root.right=Node(3)
  root.left.left=Node(4)
  root.left.right=Node(6)
  root.left.left.left=Node(5)
  level_order(root)
  in_order(root)
  pre_order(root)
  post_order(root)
