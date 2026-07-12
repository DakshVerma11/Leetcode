# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not (preorder or inorder):
            return None
        
        rootIdx=inorder.index(preorder[0])
        
        #preorderLeft=preorder[1:rootIdx+1]
        #inorderLeft=inorder[:rootIdx]
        
        #root.left=self.buildTree(preorderLeft,inorderLeft)

        #preorderRight=preorder[rootIdx+1::]
        #inorderRight=inorder[rootIdx+1::]
        #root.right=self.buildTree(preorderRight,inorderRight)

        return TreeNode(preorder[0],self.buildTree(preorder[1:rootIdx+1],inorder[:rootIdx]),self.buildTree(preorder[rootIdx+1::],inorder[rootIdx+1::]))
        
        
        

        