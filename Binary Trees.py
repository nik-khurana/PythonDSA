#TODO Binary Tree Traversals LC
# inorder traversal
# Traverse the left subtree, i.e., call Inorder(left->subtree)
# Visit the root.
# Traverse the right subtree, i.e., call Inorder(right->subtree)
# uses
# In the case of binary search trees (BST), Inorder traversal gives nodes in non-decreasing order.
# To get nodes of BST in non-increasing order, a variation of Inorder traversal where Inorder traversal is reversed can be used.
# Inorder traversal can be used to evaluate arithmetic expressions stored in expression trees.
# https://leetcode.com/problems/binary-tree-inorder-traversal/

def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    else:
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

#TODO preordertraversal
# Visit the root.
# Traverse the left subtree
# Traverse the right subtree
# uses
# Preorder traversal is used to create a copy of the tree.
# Preorder traversal is also used to get prefix expressions on an expression tree.
# https://leetcode.com/problems/binary-tree-preorder-traversal/submissions/1245901461/

def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    else:
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

#TODO postorder traversal
# Traverse the left subtree, i.e., call Postorder(left->subtree)
# Traverse the right subtree, i.e., call Postorder(right->subtree)
# Visit the root
# uses
# Postorder traversal is used to delete the tree. See the question for the deletion of a tree for details.
# Postorder traversal is also useful to get the postfix expression of an expression tree.
# Postorder traversal can help in garbage collection algorithms, particularly in systems where manual memory management is used.
# https://leetcode.com/problems/binary-tree-postorder-traversal/description/

def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    else:
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

#TODO min height of tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

def minDepth(self, root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    if root.left is None and root.right is not None:
        return 1 + self.minDepth(root.right)
    if root.left is not None and root.right is None:
        return 1 + self.minDepth(root.left)
    return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

#TODO max height of tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

def maxDepth(self, root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    if root.left is None and root.right is not None:
        return 1 + self.maxDepth(root.right)
    if root.left is not None and root.right is None:
        return 1 + self.maxDepth(root.left)
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

#TODO count no of nodes in a tree
# https://leetcode.com/problems/count-complete-tree-nodes/

def countNodes(self, root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    if root.left is None and root.right is not None:
        return 1 + self.countNodes(root.right)
    if root.left is not None and root.right is None:
        return 1 + self.countNodes(root.left)
    return 1 + self.countNodes(root.left) + self.countNodes(root.right)

#TODO diameter of binary tree
# distance bw 2 nodes