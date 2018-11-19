"""
A Red Black Tree (RBT) is a balanced binary search tree.
It has the following properties:
 - Every node is either red or black
 - The root is black
 - Every leaf NIL is black
 - If a node is red, then both its children are black
 - For each node, all simple paths from the node to descendant leaves
   contain the same number of black nodes
"""
# black color
BLACK = 0
# red color
RED = 1


class RBNode:
    """
    Represents a node of a Red Black Tree
    """
    def __init__(self, key=None):
        # color of the node
        self.color = BLACK
        # initialize parent, left child and right child
        self.parent: RBNode = None
        self.left: RBNode = None
        self.right: RBNode = None
        # number of elements to the left of this node
        self.num_left = 0
        # number of elements to the right of this node
        self.num_right = 0
        # set key
        self.key = key


# the NIL node of the Red Black Tree
nil: RBNode = RBNode()


class RedBlackTree:
    def __init__(self):
        self.root: RBNode = nil
        self.root.parent = nil
        self.root.left = nil
        self.root.right = nil
