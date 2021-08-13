"""FILE FORMAT

no_of_test_cases
no_of_vertices no_of_edges
first_vertex second_vertex weight
.
.
.
"""

#main
if __name__=='__main__':
    #open the read and write files
    with open('Input.txt') as f:
        #read the no of test cases
        t_cases=int(f.readline())
        #iterate through each test case
        for cases in range(0,t_cases):
            #read values for n and m
            #since it is a f.readline() is a string of the line, it needs to be split
            n,m=[int(i) for i in f.readline().split()]
            #graph is represented as a adjacency list
            # undirected graph
            graph=[[] for i in range(0,n+1)]
            #iterate through each edge in the file
            for edges in range(0,m):
                u,v,w=[int(i) for i in f.readline().split()]
                #since it is a undirected graph
                graph[u].append((v,w))
                graph[v].append((u,w))
            #just printing the graph on console
            print(graph)
