"""
Because binary trees can become imbalanced (e.g. a sorted order is placed in them and they become a line),
it is often necessary to create structures to automatically balance them.

One such structure is the AVL Tree (another is the popular Red-Black Tree).

The AVL tree relies on a balance factor:

balanceFactor = height(leftSubTree) - height(rightSubTree)

A positive balanceFactor means that a tree is left-heavy.
A negative balanceFactor means that a tree is right-heavy.
A 0 balanceFactor means that a tree is balanced.

The AVL defines itself as out of balanced if the balanceFactor is not 1, 0, or -1

The AVL will inherit from the normal Binary_Search_Tree, but will auto-balance leaves as they are added.
If a new leaf is added to the left, this increases the balance of the parent (and its ancestors recursively).
If a new leaf is added to the right, this reduces the balance of the parent (and its ancestors recursively).

The base case for these recursive calls are:

1) It has reached the root node.
2) The balance factor of the parent has been adjusted to zero.


To rebalance a tree we need to perform ROTATIONS on the nodes to reposition them.

A Left Rotation does the following (if tree is A -> B -> C, where all are right children):

* Promote the right child (B) to be the root of the subtree.
* Move the old root (A) to be the left child of the new root.
* If new root (B) already had a left child then make it the right child of the new left child (A).
   Note: Since the new root (B) was the right child of A the right child of A is guaranteed to be empty at this point.
   This allows us to add a new node as the right child without any further consideration.


The Right Rotation is more complex and does the following (for image of example, see https://bradfieldcs.com/algos/trees/avl-trees/):


* Promote the left child (C) to be the root of the subtree.
* Move the old root (E) to be the right child of the new root.
* If the new root(C) already had a right child (D) then make it the left child of the new right child (E).
    Note: Since the new root (C) was the left child of E, the left child of E is guaranteed to be empty at this point.
    This allows us to add a new node as the left child without any further consideration.

A rotation, however, may bring a tree out of balance if children aren't in balance. Therefore, before rotating iterate
through this analysis:

* If a subtree needs a left rotation to bring it into balance, first check the balance factor of the right child.
    If the right child is left heavy then do a right rotation on right child, followed by the original left rotation.
* If a subtree needs a right rotation to bring it into balance, first check the balance factor of the left child.
    If the left child is right heavy then do a left rotation on the left child, followed by the original right rotation.

This is implemented in the `rebalance()` method.
"""

from .binary_search_tree import BinarySearchTree, TreeNode


class AVLTreeNode(TreeNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.balance_factor = 0


class AVLTree(BinarySearchTree):

    TreeNodeClass = AVLTreeNode

    def _put(self, key, val, node):
        if key < node.key:
            if node.left:
                self._put(key, val, node.left)
            else:
                node.left = self.TreeNodeClass(key, val, parent=node)
                self.update_balance(node.left)
        else:
            if node.right:
                self._put(key, val, node.right)
            else:
                node.right = self.TreeNodeClass(key, val, parent=node)
                self.update_balance(node.right)

    def update_balance(self, node):
        if node.balance_factor > 1 or node.balance_factor < -1:
            self.rebalance(node)
            return
        if node.parent is not None:
            if node.is_left_child():
                node.parent.balance_factor += 1
            elif node.is_right_child():
                node.parent.balance_factor -= 1

            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)

    def rotate_left(self, rotation_root):
        new_root = rotation_root.right
        rotation_root.right = new_root.left
        if new_root.left is not None:
            new_root.left.parent = rotation_root
        new_root.parent = rotation_root.parent
        if not rotation_root.parent:
            self.root = new_root
        else:
            if rotation_root.is_left_child():
                rotation_root.parent.left = new_root
            else:
                rotation_root.parent.right = new_root
        new_root.left = rotation_root
        rotation_root.parent = new_root
        rotation_root.balance_factor = rotation_root.balance_factor + 1 - min(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor + 1 + max(rotation_root.balance_factor, 0)

    def rotate_right(self, rotation_root):
        new_root = rotation_root.left
        rotation_root.left = new_root.right
        if new_root.right is not None:
            new_root.right.parent = rotation_root
        new_root.parent = rotation_root.parent
        if not rotation_root.parent:
            self.root = new_root
        else:
            if rotation_root.is_right_child():
                rotation_root.parent.right = new_root
            else:
                rotation_root.parent.left = new_root
        new_root.right = rotation_root
        rotation_root.parent = new_root
        rotation_root.balance_factor = rotation_root.balance_factor + 1 - min(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor + 1 + max(rotation_root.balance_factor, 0)

    def rebalance(self, node):
        if node.balance_factor < 0 and node.right:
            if node.right.balance_factor > 0:
                self.rotate_right(node.right)
                self.rotate_left(node)
            else:
                self.rotate_left(node)
        elif node.balance_factor > 0 and node.left:
            if node.left.balance_factor < 0:
                self.rotate_left(node.left)
                self.rotate_right(node)
            else:
                self.rotate_right(node)
