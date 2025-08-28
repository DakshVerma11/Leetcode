class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)


        for i in range(n):
            temp=[]
            for j in range(n-i):
                temp.append(grid[i+j][j])
            temp.sort()
            #print(temp)
            for j in range(n-i):
                grid[i+j][j]=temp.pop()
        
        #print(grid)
        for j in range(1,n):
            temp=[]

            for i in range(n-j):
                temp.append(grid[i][i+j])
            temp.sort(reverse=True)
            #print(temp)
            for i in range(n-j):
                grid[i][i+j]=temp.pop()

        #print(grid)
        return grid