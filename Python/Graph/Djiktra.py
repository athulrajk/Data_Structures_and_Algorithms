#import Priotity Queue from the queue module
# the module is based on a heapq module
# which is used to implement a heap
# priority queues are implemented using heaps
from queue import PriorityQueue
# This is a lazy implementation of Djikstra's algorithm
# During the execution the priority queue may contain
# more than one instance of the same node
def djikstra(s_node,e_node,Graph,N):
        #visited list to mark the nodes visited
        visited=[False]*(N+1)
        #dist list to keep the shortest distance to each node, initialize to large value
        dist=[1e9]*(N+1)
        #mark the start node as visited and distance as 0
        dist[s_node]=0
        visited[s_node]=True
        #instantiating priority queue 
        p_queue=PriorityQueue()
        #pushing the start node to the queue
        #each element of the queue is a tuple(dist,node)
        p_queue.put((dist[s_node],s_node))

        """if an actual priority queue is not available, a list can be used which needs to be sorted
           in ascending order during each iteration, (it does increase the time complexity to O(v^2))
           from O(V + Elog(V))
        """
        #while the queue is non empty
        #if a list was used
        #while(len(p_queue)!=0):
        while(not p_queue.empty()):
            # if a list is used in place of priority queue then
            # p_queue.sort()
            
            #pop the top element
            cur_dist,cur_node=p_queue.get()
            #mark the node visited
            visited[cur_node]=True
            #if destination reached return the (distance to the destination)
            if cur_node==e_node:
                return dist[e_node]
            #iterate through each node connected to cur_node
            for i in Graph[cur_node]:
                #if it is not visited and the distance to the node is less, then
                if visited[i[0]]==False and dist[i[0]]>cur_dist+i[1]:
                    dist[i[0]]=cur_dist+i[1]
                    p_queue.put((dist[i[0]],i[0]))
