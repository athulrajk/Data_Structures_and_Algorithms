"""
B is list of strings in which A represents the starting location, and goal is to reach the bottom right part of the grid
X represents obstacles
Strangers are located at certain location facing the direction represented by < > ^ v on the grid
A Stranger can see everything in the direction in which they are facing as far as the first obstacle or any other stranger
!!Avoid obstacles and Strangers sight!!
"""

#function create maze that creates the maze from the given B list
def create_maze(B,N,M):
    #initialize a 2d array with 0
    maze=[[0 for i in range(M)] for j in range(N)]
    #initialize start point as (0,0)
    start_pt=(0,0)
    #iterate through the B list
    for i in range(N):
        #iterate through the string B[i]
        for j in range(M):
            #start point
            if B[i][j]=='A':
                start_pt=(i,j)
            #obstacle
            if B[i][j]=='X':
                #mark tile as 1 (cannot be traversed)
                maze[i][j]=1
            #stranger looking >
            if B[i][j]=='>':
                #mark tile as 1
                maze[i][j]=1
                #mark all tiles to the right as 1(cannot be traversed)
                #till any obtacle or stranger is seen
                for k in range(j+1,M):
                    maze[i][k]=1
                    if B[i][k]!='.':
                        break
            #similarly do for all directions
            if B[i][j]=='<':
                maze[i][j]=1
                for k in range(j-1,-1,-1):
                    maze[i][k]=1
                    if B[i][k]!='.':
                        break
            if B[i][j]=='^':
                maze[i][j]=1
                for k in range(i-1,-1,-1):
                    maze[k][j]=1
                    if B[k][j]!='.':
                        break
            if B[i][j]=='v':
                maze[i][j]=1
                for k in range(i+1,N):
                    maze[k][j]=1
                    if B[k][j]!='.':
                        break                
    #mark start point and end point as 0
    #can be traversed
    x,y=start_pt 
    maze[x][y]=maze[N-1][M-1]=0
    #return maze,start_pt
    return maze,start_pt

#solution function
#it first makes a call to create_maze function to create
#a maze out of the following conditions
#in the maze obtained 0 represents tiles that can be traversed
#while 1 represents the tiles that cannot be traversed
#it then with the help of breadth first search looks
#for a path from start to bottom right
#and returns true if it exists else returns false
def solution(B):
    #evaluate N and M
    N=len(B)
    M=len(B[0])
    #call create_maze
    maze,start=create_maze(B,N,M)
    #create a visited list for marking the visited tiles during bfs
    visited=[[False for i in range(M)] for j in range(N)]
    #direction lists
    #the pair dr[i],dc[i] together constitute a direction up,down,left,right
    dr=[1,-1,0,0]
    dc=[0,0,1,-1]
    end=(N-1,M-1)
    #create queue for bfs
    queue=[]
    #insert start into queue
    queue.append(start)
    #mark start as visited
    x,y=start
    visited[x][y]=True

    while(len(queue)!=0):
        cur_x,cur_y=queue[0]
        queue.pop(0)
        #if end is reached
        if((cur_x,cur_y)==end):
            return True
        #move to all possible directions    
        for i in range(4):
            #check if moving in a particular direction is valid
            #check if the next position is not visited and can be traversed in the maze (marked 0)
            if(cur_x+dr[i]>=0 and cur_y+dc[i]>=0 and cur_x+dr[i]<N and cur_y+dc[i]<M and \
               visited[cur_x+dr[i]][cur_y+dc[i]]==False and maze[cur_x+dr[i]][cur_y+dc[i]]==0):
                #append it to queue
                queue.append((cur_x+dr[i],cur_y+dc[i]))
                #mark as visited
                visited[cur_x+dr[i]][cur_y+dc[i]]=True
    
    #no path found return false
    return False

#main
if __name__=='__main__':
    #B list
    B=["...Xv","AX..^",".XX.."]
    
    #printing the B list
    print(B)
    #call solution(B) and print
    print(solution(B))






    
