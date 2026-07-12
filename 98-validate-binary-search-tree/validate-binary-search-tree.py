# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def checkBST(node):
            if not node:
                return True, float('inf'), float('-inf'),

            leftisBST,leftmin,leftmax=checkBST(node.left)
            rightisBST,rightmin,rightmax=checkBST(node.right)

            if leftisBST and rightisBST and leftmax<node.val<rightmin:
                return (
                    True,
                    min(leftmin,node.val),
                    max(rightmax,node.val)
                )
            return (
                False,
                0,
                0
            )
        return checkBST(root)[0]