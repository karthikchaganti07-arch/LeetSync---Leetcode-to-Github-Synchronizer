# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.c=0
        def dfs(node):
            if not node:
                return 0,0
            l_sum,l_count=dfs(node.left)
            r_sum,r_count=dfs(node.right)
            c_sum=node.val+l_sum+r_sum
            c_count=1+l_count+r_count
            if c_sum//c_count==node.val:
                self.c+=1
            return c_sum,c_count
        dfs(root)
        return self.c