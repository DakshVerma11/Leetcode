# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0
        def dfs(cur,maximum):
            nonlocal count
            if cur is None:
                return

            if maximum<=cur.val:
                count+=1
                maximum=cur.val
            dfs(cur.left,maximum)
            dfs(cur.right,maximum)
        dfs(root,-1*float('inf'))
        return count