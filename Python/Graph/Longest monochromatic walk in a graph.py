
"""
graph is directed, graph may contain cycles
if cycle is detected print("Undefined")
"""
graph=[[1],[2,9],[3,4,8],[],[],[7],[3],[],[],[]]
color=[0,0,0,0,0,0,0,0,0,0]
detect_cycle=False

def dfs(cur_node,cur_col):
    len=1
    for i in graph[cur_node]:
        visited[cur_node]=True
        stack[cur_node]=True
        if (visited[i]==True) and (color[i]==cur_col) and (stack[i]==True):
            global detect_cycle
            detect_cycle=True
        if visited[i]==False and color[i]==cur_col:
            cur_len=dfs(i,cur_col)
            if cur_len+1>len:
                len=cur_len+1
    stack[cur_node]=False
    return len

if __name__=='__main__':
    max_len=0
    visited=[False]*len(graph)
    stack=[False]*len(graph)
    for node in range(0,len(graph)):
        if detect_cycle==True:
            break
        if visited[node]==False:
            max_len=max(max_len,dfs(node,color[node]))
    if detect_cycle==True:
        print("Undefined")
    else:
        print(max_len)
