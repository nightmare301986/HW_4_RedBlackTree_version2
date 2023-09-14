class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.color = 1  # 1 for red, 0 for black

class RedBlackTree:
    def __init__(self):
        self.null_node = Node(None)
        self.null_node.color = 0
        self.root = self.null_node

    def insert(self, key):
        new_node = Node(key)
        new_node.left = self.null_node
        new_node.right = self.null_node
        parent = None
        current = self.root
        while current != self.null_node:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right
        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node
        if new_node.parent is None:
            new_node.color = 0
            return
        if new_node.parent.parent is None:
            return
        self._rebalance(new_node)

    def _rebalance(self, new_node):
        while new_node.parent.color == 1:
            if new_node.parent == new_node.parent.parent.right:
                uncle = new_node.parent.parent.left
                if uncle.color == 1:
                    uncle.color = 0
                    new_node.parent.color = 0
                    new_node.parent.parent.color = 1
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self._right_rotate(new_node)
                    new_node.parent.color = 0
                    new_node.parent.parent.color = 1
                    self._left_rotate(new_node.parent.parent)
            else:
                uncle = new_node.parent.parent.right
                if uncle.color == 1:
                    uncle.color = 0
                    new_node.parent.color = 0
                    new_node.parent.parent.color = 1
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self._left_rotate(new_node)
                    new_node.parent.color = 0
                    new_node.parent.parent.color = 1
                    self._right_rotate(new_node.parent.parent)
            if new_node == self.root:
                break
        self.root.color = 0

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.null_node:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.null_node:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def inorder_traversal(self, node):
        if node != self.null_node:
            self.inorder_traversal(node.left)
            print(node.key, end=" ")
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        if node != self.null_node:
            print(node.key, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node != self.null_node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.key, end=" ")

    def level_order_traversal(self, node):
        if self.root == self.null_node:
            return
        queue = []
        queue.append(self.root)
        while len(queue) > 0:
            node = queue.pop(0)
            print(node.key, end=" ")
            if node.left != self.null_node:
                queue.append(node.left)
            if node.right != self.null_node:
                queue.append(node.right)

    def print_tree(self):
        self.inorder_traversal(self.root)
        print('')
        self.preorder_traversal(self.root)
        print('')
        self.postorder_traversal(self.root)
        print('')
        self.level_order_traversal(self.root)

tree = RedBlackTree()
for i in range(1,21):
    tree.insert(i)

#tree.insert(6)
#tree.insert(8)
#tree.insert(1)
#tree.insert(13)
#tree.insert(20)
#tree.insert(21)
#tree.insert(27)
#tree.insert(25)

tree.print_tree()