# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return
        self.invertTree(root.left) #The strategy is to invert the left and right subtrees recursively
        self.invertTree(root.right)

        newRight = root.left #First we save the left subtree as newRight
        newLeft = root.right #Then we save the right subtree as newLeft

        root.left = newLeft #Now we set the left subtree as newLeft
        root.right = newRight #And finally we set the right subtree as newRight

        return root   
def preOrder(root):
    if not root:
        return
    return root.val, preOrder(root.left), preOrder(root.right)

solution = Solution()
treeNode1 = TreeNode(2,TreeNode(1),TreeNode(3)) # We have to create the tree with one val that is going to be the root, 
#and then we create objects of, since they're new roots to the left and right subtrees

invertedNodes = solution.invertTree (treeNode1)

print(preOrder(invertedNodes))