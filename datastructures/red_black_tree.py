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

    def minimum(self, x: RBNode=None):
        """
        Finds the minimum starting at x
        :param x: root
        :return: minimum
        """
        if x is None:
            x = self.root
        while x.left is not nil:
            x = x.left
        return x

    def maximum(self, x: RBNode=None):
        """
        Finds the maximum starting at x
        :param x: root
        :return: maximum
        """
        if x is None:
            x = self.root
        while x.right is not nil:
            x = x.right
        return x

    def successor(self, x: RBNode):
        """
        Finds the successor of x
        :param x: root
        :return: the successor
        """
        if x.right is not nil:
            return self.minimum(x.right)
        y = x.parent
        while y is not nil and x is y.right:
            x = y
            y = y.parent
        return y

    def predecessor(self, x: RBNode):
        """
        Finds the predecessor of x
        :param x: root
        :return: the predecessor
        """
        if x.left is not nil:
            return self.maximum(x.left)
        y = x.parent
        while y is not nil and x is y.left:
            x = y
            y = y.parent
        return y

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

    def delete(self, key):
        """
        Deletes the key from the tree.
        :param key: key to be deleted
        """
        z = self.search(self.root, key)
        y = z
        y_original_color = y.color
        if z.left is nil:
            x = z.right
            self._transplant(z, z.right)
        elif z.right is nil:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent is z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color is BLACK:
            self._delete_fix_up(x)

    def search(self, x: RBNode, key):
        """
        Searches for the key starting at x
        :param x: start
        :param key: key to be found
        :return: the node with the key
        """
        if x is nil or key == x.key:
            return x
        if key < x.key:
            return self.search(x.left, key)
        else:
            return self.search(x.right, key)

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

    def _delete_fix_up(self, x: RBNode):
        """
        Fixes the properties of the Red Black Tree after deletion
        :param x: starting node
        """
        while x is not self.root and x.color is BLACK:
            if x is x.parent.left:
                w = x.parent.right
                if w.color is RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self._left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color is BLACK and w.right.color is BLACK:
                    w.color = RED
                    x = x.parent
                else:
                    if w.right.color is BLACK:
                        w.left.color = BLACK
                        w.color = RED
                        self._right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.right.color = BLACK
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color is RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self._right_rotate(x.parent)
                    w = x.parent.left
                if w.left.color is BLACK and w.right.color is BLACK:
                    w.color = RED
                    x = x.parent
                else:
                    if w.left.color is BLACK:
                        w.right.color = BLACK
                        w.color = RED
                        self._left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.left.color = BLACK
                    self._right_rotate(x.parent)
                    x = self.root
        x.color = BLACK

    def _transplant(self, u: RBNode, v: RBNode):
        """
        Helper function for deletion
        :param u: root of subtree 1
        :param v: root of subtree 2
        """
        if u.parent is nil:
            self.root = v
        elif u is u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

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
