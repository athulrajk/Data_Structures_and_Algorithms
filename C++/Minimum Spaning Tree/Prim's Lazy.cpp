#include<bits/stdc++.h>
using namespace std;

//Prim's Lazy implementation
vector<pair<int,int>> graph[]={
					 {{1,4},{7,8}},
					 {{0,4},{7,11},{2,8}},
					 {{1,8},{8,2},{3,7},{5,4}},
					 {{2,7},{4,9},{5,14}},
					 {{3,9},{5,10}},
					 {{4,10},{3,14},{2,4},{6,2}},
					 {{5,2},{8,6},{7,1}},
					 {{6,1},{8,7},{1,11},{0,8}},
					 {{2,2},{6,6},{7,7}}
					};
int visited[9];
priority_queue<pair<int,pair<int,int>>> pq;
//to store the MST edges
vector<pair<int,int>> MST;
//to store the cost of MST
int MST_cost;

void Lazy_Prim(int s_node=0){
	visited[s_node]=1;
	for(auto i:graph[s_node]){
		pq.push({-1*i.second,{s_node,i.first}});
		}
	while(!pq.empty() && (int)MST.size()!=9){
		auto node=pq.top();
		pq.pop();
		if(visited[node.second.second]) continue;
		cout<<-1*node.first<<" ("<<node.second.first<<","<<node.second.second<<")\n";
		MST.push_back({node.second.first,node.second.second});
		MST_cost+=-1*node.first;
		visited[node.second.second]=1;
		for(auto i:graph[node.second.second]){
			pq.push({-1*i.second,{node.second.second,i.first}});
			}
		}		
	}

int main(){
Lazy_Prim();
cout<<MST_cost;
//print MST	
}
