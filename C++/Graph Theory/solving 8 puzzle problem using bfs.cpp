#include<iostream>
#include<queue>
#include<map>

using namespace std;

struct state
{   //current state of the matrix
    char matrix[3][3];
    // stores blank tile coordinates
    int blank_x,blank_y;
    // store the error
    //error is the no of tiles different from the end state 
    int err;
    //cost ->no of moves
    int cost;
    //overloading < operator for map or set
    bool operator < (const state& other) const{
        for (int i=0; i<3; i++) {
             for (int j=0; j<3; j++) {
                 if (matrix[i][j] < other.matrix[i][j]) {
                     return true;
                 }
                 if (matrix[i][j] > other.matrix[i][j]) {
                     return false;
                 }
             }
        }
        return false; // all were equal
    }
};

state new_state(char matrix[3][3],int blank_x, int blank_y, int new_blank_x,int new_blank_y, int cost)
{   //create new state
    state node;
    // copy data from parent matrix to current state matrix
    for(int i=0;i<3;i++){
		for(int j=0;j<3;j++){
			node.matrix[i][j]=matrix[i][j];
			}
		}
 
    // move tile by 1 position
    swap(node.matrix[blank_x][blank_y], node.matrix[new_blank_x][new_blank_y]);
 
    // set no of moves so far
    node.cost = cost;
    
    // update new blank tile coordinates
    node.blank_x = new_blank_x;
    node.blank_y = new_blank_y;
    //set error to 0
    node.err=0;
    //return the created node
    return node;
}

// down,up,left,right
//the four directions
//each of the row[i] and col[i] together constitute a direction
int row[] = { 1, 0, -1, 0 };
int col[] = { 0, -1, 0, 1 };

//function to calculate deviation from current state and end state
int calculate_error(char cur_state[3][3], char e_state[3][3])
{
    int count = 0;
    for (int i = 0; i < 3; i++)
      for (int j = 0; j < 3; j++)
        if (cur_state[i][j]!='#' && cur_state[i][j] != e_state[i][j])
           count++;
    return count;
}

//to check if the move is possible
int isok(int x, int y)
{
    return (x >= 0 && x < 3 && y >= 0 && y < 3);
}

void bfs(char s_state[3][3], int x, int y,char e_state[3][3])
{   
    //creating a map to mark visited states (a set can also be used)
    map<state,int> visited;
    queue<state> q;//queue for bfs
    // create a start node and calculate its error
    state s = new_state(s_state, x, y, x, y, 0);
    s.err = calculate_error(s_state,e_state); 
    // add start state to queue
    q.push(s);
    visited[s]=1;
    while (!q.empty())
    {   
        // create node using cur state
        state cur = q.front();
        q.pop();
        //cout<<cur.cost<<" "<<cur.err<<"\n";
        // if e_state has been reached
        if (cur.err == 0)
        {
            cout<<cur.cost<<"\n";
            return;
        }
 
		//try all possible 4 moves
        for (int i = 0; i < 4; i++)
        {   //check move is possible or not
            if (isok(cur.blank_x + row[i], cur.blank_y + col[i]))
            {
                // create a new state and calculate
                // its error
                state child = new_state(cur.matrix, cur.blank_x,cur.blank_y, cur.blank_x + row[i],cur.blank_y + col[i],cur.cost + 1);
                child.err = calculate_error(child.matrix, e_state);
                if(visited[child]!=1){
					q.push(child);
					visited[child]=1;	
				}
            }
        }
    }
}


int main(){
int blank[2];	
string s_config;
cin>>s_config;
char s_matrix[3][3];
//input the config into matrix
for(int i=0;i<(int)s_config.length();i++){
	//i/3 represents the row to be inserted
	//i%3 represents the column to be inserted
	s_matrix[i/3][i%3]=s_config[i];
	//if blank space
	//insert its location into blank
	if(s_config[i]=='#'){
		blank[0]=i/3;
		blank[1]=i%3;
		}
	}
string e_config;
cin>>e_config;
char e_matrix[3][3];
//input the config into matrix
for(int i=0;i<(int)e_config.length();i++){
	//i/3 represents the row to be inserted
	//i%3 represents the column to be inserted
	e_matrix[i/3][i%3]=e_config[i];
	}
bfs(s_matrix,blank[0],blank[1],e_matrix);		
}

