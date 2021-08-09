#include<bits/stdc++.h>
using namespace std;

const int N=5,M=5;
int a[N][M]={{1,1,0,1,0},{1,1,0,1,0},{1,1,1,1,0},{1,1,1,1,0},{1,1,1,0,0}};

//iterate through each square matrix in a matrix
//max order of the sub square matix having all ones.
int solve(){
	int max_size=0;
	for(int n=0;n<N;n++){
	  for(int m=0;m<M;m++){
		 if(a[n][m]==0) continue;
		 int cur_size=1;
		 for(int k=1;n+k<N && m+k<M;k++){
		    if(a[n+k][m+k]==0) break;
		    bool ok=true;
		    for(int i=n;i<=n+k;i++){
				if(a[i][m+k]==0){
				   ok=false;
				   break;
				 }
			   }
		    for(int i=m;i<=m+k;i++){
			    if(a[n+k][i]==0){
				   ok=false;
				   break;
				 }
			   }  	 
			if(!ok) break;
			else cur_size++;
			}
		 m=m+cur_size;		
		 max_size=max(max_size,cur_size);
		 if(N-max_size<=max_size||M-max_size<=max_size) return max_size;	 
		  }
		}
	return max_size;
}

int main(){
cout<<solve();
}
