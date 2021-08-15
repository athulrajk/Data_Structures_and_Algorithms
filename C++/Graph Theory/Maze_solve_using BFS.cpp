#include<bits/stdc++.h>
using namespace std;

const int N=4,M=4;
int Maze[N][M]={{0,1,1,1},{0,0,1,1},{1,0,1,1},{1,0,0,0}};
int dr[]={1,-1,0,0};
int dc[]={0,0,1,-1};

vector<pair<int,int>> path;

void retrace_path(pair<int,int> parent[N][M],pair<int,int> e_node){
	if(e_node.first==-1 && e_node.second==-1) return;
	path.push_back(e_node);
	retrace_path(parent,parent[e_node.first][e_node.second]);
	}

bool bfs(pair<int,int> s_node,pair<int,int> e_node){
	int visited[N][M]={0};
	vector<vector<int>> dist(N,vector<int> (M,1e9));
	pair<int,int> parent[N][M];
	queue<pair<int,int>> q;
	visited[s_node.first][s_node.second]=true;
	dist[s_node.first][s_node.second]=0;
	parent[s_node.first][s_node.second]={-1,-1};
	q.push(s_node);
	while(!q.empty()){
		pair<int,int> cur_node=q.front();
		q.pop();
		visited[cur_node.first][cur_node.second]=true;
		if(cur_node==e_node){
			cout<<dist[e_node.first][e_node.second]<<"\n";
			retrace_path(parent,e_node);
			reverse(path.begin(),path.end());
			for(auto i: path)
				cout<<"("<<i.first<<","<<i.second<<") -->  ";
			return true;
			}
		for(int i=0;i<4;i++){
			if((cur_node.first+dr[i]<N && cur_node.first+dr[i]>=0) && (cur_node.second+dc[i]<M) && (cur_node.second+dc[i]>=0) &&
			   (visited[cur_node.first+dr[i]][cur_node.second+dc[i]]==false) && (Maze[cur_node.first+dr[i]][cur_node.second+dc[i]]==0)){
					if(dist[cur_node.first+dr[i]][cur_node.second+dc[i]]>dist[cur_node.first][cur_node.second]+1){
					q.push({cur_node.first+dr[i],cur_node.second+dc[i]});
					dist[cur_node.first+dr[i]][cur_node.second+dc[i]]=dist[cur_node.first][cur_node.second]+1;
					parent[cur_node.first+dr[i]][cur_node.second+dc[i]]=cur_node;
					}
				  }
			    }			
		      }
	return false;	
	}
int main(){
bfs({0,0},{3,3});

}
