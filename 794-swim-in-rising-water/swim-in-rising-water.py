class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])
        
        minHeap=[(grid[0][0],0,0)]
        directions=[[1,0],[0,1],[-1,0],[0,-1]]

        visited=set()
        while minHeap:
            maxWaterLvl,r,c=heapq.heappop(minHeap)
            if (r,c)in visited:
                continue
            visited.add((r,c))
            if r==ROWS-1 and c==COLS-1:
                return maxWaterLvl

            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if nr<0 or nr>=ROWS or nc<0 or nc>=COLS:
                    continue
                newWaterLvl=max(maxWaterLvl,grid[nr][nc])
                heapq.heappush(minHeap,(newWaterLvl,nr,nc))
        return -1