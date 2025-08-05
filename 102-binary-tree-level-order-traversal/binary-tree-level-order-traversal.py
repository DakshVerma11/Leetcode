# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=defaultdict(list)

        def inorder(cur,depth):
            if cur is None:
                return
            res[depth].append(cur.val)
            
            inorder(cur.left,depth+1)
            inorder(cur.right,depth+1)
        inorder(root,0)
        ans = [[] for _ in range(len(res))]
        for k,v in res.items():
            ans[k]=v
        return ans