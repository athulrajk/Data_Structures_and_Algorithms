# In this case an undirected graph is considered
# The graph is represented as an adjacency list
# in here the graph is a list of list,
# nodes are represented as numbers from 0,1,2...
# each index in the graph is a node
# each list in the graph at a particular index ,
# represents the nodes connected to that node (or index)
graph=[[1],[0,2,9],[1,3,4,8],[2,6],[2],[7],[3],[5],[2],[1]]
# The nodes are colored
# colors are represented as numbers form 0,1,2...
# The number at each index shows the color of that particular node (or index)
color=[0,0,0,1,0,2,1,2,0,0]

# a depth first search function that traverses through the graph
# it takes in parameters current node and color of the starting node
# returns the length of the monochromatic path starting from the starting node
def dfs(cur_node,cur_col):
    # to store the length
    len=1
    # visited list to mark if a node is visited
    visited[cur_node]=True
    # iterate through each node connected to cur_node
    # if the color of the node is same as cur_col and if its not visited
    # visit the node
    for i in graph[cur_node]:
        if visited[i]==False and color[i]==cur_col:
            # making the best choice at a junction
            cur_len=dfs(i,cur_col)
            if cur_len+1 > len:
                len=cur_len + 1
    # return len
    return len 

#main
if __name__=='__main__':
    # to store max len
    max_len=0
    # visited list to for marking the already visited list
    visited=[False]*len(graph)
    # start a dfs from each node in graph and get the longest monochromatic
    # path starting from that node
    # if its greater than max_len, change max_len
    for node in range(0,len(graph)):
        if visited[node]==False:
            max_len=max(max_len,dfs(node,color[node]))
    # print max_len
    print(max_len)
