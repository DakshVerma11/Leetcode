class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        res = 0
        n = len(points)
        #points.sort()
        print(points)
        for i in range(n):
            for j in range(n):
                if i==j:
                    continue
                x1, y1 = points[i]
                x2, y2 = points[j]

                if x1 <= x2 and y1 >= y2:
                    canbesq = True
                    #print(x1,y2,'\t',x2,y2)
                    for k in range(n):
                        if k != i and k != j and x1 <= points[k][0] <= x2 and y2 <= points[k][1] <= y1:
                            canbesq = False
                            break
                    
                    if canbesq:
                        res += 1
        return res
