# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(node):
            if not node:
                return (0,0)

            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            cur_sum = left_sum + right_sum + node.val
            cur_count = left_count + right_count + 1

            if node.val == cur_sum // cur_count:
                self.count += 1

            return (cur_sum,cur_count)
        
        dfs(root)
        return self.count