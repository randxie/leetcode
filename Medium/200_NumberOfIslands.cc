class Solution {
public:
    int bx;
    int by;
    int numIslands(vector<vector<char>>& grid) {
		if(grid.empty()){
			return 0;
		}
		bx=int(grid.size());
		by=int(grid[0].size());
		int number=0;
		for (int i=0;i<bx;i++)
		{
			for (int j=0;j<by;j++)
			{
				if((grid[i][j])=='1')
				{

					myDFS(grid,i,j);
					number++;
				}
			}
		}
		return number;
    };

    void myDFS (vector< vector<char> >& grid, int i, int j){
    	grid[i][j]='2';
    	if ((i-1)>=0){
    		if(grid[i-1][j]=='1')
    		{
	    		myDFS(grid,i-1,j);
    		}
    	}
    	if ((i+1)<bx){
    		if(grid[i+1][j]=='1'){
    			myDFS(grid,i+1,j);
    		}
    	}
    	if ((j-1)>=0){
    		if(grid[i][j-1]=='1'){
    			myDFS(grid,i,j-1);
    		}
    	}
    	if ((j+1)<by){
    		if(grid[i][j+1]=='1'){
    			myDFS(grid,i,j+1);
    		}
    	}
    }

};