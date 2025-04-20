# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        return self.dfs(root, targetSum)

    def dfs(self, root, targetSum, sums=None):
        
        if root == None:
            return 0

        paths = 0

        if sums == None:
            sums = [root.val]
        else:
            for i in range(len(sums)):
                sums[i] += root.val
                if sums[i] == targetSum:
                    paths += 1

            sums.append(root.val)

        if root.val == targetSum:
            paths += 1

        nl = self.dfs(root.left, targetSum, sums[:])
        nr = self.dfs(root.right, targetSum, sums[:])

        paths += nl + nr
        
        return paths


def create_tree(nodes: List[int]) -> Optional[TreeNode]:
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while queue and i < len(nodes):
        current = queue.pop(0)
        if nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1
    return root


def print_tree(root: Optional[TreeNode], level=0):
    if root is not None:
        print(" " * (level * 4) + str(root.val))
        print_tree(root.left, level + 1)
        print_tree(root.right, level + 1)

nodes = [0, 1, 1]
tree = create_tree(nodes)
# print_tree(tree)

sol = Solution()
res = sol.pathSum(tree, 1)
print(res)