# Time Complexity : O(n), where n is the number of nodes in the binary tree
# Space Complexity : O(w), where w is the maximum width of the tree (can be O(n) in worst case)
# Did this code successfully run on Leetcode : YES
# Any problem you faced while coding this : No

from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        
        # BFS with level tracking
        q = deque()
        q.append(root)
        res = []

        while q:
            size = len(q)
            max_val = float("-inf")
            for _ in range(size):
                node = q.popleft()
                max_val = max(max_val, node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(max_val)

        return res

        # ---------------------------------------
        # Alternative 1: BFS with (node, level) tracking
        # Time Complexity : O(n)
        # Space Complexity : O(w), where w is the maximum width of the tree (up to O(n))

        # if not root:
        #     return []
        # q = deque([(root, 0)])
        # res = []
        # while q:
        #     node, level = q.popleft()
        #     if level == len(res):
        #         res.append(node.val)
        #     else:
        #         res[level] = max(res[level], node.val)
        #     if node.left:
        #         q.append((node.left, level + 1))
        #     if node.right:
        #         q.append((node.right, level + 1))
        # return res

        # ---------------------------------------
        # Alternative 2: DFS (Pre-order)
        # Time Complexity : O(n)
        # Space Complexity : O(h), where h is the height of the tree (O(log n) for balanced, O(n) worst case)

        # res = []
        # def dfs(node, level):
        #     if not node:
        #         return
        #     if level == len(res):
        #         res.append(node.val)
        #     else:
        #         res[level] = max(res[level], node.val)
        #     dfs(node.left, level + 1)
        #     dfs(node.right, level + 1)
        # dfs(root, 0)
        # return res
