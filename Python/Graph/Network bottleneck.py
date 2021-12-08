"""
Maximum data that can be transferred from one computer to another in a network through a single path

Using djikstra
"""

#importing priotrity queue
from queue import PriorityQueue
#function djikstra
def djikstra(graph,n,src):
    visited=[0 for i in range(n+1)]
    dist=[-1 for i in range(n+1)]
    pq=PriorityQueue()
    dist[src]=1e9
    pq.put((dist[src],src))
    while(not pq.empty()):
        cur_dist,cur_node=pq.get()
        cur_dist=abs(cur_dist)
        visited[cur_node]=1
        for i in graph[cur_node]:
            if visited[i[0]]==0 and dist[i[0]]<min(cur_dist,i[1]):
                dist[i[0]]=min(cur_dist,i[1])
                pq.put((-1*dist[i[0]],i[0]))
    dist[src]=0
    return dist

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
        graph=[[] for j in range(n+1)]
        #insert all edges
        for _ in range(m):
            u,v,d=[int(i) for i in f.readline().split()]
            graph[u].append((v,d))
        #read input for source
        src=int(f.readline())
        #function call and writing to file 
        for i in djikstra(graph,n,src)[1:]:
            w1.writelines(str(i)+' ')
        w1.writelines('\n')

        
