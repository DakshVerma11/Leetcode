class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apsum=sum(apple)


        capacity.sort(reverse=True)
        i=0
        while apsum>0:
            apsum-=capacity[i]
            i+=1

        return i