# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, min_range, max_range):
            if not node:
                return True
            if not (min_range < node.val < max_range):
                return False
            return (dfs(node.left, min_range, node.val) and 
                dfs(node.right, node.val, max_range))
        return dfs(root, float('-inf'), float('inf'))
