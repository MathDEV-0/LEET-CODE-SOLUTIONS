# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def nodeHeight(node):
            if not node: 
                return 0

            leftHeight = nodeHeight(node.left)
            if leftHeight == -1:
                return -1
            
            rightHeight = nodeHeight(node.right)
            if rightHeight == -1:
                return -1
            
            if leftHeight - rightHeight > 1 or leftHeight - rightHeight < -1:
                return -1
            
            return max(leftHeight,rightHeight)
        return nodeHeight(root) != -1
        
#root = [3,9,20,null,null,15,7] Left: 2*i+1, Right: 2*i + 2 for a node at index i
solution = Solution()
treeNode1 = TreeNode(3)
treeNode1.left = TreeNode(9)
treeNode1.right = TreeNode(20)
treeNode1.right.left = TreeNode(15)
treeNode1.right.right = TreeNode(7)
print(solution.isBalanced(treeNode1))
