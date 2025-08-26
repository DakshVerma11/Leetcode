class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diag,max_area=0,0


        for l,b in dimensions:
            diag=l*l+b*b

            if diag>max_diag:
                max_area=l*b
                max_diag=diag
            
            elif diag==max_diag and max_area<l*b:
                max_area=l*b
        return max_area