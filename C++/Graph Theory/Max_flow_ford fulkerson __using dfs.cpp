#include<bits/stdc++.h>
using namespace std;

const int V=6;
int Flow_Graph[V][V]={{ 0, 16, 13, 0, 0, 0 }, { 0, 0, 0, 12, 0, 0 },
                      { 0, 4, 0, 0, 14, 0 },  { 0, 0, 9, 0, 0, 20 },
                      { 0, 0, 0, 7, 0, 4 },   { 0, 0, 0, 0, 0, 0 } };

bool DFS(int rGraph[V][V],int src,int snk,int parent[]){
	int visited[V]={0};
	bool ok=false;
	function<void(int)> dfs=[&](int node){
		visited[node]=1;
		for(int v=0;v<V;v++){
			if(visited[v]==0 && rGraph[node][v]>0){
				parent[v]=node;
				if(v==snk) {
					ok=true;
					return;
					}
				dfs(v);
				}
			}	
		};
	dfs(src);	
	return ok;	
	}

int Ford_Fulkerson(int src,int snk){
	int rGraph[V][V];//Residual Graph
	for(int u=0;u<V;u++){
		for(int v=0;v<V;v++){
			rGraph[u][v]=Flow_Graph[u][v];
			}
		}
	int parent[V];
	int max_flow=0;
	while(DFS(rGraph,src,snk,parent)){
		//max flow through the current path 
		int cur_path_flow=1e9;
		for(int v=snk;v!=src;v=parent[v]){
			cur_path_flow=min(cur_path_flow,rGraph[parent[v]][v]);
			}
		//update the residual graph
		for(int v=snk;v!=src;v=parent[v]){
			rGraph[parent[v]][v]-=cur_path_flow;
			rGraph[v][parent[v]]+=cur_path_flow;
			}
		max_flow+=cur_path_flow;		
		}
	return max_flow;		
	}	


int main(){
	cout<<Ford_Fulkerson(0,5);
	}
