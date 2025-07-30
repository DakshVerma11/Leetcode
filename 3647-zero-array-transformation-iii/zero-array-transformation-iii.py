class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        q = collections.deque(sorted(queries))
        available = SortedList()  # available `r`s
        running = SortedList()  # running `r`s

        for i, num in enumerate(nums):
            while q and q[0][0] <= i:
                available.add(q.popleft()[1])
            while running and running[0] < i:
                running.pop(0)
            while num > len(running):
                if not available or available[-1] < i:
                    return -1
                running.add(available.pop())

        return len(available)
        
        
        """maxremoval=[-i for i in nums]
        for i in queries:
            for j in range(i[0],i[1]+1):
                maxremoval[j]+=1
        
        for i in maxremoval:
            if i<0:
                return -1
        count=0
        queries.sort(key=lambda x: x[1] - x[0] + 1,reverse=True)
        for i in queries:
            canberemoved=True
            for j in range(i[0],i[1]+1):
                if maxremoval[j]<1:
                    canberemoved=False
            if canberemoved:
                #print("canberemoved : " , i[0],i[1])
                count+=1
                for j in range(i[0],i[1]+1):
                    maxremoval[j]-=1
                    
        
        return count"""

        """
        #for i in range(len(queries)):
            #queries[i]=[queries[i][1]-queries[i][0]+1,queries[i][0],queries[i][1]]
            #queries=[length,start,end]
            
        n = len(nums)
        q = len(queries)

        def can_remove(x):
            used = queries[:q - x]

            diff = [0] * (n + 1) 
            for l, r in used:
                diff[l] += 1
                if r + 1 < len(diff):
                    diff[r + 1] -= 1

            effect = [0] * n
            effect[0] = diff[0]
            for i in range(1, n):
                effect[i] = effect[i - 1] + diff[i]

            for i in range(n):
                if effect[i] < nums[i]:
                    return False
            return True

        left = 0
        right = len(queries)
        best = -1

        while left <= right:
            mid = (left + right) // 2
            if can_remove(mid):
                best = mid
                left = mid + 1  
            else:
                right = mid - 1

        return best"""