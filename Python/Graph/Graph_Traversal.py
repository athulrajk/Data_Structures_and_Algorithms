class Graph:  
    def __init__(self, start_edges=None):
        self.adj_list = dict()
        if start_edges is not None:
            for u, v in start_edges:
                print(u,v)
                self.add_edge(u, v)

    def add_edge(self,u,v):   
        if u not in self.adj_list.keys():         
            self.adj_list[u]=[]
        self.adj_list[u].append(v)
    
    def add_vertex(self,u):
        self.adj_list[u]=[]

    def dfs(self, v_start=None, v_end=None):
        visited_list=[]
        
        def start_dfs(s_node=None,e_node=None):
            if s_node in visited_list:
                return
            visited_list.append(s_node)
            if s_node==e_node:
                return True 
            if s_node in self.adj_list.keys():    
                for i in self.adj_list[s_node]: 
                    if i not in visited_list:
                        if start_dfs(i,e_node)==True:
                            return True

        start_dfs(v_start,v_end)
        print(visited_list)
    
    def bfs(self,v_start=None,v_end=None):
        visited_list=[]
        visited_list.append(v_start)
        queue=[]
        queue.append(v_start)
        while(len(queue)!=0):
            cur_node=queue[0]
            queue.pop(0)
            if cur_node==v_end:
                break
            if cur_node in self.adj_list.keys():
                for i in self.adj_list[cur_node]:
                    if i not in visited_list:
                        visited_list.append(i)
                        queue.append(i)
        print(visited_list)


if __name__=='__main__':
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = Graph(edges)
    print(g.adj_list)
    g.dfs('A','D')
    g.bfs('A','D')
