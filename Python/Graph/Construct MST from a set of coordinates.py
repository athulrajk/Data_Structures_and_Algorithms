from math import sqrt
from queue import PriorityQueue

def euclidean_distance(p1,p2):
  return sqrt((p1[1]-p2[1])**2+(p1[2]-p2[2])**2)

#prim's lazy implementation of mst
def mst_from_points(points):
  #keeping a list of visited nodes
  visited=[False]*(len(points))
  #starting node, (any node can be selected as the starting node)
  s_node=0
  #mark start node as visited
  visited[s_node]=True
  #list for storing the tree
  MST=[]
  #priority queue 
  pq=PriorityQueue()
  #insert all edges from start node to priority queue
  for i in range(len(points)):
    if i!=s_node:
      pq.put((euclidean_distance(points[s_node],points[i]),s_node,i))
  
  #
  while(not pq.empty() and len(MST)!=len(points)-1):
    #get the top element
    cur_node=pq.get()
    #check if the node is already part of tree
    if visited[cur_node[2]]==False:
      #add to MST list
      MST.append((cur_node[0],points[cur_node[1]][0],points[cur_node[2]][0]))
      #mark the node as visited
      visited[cur_node[2]]=True
      #insert all edges from this node to the queue
      for i in range(len(points)):
        if i!=cur_node[2]:
          pq.put((euclidean_distance(points[cur_node[2]],points[i]),cur_node[2],i))
  return MST

#test
def test_mst_from_points():
  points=[('a',5,10),
          ('b',7,12),
          ('c',2,3),
          ('d',12,3),
          ('e',4,6),
          ('f',6,7)
         ]
  mst=mst_from_points(points)
  assert round(sum(i[0] for i in mst),2)==19.04

test_mst_from_points()        

