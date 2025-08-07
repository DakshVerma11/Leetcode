# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        current=[0,-1]


        def dfs(curr,k):
            if curr is None or current[0]>k:
                return 
            dfs(curr.left,k)
            current[0]+=1
            if current[0]==k:
                current[1]=curr.val
            
            dfs(curr.right,k)

        dfs(root,k)
        return current[1]