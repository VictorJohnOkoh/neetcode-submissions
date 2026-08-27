# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        return self.DFS(root, p, q)
    
    def DFS(self, root, p, q):
        if root.val == p.val or root.val == q.val:
            return root
        if (p.val > root.val and q.val < root.val) or (q.val > root.val and p.val < root.val):
            return root
        if p.val > root.val and q.val > root.val:
            return self.DFS(root.right, p, q)
        if p.val < root.val and q.val < root.val:
            return self.DFS(root.left, p, q)