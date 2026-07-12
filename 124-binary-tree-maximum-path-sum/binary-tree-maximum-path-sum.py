# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath=root.val

        def curPathSum(node):
            nonlocal maxPath
            if not node:
                return 0
            
            leftPathSum=curPathSum(node.left)
            rightPathSum=curPathSum(node.right)

            maxPath=max(maxPath,node.val+leftPathSum+rightPathSum,node.val+leftPathSum,node.val+rightPathSum,node.val)
            return node.val+max(leftPathSum,rightPathSum,0)
        curPathSum(root)
        return maxPath