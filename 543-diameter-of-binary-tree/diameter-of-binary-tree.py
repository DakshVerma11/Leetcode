# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res=0

        def diameterCur(node):
            nonlocal res
            if not node:
                return 0
            leftDepth=diameterCur(node.left)
            rightDepth=diameterCur(node.right)

            if (leftDepth+rightDepth)>res:
                res=leftDepth+rightDepth
            return 1+max(leftDepth,rightDepth)
        diameterCur(root)
        return res