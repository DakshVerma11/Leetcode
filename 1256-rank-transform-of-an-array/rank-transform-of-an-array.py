class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arrSorted=sorted(arr)
        n=len(arr)
        pos={}
        rank=0
        #print(arrSorted)
        for i in range(n):
            #print(arrSorted[i],pos)
            if i<n-1 and arrSorted[i+1]==arrSorted[i]:
                #print(i,"here")
                continue
            else:
                rank+=1
                pos[arrSorted[i]]=rank
        #print(pos)
        for i in range(n):
            arr[i]=pos[arr[i]]
        return arr