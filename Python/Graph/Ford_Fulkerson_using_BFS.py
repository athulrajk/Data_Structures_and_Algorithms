"""
FIND MAXIMUM DATA THAT CAN BE TRANSFERRED FROM A COMPUTER TO EACH OF THE OTHER COMPUTERS
CONNECTED TO A NETWORK
"""

"""
To be improved further using dynamic programming
"""


"""using ford fulkerson with bfs"""

#breadth first search for finding a path from source to sink
def BFS(rgraph,src,snk,parent,n):
  visited=[0]*(n+1)
  queue=[]
  queue.append(src)
  visited[src]=1
  while len(queue)!=0:
    cur=queue.pop(0)
    for i in range(1,n+1):
      #check if visited and also check if there can be a flow
      if rgraph[cur][i]>0 and visited[i]==0:
        queue.append(i)
        visited[i]=1
        parent[i]=cur
        if i==snk:
          return True
  return False

#main
if __name__=='__main__':
  #open files to read and write
  with open('Input4.txt') as f,open('Output4.txt','w') as w1:
    #read no of test cases
    Test_Cases=int(f.readline())
    #iterate through each test case
    for tests in range(0,Test_Cases):
      #get input for n and m
      n,m=[int(i) for i in f.readline().split()]
      #construct an adjacency matrix
      graph=[[0 for i in range(n+1)] for j in range(n+1)]
      #insert all edges
      for _ in range(m):
        u,v,d=[int(i) for i in f.readline().split()]
        graph[u][v]=d
      #read input for source
      src=int(f.readline()) 
      
      #iterate through all sinks
      for snk in range(1,n+1):
        #construct a residual graph for augmenting the path
        rgraph=[[0 for i in range(n+1)] for j in range(n+1)]
        #initialize residual graph as graph
        for i in range(n+1):
          for j in range(n+1):
            rgraph[i][j]=graph[i][j]
        #create a parent list, which stores the parent of each node in the current path
        parent=[0 for i in range(n+1)]
        #max_flow
        max_flow=0
        #boolean to check if a path exists from sink to source
        # if snk==src, then path exists  
        path_exist=False if src!=snk else True
         
        #do bfs until a path can be found
        while(BFS(rgraph,src,snk,parent,n)):
          #path 
          path_exist=True
          cur_path_flow=1e9
          v=snk
          #find max_flow through the current path
          while v!=src:
            cur_path_flow=min(cur_path_flow,rgraph[parent[v]][v])
            v=parent[v]
          #augment the flow
          v=snk
          while v!=src:
            rgraph[parent[v]][v]=rgraph[parent[v]][v]-cur_path_flow
            rgraph[v][parent[v]]=rgraph[v][parent[v]]+cur_path_flow
            v=parent[v]
          
          #add the current_max_flow to max_flow
          #the current_max_flow through each of the path is the max_flow
          max_flow=max_flow+cur_path_flow
        
        #write to file
        if path_exist==True:  
          w1.writelines(str(max_flow)+' ')
        else:
          w1.writelines('-1 ')
      w1.writelines('\n')


