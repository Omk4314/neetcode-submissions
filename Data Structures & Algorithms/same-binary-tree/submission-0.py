# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pl = self.traversal(p)
        ql = self.traversal(q)
        pl_len = len(pl)
        if pl_len == len(ql):
            for i in range(pl_len):
                if pl[i] != ql[i]:
                    return False
            return True
        return False
        
    def traversal(self, root):
        if not root:
            return [None]
        return [root.val] + self.traversal(root.left) + self.traversal(root.right)