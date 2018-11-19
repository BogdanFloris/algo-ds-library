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

    def in_order_walk(self, x: RBNode):
        if x is not nil:
            print(str(x.key) + ", c: " + str(x.color))
            self.in_order_walk(x.left)
            self.in_order_walk(x.right)

    def insert(self, key):
        """
        Insert the value into the tree.
        :param key: to be inserted
        """
        z: RBNode = RBNode(key)
        y = nil
        x = self.root
        while x is not nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = nil
        z.right = nil
        z.color = RED
        self._insert_fix_up(z)

    def _insert_fix_up(self, z: RBNode):
        """
        Fixes the properties of the Red Black Tree after inserting z
        :param z: inserted node
        """
        while z.parent.color is RED:
            if z.parent is z.parent.parent.left:
                y = z.parent.parent.right
                if y.color is RED:
                    # case 1
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z is z.parent.right:
                        # case 2
                        z = z.parent
                        self._left_rotate(z)
                    # case 3
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self._right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color is RED:
                    # case 1
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z is z.parent.left:
                        # case 2
                        z = z.parent
                        self._right_rotate(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self._left_rotate(z.parent.parent)
        self.root.color = BLACK

    def _left_rotate(self, x: RBNode):
        """
        Performs a left rotation around node x.
        :param x: the node to rotate around
        """
        y: RBNode = x.right
        x.right = y.left
        if y.left is not nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is nil:
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, y: RBNode):
        """
        Performs a right rotations around node y.
        :param y: the node to rotate around
        """
        x: RBNode = y.left
        y.left = x.right
        if x.right is not nil:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is nil:
            self.root = x
        elif y is y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        x.right = y
        y.parent = x


red_black_tree = RedBlackTree()
for i in range(1, 20):
    red_black_tree.insert(i)
red_black_tree.in_order_walk(red_black_tree.root)
