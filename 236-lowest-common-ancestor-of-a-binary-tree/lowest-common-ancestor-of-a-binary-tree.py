# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res=None

        #for each node well check if the node is not nul (false)
        #if node is p or node is q -> node.left has other or node.right has other -> cur is res
        #else propogate upwards and return first where node.left and node.right


        def postfix(node):
            nonlocal res
            if not node:
                return False
            left=postfix(node.left)
            right=postfix(node.right)
            if node==p or node==q:
                if left or right:
                    res=node
                return True
            else:
                if left and right:
                    res=node
                return left or right
            
        postfix(root)
        return res
            